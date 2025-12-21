# partialRangeUpTo(_:stride:)

**Framework**: Core ML  
**Kind**: method

Slice the tensor at the specified dimension.

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
static func partialRangeUpTo(_ range: PartialRangeThrough<Int>, stride: Int = 1) -> any MLTensorRangeExpression
```

#### Discussion

For example:

```swift
let x = MLTensor(randomNormal: [1, 3, 28, 28], scalarType: Float.self)
let y = x[..., ...3] // or x[..., .partialRangeThrough(...3, stride: 1)]
y.shape // is [1, 3, 28, 4]
```

## See Also

- [static func closedRange(ClosedRange<Int>, stride: Int) -> any MLTensorRangeExpression](mltensorrangeexpression/closedrange(_:stride:).md)
  Slice the tensor at the specified dimension.
- [static func index(Int) -> any MLTensorRangeExpression](mltensorrangeexpression/index(_:).md)
  Slice the tensor at the specified dimension.
- [static func partialRangeFrom(PartialRangeFrom<Int>, stride: Int) -> any MLTensorRangeExpression](mltensorrangeexpression/partialrangefrom(_:stride:).md)
  Slice the tensor at the specified dimension.
- [static func range(Range<Int>, stride: Int) -> any MLTensorRangeExpression](mltensorrangeexpression/range(_:stride:).md)
  Slice the tensor at the specified dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensorrangeexpression/partialrangeupto(_:stride:))*