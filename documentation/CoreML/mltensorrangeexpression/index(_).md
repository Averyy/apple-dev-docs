# index(_:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Type Method

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
static func index(_ index: Int) -> any MLTensorRangeExpression
```

Available when `Self` is `_MLTensorRange`.

#### Discussion

For example:

```swift
let x = MLTensor(randomNormal: [1, 3, 28, 28], scalarType: Float.self)
let y = x[..., 0] // or x[..., .index(0)]
y.shape // is [1, 3, 28]
```

## See Also

### Slicing the tensor
- [static func closedRange(ClosedRange<Int>, stride: Int) -> any MLTensorRangeExpression](./closedrange%28_,stride%29.md)
  Slice the tensor at the specified dimension.
- [static func partialRangeFrom(PartialRangeFrom<Int>, stride: Int) -> any MLTensorRangeExpression](./partialrangefrom%28_,stride%29.md)
  Slice the tensor at the specified dimension.
- [static partialRangeUpTo(_:stride:)](./partialrangeupto%28_,stride%29.md)
  Slice the tensor at the specified dimension.
- [static func range(Range<Int>, stride: Int) -> any MLTensorRangeExpression](./range%28_,stride%29.md)
  Slice the tensor at the specified dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensorrangeexpression/index(_:))*