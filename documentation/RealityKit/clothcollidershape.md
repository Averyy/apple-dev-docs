# ClothColliderShape

**Framework**: RealityKit  
**Kind**: enum

Shape suitable for use as a collider.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum ClothColliderShape
```

## Topics

### Specifying the collider shape
- [ClothColliderShape.box(_:)](clothcollidershape/box(_:).md)
  A box collider shape.
- [case roundedBox(ClothRoundedBoxShape)](clothcollidershape/roundedbox(_:).md)
  A rounded box collider shape.
- [ClothColliderShape.sphere(_:)](clothcollidershape/sphere(_:).md)
  A sphere collider shape.
- [case capsule(ClothCapsuleShape)](clothcollidershape/capsule(_:).md)
  A capsule collider shape.
- [ClothColliderShape.plane(_:)](clothcollidershape/plane(_:).md)
  A plane collider shape.
- [ClothColliderShape.mesh(_:)](clothcollidershape/mesh(_:).md)
  A mesh collider shape.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct ClothColliderComponent](clothcollidercomponent.md)
  A component that adds a cloth-compatible collider to an entity.
- [struct ClothColliderMaterial](clothcollidermaterial.md)
  A struct that represents a collider’s material.
- [struct ClothCollisionFilter](clothcollisionfilter.md)
  Defines the collision groups for a body or collider and the mask for one-way collisions.
- [struct ClothCollisionGroupSet](clothcollisiongroupset.md)
  `ClothCollisionGroupSet` is the basis for the `ClothCollisionFilter` and should not be used separately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothcollidershape)*