# interleaveLayout

**Framework**: Core AI  
**Kind**: property

Returns which dimension is interleaved, and by what factor it is interleaved. Or returns `nil` if there is not an interleaved dimension.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var interleaveLayout: NDArray.InterleaveLayout? { get }
```

#### Discussion

See [`NDArray.InterleaveLayout`](ndarray/interleavelayout-swift.struct.md) for full documentation.

## See Also

- [var isContiguous: Bool](ndarray/mutableview/iscontiguous.md)
  Returns `true` if the elements in this view have a row-major contiguous layout.
- [var rank: Int](ndarray/mutableview/rank.md)
  The rank of the tensor.
- [var shape: Span<Int>](ndarray/mutableview/shape.md)
  The shape of the tensor.
- [var strides: Span<Int>](ndarray/mutableview/strides.md)
  The strides of the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutableview/interleavelayout)*