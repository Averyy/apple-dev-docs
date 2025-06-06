# CollisionComponent.Mode

**Framework**: RealityKit  
**Kind**: enum

A mode that dictates how much collision data is collected for a given entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
enum Mode
```

## Topics

### Collision modes
- [CollisionComponent.Mode.default](collisioncomponent/mode-swift.enum/default.md)
  A default collision object.
- [CollisionComponent.Mode.trigger](collisioncomponent/mode-swift.enum/trigger.md)
  A trigger collision object.
### Comparing collision modes
- [static func == (CollisionComponent.Mode, CollisionComponent.Mode) -> Bool](collisioncomponent/mode-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](collisioncomponent/mode-swift.enum/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func hash(into: inout Hasher)](collisioncomponent/mode-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](collisioncomponent/mode-swift.enum/hashvalue.md)
  The hash value.
### Enumeration Cases
- [CollisionComponent.Mode.colliding](collisioncomponent/mode-swift.enum/colliding.md)
  An environmental collision object.
### Default Implementations
- [Equatable Implementations](collisioncomponent/mode-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Simulating physics with collisions in your visionOS app](simulating-physics-with-collisions-in-your-visionos-app.md)
  Create entities that behave and react like physical objects in a RealityKit view.
- [Configuring Collision in RealityKit](configuring-collision-in-realitykit.md)
  Use collision groups and collision filters to control which objects collide.
- [struct CollisionComponent](collisioncomponent.md)
  A component that gives an entity the ability to collide with other entities that also have collision components.
- [class ShapeResource](shaperesource.md)
  A representation of a shape.
- [enum ShapeResourceError](shaperesourceerror.md)
- [struct CollisionGroup](collisiongroup.md)
  A bitmask used to define the collision group to which an entity belongs.
- [struct CollisionFilter](collisionfilter.md)
  A set of masks that determine whether entities can collide during simulations.
- [class TriggerVolume](triggervolume.md)
  An invisible 3D shape that detects when objects enter or exit a given region of space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisioncomponent/mode-swift.enum)*