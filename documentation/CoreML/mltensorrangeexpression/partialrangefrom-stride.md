# partialRangeFrom(_:stride:)

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
static func partialRangeFrom(_ range: PartialRangeFrom<Int>, stride: Int = 1) -> any MLTensorRangeExpression
```

#### Discussion

For example:

```swift
let x = MLTensor(randomNormal: [1, 3, 28, 28], scalarType: Float.self)
let y = x[..., 1...] // or x[..., .partialRangeFrom(1..., stride: 1)]
y.shape // is [1, 3, 28, 27]
```

## See Also

- [static func closedRange(ClosedRange<Int>, stride: Int) -> any MLTensorRangeExpression](mltensorrangeexpression/closedrange(_:stride:).md)
  Slice the tensor at the specified dimension.
- [static func index(Int) -> any MLTensorRangeExpression](mltensorrangeexpression/index(_:).md)
  Slice the tensor at the specified dimension.
- [static partialRangeUpTo(_:stride:)](mltensorrangeexpression/partialrangeupto(_:stride:).md)
  Slice the tensor at the specified dimension.
- [static func range(Range<Int>, stride: Int) -> any MLTensorRangeExpression](mltensorrangeexpression/range(_:stride:).md)
  Slice the tensor at the specified dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensorrangeexpression/partialrangefrom(_:stride:))*