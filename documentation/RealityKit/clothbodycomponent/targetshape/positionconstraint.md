# ClothBodyComponent.TargetShape.PositionConstraint

**Framework**: RealityKit  
**Kind**: struct

A constraint that pulls a particle towards a certain position.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct PositionConstraint
```

## Topics

### Creating a constraint
- [init(position: SIMD3<Float>, stiffness: Float)](clothbodycomponent/targetshape/positionconstraint/init(position:stiffness:).md)
  Creates a position constraint with the given target position and stiffness.
### Configuring the constraint
- [var stiffness: Float](clothbodycomponent/targetshape/positionconstraint/stiffness.md)
  The stiffness by which the particle is pulled towards the position.
### Instance Properties
- [var position: SIMD3<Float>](clothbodycomponent/targetshape/positionconstraint/position.md)
  The target position.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var constraints: PerClothVertexData<ClothBodyComponent.TargetShape.PositionConstraint>](clothbodycomponent/targetshape/constraints.md)
  The position constraints that pull the individual particles towards the target shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/targetshape/positionconstraint)*