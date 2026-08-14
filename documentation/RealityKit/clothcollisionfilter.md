# ClothCollisionFilter

**Framework**: RealityKit  
**Kind**: struct

Defines the collision groups for a body or collider and the mask for one-way collisions.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ClothCollisionFilter
```

#### Overview

Collisions in cloth are one-way: an entity’s mask determines which groups it will push away, independently of whether the other entity pushes back. For a body particle to be displaced by a collider, the particle’s groups must overlap with the collider’s mask. For two body particles in a self-collision, each particle is independently displaced based on whether its groups overlap with the other particle’s mask.

## Topics

### Creating a collision filter
- [init(groups: ClothCollisionGroupSet, mask: ClothCollisionGroupSet)](clothcollisionfilter/init(groups:mask:).md)
  Creates a collision filter with the given groups and mask.
### Configuring collision groups
- [var groups: ClothCollisionGroupSet](clothcollisionfilter/groups.md)
  The set of collision groups, stored as a bit mask, to which the entity belongs.
- [var mask: ClothCollisionGroupSet](clothcollisionfilter/mask.md)
  The set of collision groups, stored as a bit mask, towards which the entity introduces one-way collisions.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct ClothColliderComponent](clothcollidercomponent.md)
  A component that adds a cloth-compatible collider to an entity.
- [enum ClothColliderShape](clothcollidershape.md)
  Shape suitable for use as a collider.
- [struct ClothColliderMaterial](clothcollidermaterial.md)
  A struct that represents a collider’s material.
- [struct ClothCollisionGroupSet](clothcollisiongroupset.md)
  `ClothCollisionGroupSet` is the basis for the `ClothCollisionFilter` and should not be used separately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothcollisionfilter)*