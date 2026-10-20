# type

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

The type of the shape constraint.

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
var type: MLMultiArrayShapeConstraintType { get }
```

```objc
@property (nonatomic, readonly) MLMultiArrayShapeConstraintType type;
```

## See Also

### Accessing the Constraints
- [var enumeratedShapes: [[NSNumber]]](./enumeratedshapes.md)
  Array of allowed shapes for a multiarray feature.
- [var sizeRangeForDimension: [NSValue]](./sizerangefordimension.md)
  The allowable range for a dimention of the multiarray.
- [enum MLMultiArrayShapeConstraintType](../mlmultiarrayshapeconstrainttype.md)
  The possible types of shape constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarrayshapeconstraint/type)*