# scalarType

**Framework**: Core AI  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var scalarType: NDArray.ScalarType { get }
```

## See Also

### Inspecting the view
- [var shape: Span<Int>](./shape.md)
  The shape of the tensor.
- [var strides: Span<Int>](./strides.md)
  The strides of the tensor.
- [var bytes: RawSpan](./bytes.md)
  A span over the backing bytes of this tensor.
- [var interleaveLayout: NDArray.InterleaveLayout?](./interleavelayout.md)
  Returns which dimension is interleaved, and by what factor it is interleaved. Or returns `nil` if there is not an interleaved dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/rawview/scalartype)*