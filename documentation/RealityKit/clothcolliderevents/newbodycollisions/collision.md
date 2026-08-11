# ClothColliderEvents.NewBodyCollisions.Collision

**Framework**: RealityKit  
**Kind**: struct

A collision with a cloth body.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Collision
```

## Topics

### Identifying the collider
- [let bodyEntity: Entity](clothcolliderevents/newbodycollisions/collision/bodyentity.md)
  The entity of the body that collided with the collider.
- [var bodyComponent: ClothBodyComponent?](clothcolliderevents/newbodycollisions/collision/bodycomponent.md)
  The [`ClothBodyComponent`](clothbodycomponent.md) of the colliding body, if still present on the entity.
### Accessing affected particles
- [func withParticleIndices<Result>((Span<UInt32>) -> Result) -> Result](clothcolliderevents/newbodycollisions/collision/withparticleindices(_:).md)
  Provides access to the indices of particles that collided with the collider.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func withCollisions<Result>((Span<ClothColliderEvents.NewBodyCollisions.Collision>) -> Result) -> Result](clothcolliderevents/newbodycollisions/withcollisions(_:).md)
  Provides access to the collisions with cloth bodies that took place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothcolliderevents/newbodycollisions/collision)*