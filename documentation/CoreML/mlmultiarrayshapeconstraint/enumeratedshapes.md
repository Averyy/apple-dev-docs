# enumeratedShapes

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

Array of allowed shapes for a multiarray feature.

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
var enumeratedShapes: [[NSNumber]] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSArray<NSNumber *> *> * enumeratedShapes;
```

## See Also

### Accessing the Constraints
- [var sizeRangeForDimension: [NSValue]](./sizerangefordimension.md)
  The allowable range for a dimention of the multiarray.
- [var type: MLMultiArrayShapeConstraintType](./type.md)
  The type of the shape constraint.
- [enum MLMultiArrayShapeConstraintType](../mlmultiarrayshapeconstrainttype.md)
  The possible types of shape constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarrayshapeconstraint/enumeratedshapes)*