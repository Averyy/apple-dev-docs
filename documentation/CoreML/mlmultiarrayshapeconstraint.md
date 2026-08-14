# MLMultiArrayShapeConstraint

**Framework**: Core ML  
**Kind**: class

The lists of shapes or ranges of shapes that constrain a multiarray feature.

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
class MLMultiArrayShapeConstraint
```

## Topics

### Accessing the Constraints
- [var enumeratedShapes: [[NSNumber]]](mlmultiarrayshapeconstraint/enumeratedshapes.md)
  Array of allowed shapes for a multiarray feature.
- [var sizeRangeForDimension: [NSValue]](mlmultiarrayshapeconstraint/sizerangefordimension.md)
  The allowable range for a dimention of the multiarray.
- [var type: MLMultiArrayShapeConstraintType](mlmultiarrayshapeconstraint/type.md)
  The type of the shape constraint.
- [enum MLMultiArrayShapeConstraintType](mlmultiarrayshapeconstrainttype.md)
  The possible types of shape constraints.
### Initializers
- [init?(coder: NSCoder)](mlmultiarrayshapeconstraint/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [var shape: [NSNumber]](mlmultiarrayconstraint/shape.md)
  The shape of the multi array.
- [var dataType: MLMultiArrayDataType](mlmultiarrayconstraint/datatype.md)
  The type for the multi array.
- [var shapeConstraint: MLMultiArrayShapeConstraint](mlmultiarrayconstraint/shapeconstraint.md)
  The constraint on the shape of the multiarray.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarrayshapeconstraint)*