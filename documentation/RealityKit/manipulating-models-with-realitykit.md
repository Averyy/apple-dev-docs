# Manipulating models with RealityKit

**Framework**: RealityKit

Interact with detailed 3D models using manipulation and clipping controls.

**Availability**:
- visionOS 27.0+
- Xcode 27.0+

#### Overview

This sample loads a structured 3D model, such as an engine assembly, into an immersive space and provides the tools to take it apart and look inside. The sample highlights two RealityKit components:

- It uses a [`ManipulationComponent`](manipulationcomponent.md) to let a person move, rotate, and scale an entity with their hands; moving that component between the model’s root and its individual parts switches between manipulating the whole model and each piece on its own.
- To look inside the engine, it applies [`ClippingComponent`](clippingcomponent.md) to discard any geometry outside an adjustable bounding box so a person can slice through the model and expose its interior. This allows people to expand the model’s parts along its natural axis to reveal how the pieces fit together.

![An expanded view of an engine assembly, with the major parts spread apart along a vertical axis to reveal the interior structure.](/images/com.apple.RealityKit/manipulating-models-with-realitykit-PageImage-card@2x.png)

> **Note**: This sample code project is associated with WWDC26 session 284: [`Collaborate on structured 3D models in visionOS`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2026/284).

#### Choose a Model and Display Controls

When the app launches, `ContentView` offers two ways to bring in a model: open the bundled engine model, or pick an external USD with the system file importer.

```swift
var body: some View {
    @Bindable var appModel = appModel
    VStack {
        Button("Open Default Model") {
            appModel.selectDefaultModel()
        }

        Button("Select Model File…") {
            appModel.presentFileImporter()
        }
    }
    .padding()
    .fileImporter(
        isPresented: $appModel.isFileImporterPresented,
        allowedContentTypes: AppModel.supportedContentTypes
    ) { result in
        if case .success(let url) = result {
            appModel.selectModel(url: url)
        }
    }
}
```

The sample includes the default model for reference. An external model must provide a USD hierarchy that organizes the meshes into named, nested parts, because the manipulation, clipping, and expansion features all operate on that tree.

After choosing either the bundled engine model or an external file, the app presents that model in an immersive space. `ImmersiveView` loads the model into that space and adds a second entity to host the controls. The toolbar is an ordinary SwiftUI view, wrapped in a [`ViewAttachmentComponent`](viewattachmentcomponent.md) for use in the [`RealityView`](realityview.md).

```swift
private func makeControlsEntity() -> Entity {
    let entity = Entity()

    let controlsAttachment = ViewAttachmentComponent(rootView: ImmersiveControlsView().environment(appModel))
    entity.viewAttachmentComponent = controlsAttachment
    entity.position = Self.controlsPosition

    return entity
}
```

`ImmersiveControlsView` arranges the controls in a capsule along the bottom of the view, and includes an exit button, the primary model actions (lock, expand, and clipping), and a button that toggles the model hierarchy panel. The following sections discuss these primary actions.

#### Load a Model and Make It Manipulable

The sample loads a model from a URL and configures it for interaction in one place. It creates the entity with [`init(contentsOf:withName:)`](entity/init(contentsof:withname:).md), then attaches a collision shape to each part so gestures can find them, adds a [`ManipulationComponent`](manipulationcomponent.md) so a person can move, rotate, and scale the model with their hands, and adds the input and hover components that gestures depend on. For other ways to bring a model into your app, see [`Loading entities from a file`](loading-entities-from-a-file.md).

```swift
private func makeModelEntity(from url: URL) async throws -> Entity {
    // Load with `Entity`, not `ModelEntity`, to preserve the part hierarchy that assembly
    // expansion, the outline view, and per-leaf collision shapes depend on.
    let entity = try await Entity(contentsOf: url)

    // Attach a convex-hull `CollisionComponent` to every leaf entity that owns a
    // `ModelComponent`. The shapes are built once from each mesh, so opening or
    // closing the assembly later doesn't have to rebuild collision from visual bounds.
    await entity.attachLeafCollisionShapes()

    let bounds = entity.visualBounds(recursive: true, relativeTo: entity)

    // Configure the manipulation component.
    var manipulation = ManipulationComponent()
    // The model stays wherever the person leaves it, rather than snapping back to its origin.
    manipulation.releaseBehavior = .stay
    entity.manipulationComponent = manipulation

    // Configure clipping bounds cache using the model's visual bounds.
    let clippingBoundsCache = ClippingBoundsCacheComponent(storedClippingBounds: bounds)
    entity.clippingBoundsCacheComponent = clippingBoundsCache

    // `InputTargetComponent` turns on gesture recognition.
    // `HoverEffectComponent` provides visual feedback when the person looks at the model.
    entity.inputTargetComponent = InputTargetComponent()
    entity.hoverEffectComponent = HoverEffectComponent()

    // Position and scale the entity to fit comfortably in the view.
    let maxExtent = max(bounds.extents.x, bounds.extents.y, bounds.extents.z)
    let scale = Self.targetModelSize / maxExtent
    entity.scale = [scale, scale, scale]
    entity.position = Self.modelPosition - (bounds.center * scale)

    return entity
}
```

