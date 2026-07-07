# ClothBodyComponent.TargetShape

**Framework**: RealityKit  
**Kind**: struct

Pulls particles of a cloth body toward positions in either local or simulation space.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct TargetShape
```

## Topics

### Creating a target shape
- [init(for: ClothBodyComponent)](clothbodycomponent/targetshape/init(for:).md)
  Creates a target shape that is compatible with the given [`ClothBodyComponent`](clothbodycomponent.md).
### Constraining vertex positions
- [var constraints: PerClothVertexData<ClothBodyComponent.TargetShape.PositionConstraint>](clothbodycomponent/targetshape/constraints.md)
  The position constraints that pull the individual particles towards the target shape.
- [ClothBodyComponent.TargetShape.PositionConstraint](clothbodycomponent/targetshape/positionconstraint.md)
  A constraint that pulls a particle towards a certain position.
### Configuring the target shape
- [var weight: Float](clothbodycomponent/targetshape/weight.md)
  The weight by which the body will be pulled towards this target shape.
- [var space: ClothCoordinateSpace](clothbodycomponent/targetshape/space.md)
  The space in which the position constraints are defined.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var targetShapes: [ClothBodyComponent.TargetShape]](clothbodycomponent/targetshapes.md)
  The target shapes associated with the body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/targetshape)*