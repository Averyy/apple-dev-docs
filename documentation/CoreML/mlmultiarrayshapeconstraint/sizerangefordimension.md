# sizeRangeForDimension

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

The allowable range for a dimention of the multiarray.

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
var sizeRangeForDimension: [NSValue] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSValue *> * sizeRangeForDimension;
```

## See Also

### Accessing the Constraints
- [var enumeratedShapes: [[NSNumber]]](./enumeratedshapes.md)
  Array of allowed shapes for a multiarray feature.
- [var type: MLMultiArrayShapeConstraintType](./type.md)
  The type of the shape constraint.
- [enum MLMultiArrayShapeConstraintType](../mlmultiarrayshapeconstrainttype.md)
  The possible types of shape constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarrayshapeconstraint/sizerangefordimension)*