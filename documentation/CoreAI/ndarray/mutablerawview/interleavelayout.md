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

- [var scalarType: NDArray.ScalarType](ndarray/mutablerawview/scalartype.md)
  The scalar type of the ndArray.
- [var shape: Span<Int>](ndarray/mutablerawview/shape.md)
  The shape of the ndArray.
- [var strides: Span<Int>](ndarray/mutablerawview/strides.md)
  The strides of the ndArray.
- [var mutableBytes: MutableRawSpan](ndarray/mutablerawview/mutablebytes.md)
  A mutable span over the backing bytes of this tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutablerawview/interleavelayout)*