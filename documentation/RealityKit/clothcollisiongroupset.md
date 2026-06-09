# ClothCollisionGroupSet

**Framework**: RealityKit  
**Kind**: struct

`ClothCollisionGroupSet` is the basis for the `ClothCollisionFilter` and should not be used separately.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ClothCollisionGroupSet
```

## Topics

### Creating a group set
- [init(groups: [Int])](clothcollisiongroupset/init(groups:).md)
  Creates a collision group set from an array of numbered groups.
### Accessing default groups
- [static let defaultBodies: ClothCollisionGroupSet](clothcollisiongroupset/defaultbodies.md)
  Default option reserved for cloth bodies.
- [static let defaultColliders: ClothCollisionGroupSet](clothcollisiongroupset/defaultcolliders.md)
  Default option reserved for colliders.
### Initializers
- [init(rawValue: UInt32)](clothcollisiongroupset/init(rawvalue:).md)
  Creates a collision group set from a raw bitmask value.
### Instance Properties
- [var rawValue: UInt32](clothcollisiongroupset/rawvalue.md)
  The raw bitmask value of the set, where each set bit represents a group between 1 and 32.
### Type Properties
- [static let all: ClothCollisionGroupSet](clothcollisiongroupset/all.md)
  Option that includes all groups.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct ClothColliderComponent](clothcollidercomponent.md)
  A component that adds a cloth-compatible collider to an entity.
- [enum ClothColliderShape](clothcollidershape.md)
  Shape suitable for use as a collider.
- [struct ClothColliderMaterial](clothcollidermaterial.md)
  A struct that represents a collider’s material.
- [struct ClothCollisionFilter](clothcollisionfilter.md)
  Defines the collision groups for a body or collider and the mask for one-way collisions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothcollisiongroupset)*