# strides

**Framework**: Core AI  
**Kind**: property

The strides of the ndArray.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var strides: Span<Int> { get }
```

## See Also

- [var scalarType: NDArray.ScalarType](ndarray/mutablerawview/scalartype.md)
  The scalar type of the ndArray.
- [var shape: Span<Int>](ndarray/mutablerawview/shape.md)
  The shape of the ndArray.
- [var mutableBytes: MutableRawSpan](ndarray/mutablerawview/mutablebytes.md)
  A mutable span over the backing bytes of this tensor.
- [var interleaveLayout: NDArray.InterleaveLayout?](ndarray/mutablerawview/interleavelayout.md)
  Returns which dimension is interleaved, and by what factor it is interleaved. Or returns `nil` if there is not an interleaved dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutablerawview/strides)*