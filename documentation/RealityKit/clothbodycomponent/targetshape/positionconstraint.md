# ClothBodyComponent.TargetShape.PositionConstraint

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A constraint that pulls a particle towards a certain position.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct PositionConstraint
```

## Topics

### Creating a constraint
- [init(position: SIMD3<Float>, stiffness: Float)](./positionconstraint/init%28position,stiffness%29.md)
  Creates a position constraint with the given target position and stiffness.
### Configuring the constraint
- [var stiffness: Float](./positionconstraint/stiffness.md)
  The stiffness by which the particle is pulled towards the position.
### Instance Properties
- [var position: SIMD3<Float>](./positionconstraint/position.md)
  The target position.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Constraining vertex positions
- [var constraints: PerClothVertexData<ClothBodyComponent.TargetShape.PositionConstraint>](./constraints.md)
  The position constraints that pull the individual particles towards the target shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/targetshape/positionconstraint)*