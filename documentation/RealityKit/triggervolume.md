# TriggerVolume

**Framework**: RealityKit  
**Kind**: class

An invisible 3D shape that detects when objects enter or exit a given region of space.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class TriggerVolume
```

#### Overview

A trigger volume is an entity that can participate in collisions because it has a [`CollisionComponent`](collisioncomponent.md). You use a trigger volume as a sensor that indicates when another collision-capable entity, like a [`ModelEntity`](modelentity.md), enters the region of space occupied by the trigger volume. You can use the generated [`CollisionEvents`](collisionevents.md) between the trigger volume and the other entity to trigger an action, like indicating to the user that a projectile hit its target.

![Diagram showing the components present in the trigger volume](https://docs-assets.developer.apple.com/published/ea980c874c628a17ed64dc62cfbc9d49/TriggerVolume-1%402x.png)

The trigger volume itself is very simple. It lacks any physical appearance, and doesn’t participate in physics simulations. This makes it very efficient for tasks that require only collision detection.

## Topics

### Creating a trigger volume
- [init()](triggervolume/init.md)
  Creates a trigger volume.
- [convenience init(shape: ShapeResource, filter: CollisionFilter)](triggervolume/init(shape:filter:).md)
  Creates a trigger volume with the given shape and collision filter.
- [init(shapes: [ShapeResource], filter: CollisionFilter)](triggervolume/init(shapes:filter:).md)
  Creates a trigger volume with the given composite shape and collision filter.

## Relationships

### Inherits From
- [Entity](entity.md)
### Conforms To
- [CoordinateSpace3D](../Spatial/CoordinateSpace3D.md)
- [CoordinateSpace3DFloat](../Spatial/CoordinateSpace3DFloat.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [EventSource](eventsource.md)
- [HasCollision](hascollision.md)
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

- [Simulating physics with collisions in your visionOS app](simulating-physics-with-collisions-in-your-visionos-app.md)
  Create entities that behave and react like physical objects in a RealityKit view.
- [Configuring Collision in RealityKit](configuring-collision-in-realitykit.md)
  Use collision groups and collision filters to control which objects collide.
- [struct CollisionComponent](collisioncomponent.md)
  A component that gives an entity the ability to collide with other entities that also have collision components.
- [CollisionComponent.Mode](collisioncomponent/mode-swift.enum.md)
  A mode that dictates how much collision data is collected for a given entity.
- [class ShapeResource](shaperesource.md)
  A representation of a shape.
- [enum ShapeResourceError](shaperesourceerror.md)
- [struct CollisionGroup](collisiongroup.md)
  A bitmask used to define the collision group to which an entity belongs.
- [struct CollisionFilter](collisionfilter.md)
  A set of masks that determine whether entities can collide during simulations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/triggervolume)*