A `ManipulationComponent` performs gestures only where an entity has a [`CollisionComponent`](collisioncomponent.md), so the sample gives every part its own collider up front with `attachLeafCollisionShapes()`. Setting [`releaseBehavior`](manipulationcomponent/releasebehavior-swift.property.md) to [`stay`](manipulationcomponent/releasebehavior-swift.struct/stay.md) leaves the model wherever a person puts it instead of snapping the model back to its origin. The `attachLeafCollisionShapes()` method also records the model’s bounds in a custom `ClippingBoundsCacheComponent`. The clipping feature reads the model’s bounds later, and scales the entity so its largest dimension fits a target size in the view.

The collision work happens once, at load. `attachLeafCollisionShapes()` walks the model’s subtree, collects every entity that has a [`ModelComponent`](modelcomponent.md), and builds a convex-hull [`ShapeResource`](shaperesource.md) from each mesh. Because generating those shapes can be expensive, the method distributes the work across a task group and applies each result as it arrives.

```swift
func attachLeafCollisionShapes() async {
    // Collect every (entity, mesh) pair up front to distribute the work.
    var targets: [(entity: Entity, mesh: MeshResource, name: String)] = []
    var stack: [Entity] = [self]
    while let entity = stack.popLast() {
        if let mesh = entity.components[ModelComponent.self]?.mesh {
            targets.append((entity, mesh, entity.name))
        }
        stack.append(contentsOf: entity.children)
    }

    await withTaskGroup(of: (Int, ShapeResource?, String?).self) { group in
        for (index, target) in targets.enumerated() {
            let mesh = target.mesh
            group.addTask {
                do {
                    let shape = try await ShapeResource.generateConvex(from: mesh)
                    return (index, shape, nil)
                } catch {
                    return (index, nil, "\(error)")
                }
            }
        }

        for await (index, shape, errorDescription) in group {
            if let shape {
                targets[index].entity.collisionComponent =
                    CollisionComponent(shapes: [shape], mode: .trigger)
            } else if let errorDescription {
                Logger.logger.error(
                    "Failed to build collision shape for \(targets[index].name): \(errorDescription)"
                )
            }
        }
    }
}
```

Because each leaf keeps its collider for the lifetime of the model, switching between whole-model and per-part interaction never has to add, remove, or recompute collision shapes.

The immersive view calls `makeModelEntity(from:)` inside a [`RealityView`](realityview.md) and adds the result to the scene, alongside the controls entity from the previous section.

```swift
private func loadModel(from url: URL, into content: RealityViewContent) async {
    // Because the file was selected with the system file importer from outside the app sandbox,
    // obtain security-scoped access before reading it.
    let didStartAccessing = url.startAccessingSecurityScopedResource()
    defer {
        if didStartAccessing {
            url.stopAccessingSecurityScopedResource()
        }
    }
    do {
        let entity = try await makeModelEntity(from: url)
        content.add(entity)
        content.add(makeControlsEntity())
        appModel.modelEntity = entity
        appModel.setupClippingObservation(for: entity)
        appModel.isModelLoaded = true
    } catch {
        Logger.logger.error("Failed to load the model from \(url): \(error)")
    }
}
```

