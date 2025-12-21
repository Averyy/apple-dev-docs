# MLMultiArrayShapeConstraintType

**Framework**: Core ML  
**Kind**: enum

The possible types of shape constraints.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
enum MLMultiArrayShapeConstraintType
```

## Topics

### Constraint types
- [MLMultiArrayShapeConstraintType.enumerated](mlmultiarrayshapeconstrainttype/enumerated.md)
  The constraint is an array of allowed shapes.
- [MLMultiArrayShapeConstraintType.range](mlmultiarrayshapeconstrainttype/range.md)
  The constraint is a set of ranges allowed for the array shape.
- [MLMultiArrayShapeConstraintType.unspecified](mlmultiarrayshapeconstrainttype/unspecified.md)
  The constraint type is undefined.
### Creating a constraint type
- [init?(rawValue: Int)](mlmultiarrayshapeconstrainttype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var enumeratedShapes: [[NSNumber]]](mlmultiarrayshapeconstraint/enumeratedshapes.md)
  Array of allowed shapes for a multiarray feature.
- [var sizeRangeForDimension: [NSValue]](mlmultiarrayshapeconstraint/sizerangefordimension.md)
  The allowable range for a dimention of the multiarray.
- [var type: MLMultiArrayShapeConstraintType](mlmultiarrayshapeconstraint/type.md)
  The type of the shape constraint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarrayshapeconstrainttype)*