# ClothColliderMaterial

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A struct that represents a collider’s material.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ClothColliderMaterial
```

## Topics

### Configuring friction
- [var kineticFriction: Float](./clothcollidermaterial/kineticfriction.md)
  The friction the collider applies to contacting cloth body particles with relative motion.
- [var staticFriction: Float](./clothcollidermaterial/staticfriction.md)
  The friction the collider applies to contacting cloth body particles with no relative motion.
### Initializers
- [init()](./clothcollidermaterial/init%28%29.md)
  Creates a new material for cloth colliders.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Collision
- [struct ClothColliderComponent](./clothcollidercomponent.md)
  A component that adds a cloth-compatible collider to an entity.
- [enum ClothColliderShape](./clothcollidershape.md)
  Shape suitable for use as a collider.
- [struct ClothCollisionFilter](./clothcollisionfilter.md)
  Defines the collision groups for a body or collider and the mask for one-way collisions.
- [struct ClothCollisionGroupSet](./clothcollisiongroupset.md)
  `ClothCollisionGroupSet` is the basis for the `ClothCollisionFilter` and should not be used separately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothcollidermaterial)*