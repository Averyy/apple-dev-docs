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

- [var scalarType: NDArray.ScalarType](ndarray/rawview/scalartype.md)
- [var shape: Span<Int>](ndarray/rawview/shape.md)
  The shape of the tensor.
- [var strides: Span<Int>](ndarray/rawview/strides.md)
  The strides of the tensor.
- [var bytes: RawSpan](ndarray/rawview/bytes.md)
  A span over the backing bytes of this tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/rawview/interleavelayout)*