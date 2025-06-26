# AnchorEntity

**Framework**: RealityKit  
**Kind**: class

An anchor that tethers entities to a scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class AnchorEntity
```

## Mentions

- [Handling different-sized objects in physics simulations](handling-different-sized-objects-in-physics-simulations.md)
- [Taking Control of Scene Anchoring](taking-control-of-scene-anchoring.md)
- [Loading entities from a file](loading-entities-from-a-file.md)
- [Adding procedural assets to a scene](adding-procedural-assets-to-a-scene.md)

#### Overview

Control how RealityKit places virtual objects into your scene with anchor entities. `AnchorEntity` conforms to the [`HasAnchoring`](hasanchoring.md) protocol, which gives it an [`AnchoringComponent`](anchoringcomponent.md) instance.

RealityKit places anchors based on the anchoring component’s [`target`](anchoringcomponent/target-swift.property.md) property. For example, you can configure an anchor entity to rest on a horizontal surface that RealityKit detects in an AR scene like a table or floor, and RealityKit automatically places that anchor after it detects an appropriate horizontal plane in the real world. The example below creates an anchor to a horizontal surface:

```swift
AnchorEntity(.plane(.horizontal,
                    classification: .any,
                    minimumBounds: SIMD2<Float>(0.2, 0.2)
))
```

See [`Selecting an anchor for a Reality Composer scene`](selecting-an-anchor-for-a-reality-composer-scene.md) for more information about the different types of anchors available when using Reality Composer Pro.

![A diagram showing the components present in the anchor entity. It contains](https://docs-assets.developer.apple.com/published/e78311258ee5161ce72fbe286f53f45f/AnchorEntity-1%402x.png)

Add anchor entities directly to your scene’s [`anchors`](scene/anchors.md) collection, or anywhere else in the scene hierarchy by adding them to the `Entity/children` collection of another entity in your scene. Because `AnchorEntity` is a subclass of [`Entity`](entity.md), you can make an anchor entity a subentity of any other entity. RealityKit might move anchor entities as the scene updates, so the location and rotation of the anchor entity can change relative to its container entity, even if your code never modifies its `Entity/transform` property.

Some anchor entities might not show up in your scene at all if RealityKit fails to detect an appropriate place for them. For example, an anchor entity with an `image` target doesn’t show up in the scene until RealityKit detects the specified image in the real world.

![A block diagram showing how anchor entities attach to a scene, and how they](https://docs-assets.developer.apple.com/published/49a94f8af177d4ae0e15f0fa011c760a/AnchorEntity-2%402x.png)

You can have multiple anchors in a RealityKit scene. For example, one anchor can place a toy car on a horizontal surface, like a table, and another can tie an informative text bubble to an image in the same scene.

> **Note**: By default, physics bodies and colliders affect only entities that share the same anchor.

An entity and its descendants can participate in the physics simulation at the root of your scene by setting its `AnchoringComponent/physicsSimulation-swift.property` to `AnchoringComponent/PhysicsSimulation-swift.enum/none`.

## Topics

### Creating an anchor
- [init()](anchorentity/init.md)
  Creates a new anchor entity.
- [convenience init(any Anchor)](anchorentity/init(_:)-8k2z3.md)
- [init(AnchoringComponent.Target)](anchorentity/init(_:)-9rdwu.md)
  Creates an anchor entity targeting a particular kind of anchor.
- [convenience(_:trackingMode:)](anchorentity/init(_:trackingmode:).md)
- [convenience(_:trackingMode:physicsSimulation:)](anchorentity/init(_:trackingmode:physicssimulation:).md)
- [convenience init(anchor: ARAnchor)](anchorentity/init(anchor:).md)
  Creates an anchor entity that uses an existing AR anchor.
- [convenience init(plane: AnchoringComponent.Target.Alignment, classification: AnchoringComponent.Target.Classification, minimumBounds: SIMD2<Float>)](anchorentity/init(plane:classification:minimumbounds:).md)
  Creates an anchor entity that targets a plane with the given characteristics.
- [convenience init(raycastResult: ARRaycastResult)](anchorentity/init(raycastresult:).md)
  Creates an anchor entity using the information about a real-world surface discovered using a ray-cast query.
- [convenience init(world: float4x4)](anchorentity/init(world:)-4snw2.md)
  Creates an anchor entity with a target fixed at the given position in the scene.
- [convenience init(world: SIMD3<Float>)](anchorentity/init(world:)-u9qv.md)
  Creates an anchor entity with a target fixed at the given position in the scene.
### Initializers
- [convenience(_:)](anchorentity/init(_:).md)
- [convenience(world:)](anchorentity/init(world:).md)
  Creates an anchor entity with a target fixed at the given position in the scene.

## Relationships

### Inherits From
- [Entity](entity.md)
### Conforms To
- [CoordinateSpace3D](../Spatial/CoordinateSpace3D.md)
- [CoordinateSpace3DFloat](../Spatial/CoordinateSpace3DFloat.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [EventSource](eventsource.md)
- [HasAnchoring](hasanchoring.md)
- [HasHierarchy](hashierarchy.md)
- [HasSynchronization](hassynchronization.md)
- [HasTransform](hastransform.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Observable](../Observation/Observable.md)
- [RealityCoordinateSpace](realitycoordinatespace.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AnchoringComponent](anchoringcomponent.md)
  A component that anchors virtual content to a real world target.
- [AnchoringComponent.Target](anchoringcomponent/target-swift.enum.md)
  Defines the kinds of real world objects to which an anchor entity can be tethered.
- [struct ARKitAnchorComponent](arkitanchorcomponent.md)
- [protocol HasAnchoring](hasanchoring.md)
  An interface that enables anchoring of virtual content to a real-world object in an AR scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchorentity)*