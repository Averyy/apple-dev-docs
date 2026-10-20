# AnchorEntity

**Framework**: RealityKit  
**Kind**: class  
**Role**: Class

An anchor that tethers entities to a scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency class AnchorEntity
```

## Mentions

- [Handling different-sized objects in physics simulations](./handling-different-sized-objects-in-physics-simulations.md)
- [Loading entities from a file](./loading-entities-from-a-file.md)

#### Overview

Control how RealityKit places virtual objects into your scene with anchor entities. `AnchorEntity` conforms to the [`HasAnchoring`](./hasanchoring.md) protocol, which gives it an [`AnchoringComponent`](./anchoringcomponent.md) instance.

RealityKit places anchors based on the anchoring component’s [`target`](./anchoringcomponent/target-swift.property.md) property. For example, you can configure an anchor entity to rest on a horizontal surface that RealityKit detects in an AR scene like a table or floor, and RealityKit automatically places that anchor after it detects an appropriate horizontal plane in the real world. The example below creates an anchor to a horizontal surface:

```swift
AnchorEntity(.plane(.horizontal,
                    classification: .any,
                    minimumBounds: SIMD2<Float>(0.2, 0.2)
))
```

See [Creating an anchor](./anchorentity.md#Creating-an-anchor) for more information about the different types of anchors available when using Reality Composer Pro.

![A diagram showing the components present in the anchor entity. It contains](https://developer.apple.com/tutorials/images/com.apple.RealityKit/AnchorEntity-1@2x.png)

Add anchor entities directly to your scene’s [`anchors`](./scene/anchors.md) collection, or anywhere else in the scene hierarchy by adding them to the [`children`](./hashierarchy/children.md) collection of another entity in your scene. Because `AnchorEntity` is a subclass of [`Entity`](./entity.md), you can make an anchor entity a subentity of any other entity. RealityKit might move anchor entities as the scene updates, so the location and rotation of the anchor entity can change relative to its container entity, even if your code never modifies its [`transformMatrix(relativeTo:)`](./hastransform/transformmatrix%28relativeto%29.md) property.

Some anchor entities might not show up in your scene at all if RealityKit fails to detect an appropriate place for them. For example, an anchor entity with an `image` target doesn’t show up in the scene until RealityKit detects the specified image in the real world.

![A block diagram showing how anchor entities attach to a scene, and how they](https://developer.apple.com/tutorials/images/com.apple.RealityKit/AnchorEntity-2@2x.png)

You can have multiple anchors in a RealityKit scene. For example, one anchor can place a toy car on a horizontal surface, like a table, and another can tie an informative text bubble to an image in the same scene.

> **Note**: By default, physics bodies and colliders affect only entities that share the same anchor.

An entity and its descendants can participate in the physics simulation at the root of your scene by setting its [`physicsSimulation`](./anchoringcomponent/physicssimulation-swift.property.md) to

## Topics

### Creating an anchor
- [init()](./anchorentity/init%28%29.md)
  Creates a new anchor entity.
- [convenience init(any Anchor)](./anchorentity/init%28_%29-9vipc.md)
- [init(AnchoringComponent.Target)](./anchorentity/init%28_%29-9rdwu.md)
  Creates an anchor entity targeting a particular kind of anchor.
- [convenience init(AnchoringComponent.Target, trackingMode: AnchoringComponent.TrackingMode)](./anchorentity/init%28_,trackingmode%29.md)
- [convenience init(AnchoringComponent.Target, trackingMode: AnchoringComponent.TrackingMode, physicsSimulation: AnchoringComponent.PhysicsSimulation)](./anchorentity/init%28_,trackingmode,physicssimulation%29.md)
- [convenience init(anchor: ARAnchor)](./anchorentity/init%28anchor%29.md)
  Creates an anchor entity that uses an existing AR anchor.
- [convenience init(plane: AnchoringComponent.Target.Alignment, classification: AnchoringComponent.Target.Classification, minimumBounds: SIMD2<Float>)](./anchorentity/init%28plane,classification,minimumbounds%29.md)
  Creates an anchor entity that targets a plane with the given characteristics.
- [convenience init(raycastResult: ARRaycastResult)](./anchorentity/init%28raycastresult%29.md)
  Creates an anchor entity using the information about a real-world surface discovered using a ray-cast query.
- [convenience init(world: float4x4)](./anchorentity/init%28world%29-4snw2.md)
  Creates an anchor entity with a target fixed at the given position in the scene.
- [convenience init(world: SIMD3<Float>)](./anchorentity/init%28world%29-u9qv.md)
  Creates an anchor entity with a target fixed at the given position in the scene.
### Initializers
- [convenience(_:)](./anchorentity/init%28_%29.md)
- [convenience(world:)](./anchorentity/init%28world%29.md)
  Creates an anchor entity with a target fixed at the given position in the scene.

## Relationships

### Inherits From
- [Entity](./entity.md)
### Conforms To
- [CoordinateSpace3D](../Spatial/coordinatespace3d.md)
- [CoordinateSpace3DFloat](../Spatial/coordinatespace3dfloat.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [EventSource](./eventsource.md)
- [HasAnchoring](./hasanchoring.md)
- [HasHierarchy](./hashierarchy.md)
- [HasSynchronization](./hassynchronization.md)
- [HasTransform](./hastransform.md)
- [Hashable](../Swift/hashable.md)
- [Identifiable](../Swift/identifiable.md)
- [Observable](../Observation/observable.md)
- [RealityCoordinateSpace](./realitycoordinatespace.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Anchoring components
- [struct AnchoringComponent](./anchoringcomponent.md)
  A component that anchors virtual content to a real world target.
- [AnchoringComponent.Target](./anchoringcomponent/target-swift.enum.md)
  Defines the kinds of real world objects to which an anchor entity can be tethered.
- [AnchoringComponent.TrackingMode](./anchoringcomponent/trackingmode-swift.struct.md)
  Options for how an entity tracks its target anchor.
- [struct ARKitAnchorComponent](./arkitanchorcomponent.md)
  A component that exposes the backing ARKit data of an anchored entity.
- [protocol HasAnchoring](./hasanchoring.md)
  An interface that enables anchoring of virtual content to a real-world object in an AR scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchorentity)*