For more information about configuring entities for direct manipulation, see [`Manipulating entities with solid collisions`](https://developer.apple.com/documentation/visionos/manipulating-entities-with-solid-collisions).

#### Lock and Unlock the Model

The locking control locks and unlocks the model. The model starts locked, with the [`ManipulationComponent`](manipulationcomponent.md) on the root so the whole assembly moves as one. Unlocking moves manipulation onto the individual parts instead. The `toggleModelLock()` method alternates between these two configurations.

```swift
/// Toggle whether to lock or unlock the model for direct manipulation.
func toggleModelLock() {
    guard let entity = modelEntity else { return }
    isModelLocked.toggle()
    if isModelLocked {
        entity.closeAssembly()
    } else {
        entity.openAssembly()
    }
}
```

When the model unlocks, `openAssembly()` removes the manipulation and input components from the root so gestures pass through, then adds an input target and its own `ManipulationComponent` to each part. The parts already retain their colliders from initial load.

```swift
/// Opens the assembly by enabling individual manipulation of each child part.
func openAssembly() {
    // Remove manipulation from the root so gestures pass through to individual children.
    manipulationComponent = nil
    inputTargetComponent = nil

    for child in assemblyChildren {
        child.inputTargetComponent = InputTargetComponent()

        var manipulation = ManipulationComponent()
        manipulation.releaseBehavior = .stay
        child.manipulationComponent = manipulation
    }
}
```

Locking the model again reverses the process: `closeAssembly()` removes those components from the parts and restores them on the root, so the model moves as a single object with its internal layout intact. The geometry and the hierarchy never change; only where the components live in the tree does. The sample identifies the parts with `assemblyParent`, which descends to the first entity with more than one part — the parts a person manipulates when the model is unlocked.

#### Expand and Collapse the Model

The expansion control expands the assembly, then collapses it back. Expanding also unlocks the model, and collapsing re-locks it. The `toggleModelExpansion()` method handles both directions.

```swift
/// Toggle the expansion state of the model, spreading parts apart or restoring them.
func toggleModelExpansion() {
    guard let entity = modelEntity else { return }
    guard let parent = entity.assemblyParent else { return }
    isModelExpanded.toggle()
    if isModelExpanded {
        if isModelLocked {
            toggleModelLock()
        }
        // Save initial transforms so parts can animate back to their original positions.
        for child in parent.children {
            initialChildTransforms[child.id] = child.transform
        }
        parent.expandAlongPrimaryAxis(offset: 0.01)
    } else {
        for child in parent.children {
            guard let savedTransform = initialChildTransforms[child.id] else { continue }
            child.move(to: savedTransform, relativeTo: child.parent, duration: 0.3)
        }
        initialChildTransforms.removeAll()
        if !isModelLocked {
            toggleModelLock()
        }
    }
}
```

Before expanding, the app records each part’s transform so it can animate the pieces home later. Expanding delegates to the model entity’s `expandAlongPrimaryAxis(offset:)`, which chooses a direction and lays out the parts along it. Collapsing moves each part back to its saved transform with [`move(to:relativeTo:duration:timingFunction:)`](hastransform/move(to:relativeto:duration:timingfunction:).md) before locking it again.

#### Choose the Expansion Axis

To expand the assembly, the sample first determines an expansion axis. The `findOptimalAxisForExpansion()` method chooses the axis along which the parts are most spread out, weighting each part by its bounding-box volume so large structural components count for more than small pieces.

```swift
private func findOptimalAxisForExpansion() -> Axis3D {
    let variances = calculateVolumeWeightedPositionVariance()
    let axis: Axis3D
    if variances.z > variances.x && variances.z > variances.y {
        axis = .zAxis
    } else if variances.y > variances.z && variances.y > variances.x {
        axis = .yAxis
    } else {
        axis = .xAxis
    }
    return axis
}
```

The variance calculation collects each child’s bounding-box center and volume, computes a volume-weighted mean position, and sums the squared, volume-weighted deviations along each axis. The axis with the largest variance becomes the expansion direction. For an assembly built around a primary axis (like the bundled engine whose major parts stack vertically), that direction matches the one a person would intuitively choose, but does so automatically.

```swift
private func calculateVolumeWeightedPositionVariance() -> SIMD3<Float> {
    guard children.count > 1 else { return .zero }

    // `visualBounds(recursive: true)` is expensive. The app caches bounds in entity-local
    // space at load time and reuses them here rather than recomputing the full hierarchy.
    let centerAndVolume = children.compactMap { child -> (SIMD3<Float>, Float)? in
        let bounds = child.visualBounds(recursive: true, relativeTo: self)
        let extents = bounds.extents
        let volume = extents.x * extents.y * extents.z
        return (bounds.center, volume)
    }

    guard !centerAndVolume.isEmpty else { return .zero }

    let positions = centerAndVolume.map(\.0)
    let volumes = centerAndVolume.map(\.1)
    let totalVolume = volumes.reduce(0, +)
    guard totalVolume > 0 else { return .zero }

    let mean = zip(positions, volumes)
        .map { $0 * $1 }
        .reduce(.zero, +) / totalVolume

    return zip(positions, volumes)
        .map { position, volume in
            let diff = position - mean
            return SIMD3<Float>(
                diff.x * diff.x * volume,
                diff.y * diff.y * volume,
                diff.z * diff.z * volume
            )
        }
        .reduce(.zero, +) / totalVolume
}
```

#### Animate the Parts Into Place

With an axis chosen, `layoutChildren(along:additionalOffset:)` sorts the parts along that direction and positions each one just past the previous part. The method adds a small gap between the parts that stays visually consistent at any model scale. It animates each part with a [`FromToByAction`](fromtobyaction.md) in [`FromToByAction.TransformMode.scene`](fromtobyaction/transformmode/scene.md) mode, so the motion stays correct even if a person moves or rotates the model midanimation.

```swift
private func animateChild(_ child: Entity, along axis: Axis3D, delta: Float) {
    let childPos = child.position(relativeTo: self)
    let newLocalPos = axis.set(value: axis.value(for: childPos) + delta, for: childPos)
    let newWorldPos = convert(position: newLocalPos, to: nil)

    // Use a world-space (scene mode) transform so the animation remains correct even if
    // the parent entity is moving or the person rotates the model midanimation.
    var transform = Transform(matrix: child.transformMatrix(relativeTo: nil))
    transform.translation = newWorldPos

    let action = FromToByAction(to: transform,
                                mode: .scene,
                                timing: .easeInOut,
                                isAdditive: false)
    if let animation = try? AnimationResource.makeActionAnimation(
        for: action, bindTarget: .transform
    ) {
        child.playAnimation(animation)
    }
}
```

Because each part already carries a [`ManipulationComponent`](manipulationcomponent.md) whose [`releaseBehavior`](manipulationcomponent/releasebehavior-swift.property.md) is [`stay`](manipulationcomponent/releasebehavior-swift.struct/stay.md), it holds its new position when the animation finishes and a person grabs it. Locking remains available while expanding the model to allow re-locking the expanded view and repositioning it as a single unit.

#### Clip Through the Model with Planes

The clipping control slices through the model so a person can see a cross section of its interior. The sample drives clipping as a three-state machine (off, active, and editing) stored on the entity, through a `clippingState` accessor. Changing the state adds or removes a [`ClippingComponent`](clippingcomponent.md) and caches the current bounds.

```swift
/// The current clipping state, controlling whether the entity is actively clipped.
var clippingState: ClippingBoundsCacheComponent.ClippingState {
    get {
        clippingBoundsCacheComponent?.clippingState ?? .off
    }
    set {
        if newValue == clippingState { return }
        clippingBoundsCacheComponent?.clippingState = newValue
        let shouldClip = (newValue == .active || newValue == .editing)
        locallyUpdateIsClipped(shouldClip)
    }
}
```

The private `locallyUpdateIsClipped(_:)` does the component work. It adds a `ClippingComponent` with the cached bounds and sets [`shouldClipChildren`](clippingcomponent/shouldclipchildren.md) so clipping reaches the nested parts, or caches the current bounds before removing the component. Turning clipping off removes the `ClippingComponent` entirely, taking its bounds with it, so the sample stores those bounds in a separate `ClippingBoundsCacheComponent` that outlives the clip. Toggling clipping off and on restores the previous cross section instead of resetting to the model’s full bounds.

```swift
private func locallyUpdateIsClipped(_ newValue: Bool) {
    if newValue {
        if clippingComponent == nil {
            let bounds = clippingBoundsCacheComponent?.storedClippingBounds ?? BoundingBox()
            clippingComponent = ClippingComponent(bounds: bounds)
        } else if let bounds = clippingBoundsCacheComponent?.storedClippingBounds {
            clippingComponent?.bounds = bounds
        }
        clippingComponent?.shouldClipChildren = true
    } else {
        // Cache current bounds before removing the component so they persist for the next activation.
        if let bounds = clippingComponent?.bounds {
            clippingBoundsCacheComponent?.storedClippingBounds = bounds
        }
        clippingComponent = nil
    }
}
```

In the editing state, the `AppModel` object’s `handleClippingStateChange(for:newState:)` method adds a `ClippingControlEntity` (six draggable planes, one per face of the bounding box) as a sibling of the model, and removes it when editing ends. `clipEntity(_:)` fits the planes to the model’s bounds and attaches a transform-sync component so the planes follow the model as it moves.

```swift
/// Attaches clipping planes to the specified model entity and begins clipping.
/// - Parameter model: The entity to clip.
func clipEntity(_ model: Entity) throws {
    guard model.parent != nil else {
        throw ClippingControlError.clippedEntityMustHaveParent
    }

    let bounds = model.clippingBoundsCacheComponent?.storedClippingBounds
        ?? model.visualBounds(recursive: true, relativeTo: model)

    transform = model.transform
    makeFit(to: bounds)
    clippedEntity = model

    // Sync ensures the clipping planes follow the model if it moves, such as when using a drag gesture.
    model.clippingTransformSyncComponent = ClippingTransformSyncComponent(clippingControl: self)
}
```

#### Convert a Drag Into a Bounds Change

Each plane controls one scalar value of the bounding box, so dragging a plane moves it only along the axis normal to its face. The drag gesture arrives in the plane’s local coordinate space, but the clipping bounds live in the model’s space. The sample converts the drag delta into world space, then projects it onto the plane’s constrained direction so it discards any motion not perpendicular to the face.

```swift
private func computeConstrainedDelta(
    value: EntityTargetValue<DragGesture.Value>,
    activePlane: ClippingPlaneControlEntity
) -> SIMD3<Float> {
    // The gesture provides `location3D` in the plane's local coordinate space.
    let eventLocationInPlane = SIMD3<Float>(Float(value.location3D.x), Float(value.location3D.y), Float(value.location3D.z))
    // Convert to world-space so the app can compute a meaningful delta regardless of entity hierarchy.
    let eventLocationInWorld = value.entity.convert(position: eventLocationInPlane, to: nil)

    if firstEventLocationInWorld == nil {
        firstEventLocationInWorld = eventLocationInWorld
    }

    guard let firstLocation = firstEventLocationInWorld else { return .zero }
    let eventDeltaInWorld = eventLocationInWorld - firstLocation
    // Convert delta into entity-local space where axes are axis-aligned, making projection simple.
    let eventDeltaInLocal = convert(direction: eventDeltaInWorld, from: nil)

    // Project the drag delta onto the plane's constrained axis so the plane only moves perpendicular to its face.
    let localVector = activePlane.clippingPlane.constrainedDirection
    let constrainedDeltaInLocal = localVector * (dot(eventDeltaInLocal, localVector) / dot(localVector, localVector))

    // Convert back to world space for applying the position update.
    return convert(direction: constrainedDeltaInLocal, to: nil)
}
```

The expression `localVector * (dot(eventDeltaInLocal, localVector) / dot(localVector, localVector))` is the standard projection of one vector onto another. Because `constrainedDirection` is an axis-aligned unit vector (one of `{±1, 0, 0}`, `{0, ±1, 0}`, or `{0, 0, ±1}`), the projection keeps only the component of the drag along that single axis.

With the constrained delta in hand, the app trims one edge of the cached bounding box (`max` for a plane on the positive side of an axis, `min` for the negative side) and clamps the result inside the model’s bounds so a plane can’t move past the geometry.

```swift
private func trimmedBoundingBox(_ constrainedDeltaInWorld: SIMD3<Float>, _ positiveSide: Bool) throws -> BoundingBox {
    guard let clippedEntity else {
        throw ClippingControlError.clippedEntityNotFound
    }
    guard let boundsAtDragStart = clippedEntity.clippingBoundsCacheComponent?.storedClippingBounds else {
        throw ClippingControlError.missingStoredClippingBounds
    }

    // Work in entity-local space so bounds calculations remain valid regardless of world transform.
    let entityBounds = clippedEntity.visualBounds(recursive: true, relativeTo: clippedEntity)

    // Convert the world-space delta into entity-local space to adjust the bounding box edges.
    let constrainedDeltaInEntity = clippedEntity.convert(direction: constrainedDeltaInWorld, from: nil)

    if positiveSide {
        let newMax = boundsAtDragStart.max + constrainedDeltaInEntity
        let constrainedMax = entityBounds.constrain(newMax)
        return BoundingBox(lower: boundsAtDragStart.min, upper: constrainedMax)
    } else {
        let newMin = boundsAtDragStart.min + constrainedDeltaInEntity
        let constrainedMin = entityBounds.constrain(newMin)
        return BoundingBox(lower: constrainedMin, upper: boundsAtDragStart.max)
    }
}
```

#### Sync the Clipping Planes to the Model

While a clip is active, the model and its plane controls are separate entities. The planes have to follow whenever the model moves. The sample uses a [`System`](system.md) rather than a one-shot observer so the update runs every frame and the planes track the model without a frame of lag.

```swift
/// This uses a `System` rather than an `onChange` handler so it runs every frame,
/// keeping transforms in sync without a frame of lag.
final class ClippingTransformSyncSystem: System {
    /// A query that matches all entities with a clipping transform sync component.
    static let query = EntityQuery(where: .has(ClippingTransformSyncComponent.self))

    required init(scene: Scene) {}

    /// Update clipping control transforms to match their associated entities each frame.
    /// - Parameter context: The scene update context providing entity access.
    func update(context: SceneUpdateContext) {
        for entity in context.entities(matching: Self.query, updatingSystemWhen: .rendering) {
            guard var component = entity.clippingTransformSyncComponent else {
                continue
            }

            guard let control = component.clippingControl else {
                entity.clippingTransformSyncComponent = nil
                continue
            }

            let currentTransform = entity.transform
            // Only write when the transform actually changed to avoid sending unnecessary change notifications.
            if component.lastSyncedTransform != currentTransform {
                control.transform = currentTransform
                component.lastSyncedTransform = currentTransform
            }

            // Entity Component System (ECS) components are value types; write mutations back to the entity.
            entity.clippingTransformSyncComponent = component
        }
    }
}
```

The system matches every entity that carries a `ClippingTransformSyncComponent` using an [`EntityQuery`](entityquery.md), then copies the entity’s transform onto its clipping control. It writes the transform only when it actually changes, which avoids sending unnecessary change notifications each frame. The app registers the system once at startup, in the `AppModel` initializer, before any scene runs. For more information about systems and queries, see [`Implementing systems for entities in a scene`](implementing-systems-for-entities-in-a-scene.md).

#### View the Model Hierarchy

The hierarchy control toggles a panel that lists the model’s structure, so a person can see the asset’s organization and identify which components can be separated. `EntityHierarchyView` renders the loaded entity’s descendants with an [`OutlineGroup`](https://developer.apple.com/documentation/swiftui/outlinegroup) view.

```swift
var body: some View {
    if appModel.isHierarchyVisible, let entity = appModel.modelEntity {
        List {
            OutlineGroup(entity.childrenOrNil ?? [], children: \.childrenOrNil) { child in
                Label(child.name.isEmpty ? "Untitled" : child.name, systemImage: child.children.isEmpty ? "cube" : "folder")
                    .font(.subheadline)
            }
        }
        .listStyle(.plain)
        .padding(.vertical)
        .frame(width: 360, height: 560)
        .glassBackgroundEffect()
    }
}
```

Because the panel reads the live entities, it mirrors the names and grouping in the model’s USD hierarchy: the same tree that `assemblyParent` searches and that the lock and expand controls act on.

## See Also

- [Creating 3D entities with RealityKit](../visionos/creating-3d-entities-with-realitykit.md)
  Display a horizontal row of three-dimensional shapes in your visionOS app, using predefined mesh and white material.
- [Creating 3D models as movable windows](../visionos/creating-a-volumetric-window-in-visionos.md)
  Display 3D content with a volumetric window that people can move.
- [Creating a 3D painting space](../visionos/creating-a-painting-space-in-visionos.md)
  Implement a painting canvas entity, and update its mesh to represent a stroke.
- [Tracking and visualizing hand movement](../visionos/tracking-and-visualizing-hand-movement.md)
  Use hand-tracking anchors to display a visual representation of hand transforms in visionOS.
- [Applying mesh to real-world surroundings](../visionos/applying-mesh-to-real-world-surroundings.md)
  Add a layer of mesh to objects in the real world, using scene reconstruction in ARKit.
- [Obscuring virtual items in a scene behind real-world items](../visionos/obscuring-virtual-items-in-a-scene-behind-real-world-items.md)
  Increase the realism of an immersive experience by adding entities with invisible materials  real-world objects.
- [struct ModelComponent](modelcomponent.md)
  A component that contains a mesh and materials for the visual appearance of an entity.
- [class MeshResource](meshresource.md)
  A high-level representation of a collection of vertices and edges that define a shape.
- [class ModelEntity](modelentity.md)
  A representation of a physical object that RealityKit renders and optionally simulates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/manipulating-models-with-realitykit)*