# ClothBodyComponent.TargetShape

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Pulls particles of a cloth body toward positions in either local or simulation space.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct TargetShape
```

## Topics

### Creating a target shape
- [init(for: ClothBodyComponent)](./targetshape/init%28for%29.md)
  Creates a target shape that is compatible with the given [`ClothBodyComponent`](../clothbodycomponent.md).
### Constraining vertex positions
- [var constraints: PerClothVertexData<ClothBodyComponent.TargetShape.PositionConstraint>](./targetshape/constraints.md)
  The position constraints that pull the individual particles towards the target shape.
- [ClothBodyComponent.TargetShape.PositionConstraint](./targetshape/positionconstraint.md)
  A constraint that pulls a particle towards a certain position.
### Configuring the target shape
- [var weight: Float](./targetshape/weight.md)
  The weight by which the body will be pulled towards this target shape.
- [var space: ClothCoordinateSpace](./targetshape/space.md)
  The space in which the position constraints are defined.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Defining target shapes
- [var targetShapes: [ClothBodyComponent.TargetShape]](./targetshapes.md)
  The target shapes associated with the body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/targetshape)*