# strides

**Framework**: Core AI  
**Kind**: property  
**Role**: Instance Property

The strides of the tensor.

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

### Inspecting the view
- [var scalarType: NDArray.ScalarType](./scalartype.md)
- [var shape: Span<Int>](./shape.md)
  The shape of the tensor.
- [var bytes: RawSpan](./bytes.md)
  A span over the backing bytes of this tensor.
- [var interleaveLayout: NDArray.InterleaveLayout?](./interleavelayout.md)
  Returns which dimension is interleaved, and by what factor it is interleaved. Or returns `nil` if there is not an interleaved dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/rawview/strides)*