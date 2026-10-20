# ClothColliderEvents.NewBodyCollisions.Collision

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A collision with a cloth body.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Collision
```

## Topics

### Identifying the collider
- [let bodyEntity: Entity](./collision/bodyentity.md)
  The entity of the body that collided with the collider.
- [var bodyComponent: ClothBodyComponent?](./collision/bodycomponent.md)
  The [`ClothBodyComponent`](../../clothbodycomponent.md) of the colliding body, if still present on the entity.
### Accessing affected particles
- [func withParticleIndices<Result>((Span<UInt32>) -> Result) -> Result](./collision/withparticleindices%28_%29.md)
  Provides access to the indices of particles that collided with the collider.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Accessing collision data
- [func withCollisions<Result>((Span<ClothColliderEvents.NewBodyCollisions.Collision>) -> Result) -> Result](./withcollisions%28_%29.md)
  Provides access to the collisions with cloth bodies that took place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothcolliderevents/newbodycollisions/collision)*