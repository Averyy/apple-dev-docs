# ClothColliderShape

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

Shape suitable for use as a collider.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum ClothColliderShape
```

## Topics

### Specifying the collider shape
- [ClothColliderShape.box(_:)](./clothcollidershape/box%28_%29.md)
  A box collider shape.
- [case roundedBox(ClothRoundedBoxShape)](./clothcollidershape/roundedbox%28_%29.md)
  A rounded box collider shape.
- [ClothColliderShape.sphere(_:)](./clothcollidershape/sphere%28_%29.md)
  A sphere collider shape.
- [case capsule(ClothCapsuleShape)](./clothcollidershape/capsule%28_%29.md)
  A capsule collider shape.
- [ClothColliderShape.plane(_:)](./clothcollidershape/plane%28_%29.md)
  A plane collider shape.
- [ClothColliderShape.mesh(_:)](./clothcollidershape/mesh%28_%29.md)
  A mesh collider shape.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Collision
- [struct ClothColliderComponent](./clothcollidercomponent.md)
  A component that adds a cloth-compatible collider to an entity.
- [struct ClothColliderMaterial](./clothcollidermaterial.md)
  A struct that represents a collider’s material.
- [struct ClothCollisionFilter](./clothcollisionfilter.md)
  Defines the collision groups for a body or collider and the mask for one-way collisions.
- [struct ClothCollisionGroupSet](./clothcollisiongroupset.md)
  `ClothCollisionGroupSet` is the basis for the `ClothCollisionFilter` and should not be used separately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothcollidershape)*