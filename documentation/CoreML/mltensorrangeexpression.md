# MLTensorRangeExpression

**Framework**: Core ML  
**Kind**: protocol

A type that can be used to slice a dimension of a tensor. Don’t use this type directly.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol MLTensorRangeExpression : Sendable
```

## Topics

### Type Properties
- [static var fillAll: any MLTensorRangeExpression](mltensorrangeexpression/fillall.md)
  The same as the ellipsis literal `...` used to indicate unspecified dimensions of the tensor.
- [static var newAxis: any MLTensorRangeExpression](mltensorrangeexpression/newaxis.md)
  Expand the tensor at the specified dimension.
- [static var squeezeAxis: any MLTensorRangeExpression](mltensorrangeexpression/squeezeaxis.md)
  Squeeze the tensor at the specified dimension.
### Type Methods
- [static func closedRange(ClosedRange<Int>, stride: Int) -> any MLTensorRangeExpression](mltensorrangeexpression/closedrange(_:stride:).md)
  Slice the tensor at the specified dimension.
- [static func index(Int) -> any MLTensorRangeExpression](mltensorrangeexpression/index(_:).md)
  Slice the tensor at the specified dimension.
- [static func partialRangeFrom(PartialRangeFrom<Int>, stride: Int) -> any MLTensorRangeExpression](mltensorrangeexpression/partialrangefrom(_:stride:).md)
  Slice the tensor at the specified dimension.
- [static func partialRangeUpTo(PartialRangeUpTo<Int>, stride: Int) -> any MLTensorRangeExpression](mltensorrangeexpression/partialrangeupto(_:stride:)-4vz11.md)
  Slice the tensor at the specified dimension.
- [static func partialRangeUpTo(PartialRangeThrough<Int>, stride: Int) -> any MLTensorRangeExpression](mltensorrangeexpression/partialrangeupto(_:stride:)-5ccj1.md)
  Slice the tensor at the specified dimension.
- [static func range(Range<Int>, stride: Int) -> any MLTensorRangeExpression](mltensorrangeexpression/range(_:stride:).md)
  Slice the tensor at the specified dimension.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MLTensor](mltensor.md)
  A multi-dimensional array of numerical or Boolean scalars tailored to ML use cases, containing methods to perform transformations and mathematical operations efficiently using a ML compute device.
- [protocol MLTensorScalar](mltensorscalar.md)
  A type that represents the tensor scalar types supported by the framework. Don’t use this type directly.
- [func pointwiseMin(MLTensor, MLTensor) -> MLTensor](pointwisemin(_:_:).md)
  Computes the element-wise minimum of two tensors.
- [func pointwiseMax(MLTensor, MLTensor) -> MLTensor](pointwisemax(_:_:).md)
  Computes the element-wise maximum of two tensors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensorrangeexpression)*