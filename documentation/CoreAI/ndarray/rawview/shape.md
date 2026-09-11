# shape

**Framework**: Core AI  
**Kind**: property

The shape of the tensor.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var shape: Span<Int> { get }
```

## See Also

- [var scalarType: NDArray.ScalarType](ndarray/rawview/scalartype.md)
- [var strides: Span<Int>](ndarray/rawview/strides.md)
  The strides of the tensor.
- [var bytes: RawSpan](ndarray/rawview/bytes.md)
  A span over the backing bytes of this tensor.
- [var interleaveLayout: NDArray.InterleaveLayout?](ndarray/rawview/interleavelayout.md)
  Returns which dimension is interleaved, and by what factor it is interleaved. Or returns `nil` if there is not an interleaved dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/rawview/shape)*