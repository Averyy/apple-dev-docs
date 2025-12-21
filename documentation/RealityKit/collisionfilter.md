# CollisionFilter

**Framework**: RealityKit  
**Kind**: struct

A set of masks that determine whether entities can collide during simulations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
struct CollisionFilter
```

#### Overview

Use Collision filters in combination with collision groups to define which entities collide with which other entities in a scene. For more information on using collision filters, see [`CollisionGroup`](collisiongroup.md)

## Topics

### Creating a collision filter
- [init(group: CollisionGroup, mask: CollisionGroup)](collisionfilter/init(group:mask:).md)
  Creates a collision filter.
- [static let `default`: CollisionFilter](collisionfilter/default.md)
  The default collision filter.
- [static let sensor: CollisionFilter](collisionfilter/sensor.md)
  A collision filter for an entity that collides with everything.
### Customizing groups
- [var group: CollisionGroup](collisionfilter/group.md)
  The collision group or groups, stored as a bit mask, to which the entity belongs.
- [var mask: CollisionGroup](collisionfilter/mask.md)
  The collision group or groups, stored as a bitmask, with which the entity can collide.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

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
- [class TriggerVolume](triggervolume.md)
  An invisible 3D shape that detects when objects enter or exit a given region of space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisionfilter)*