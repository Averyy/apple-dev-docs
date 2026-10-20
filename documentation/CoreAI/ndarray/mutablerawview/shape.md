# shape

**Framework**: Core AI  
**Kind**: property  
**Role**: Instance Property

The shape of the ndArray.

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

### Inspecting the view
- [var scalarType: NDArray.ScalarType](./scalartype.md)
  The scalar type of the ndArray.
- [var strides: Span<Int>](./strides.md)
  The strides of the ndArray.
- [var mutableBytes: MutableRawSpan](./mutablebytes.md)
  A mutable span over the backing bytes of this tensor.
- [var interleaveLayout: NDArray.InterleaveLayout?](./interleavelayout.md)
  Returns which dimension is interleaved, and by what factor it is interleaved. Or returns `nil` if there is not an interleaved dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutablerawview/shape)*