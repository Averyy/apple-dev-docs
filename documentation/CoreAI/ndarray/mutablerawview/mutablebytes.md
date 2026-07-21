# mutableBytes

**Framework**: Core AI  
**Kind**: property

A mutable span over the backing bytes of this tensor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@export(implementation)
var mutableBytes: MutableRawSpan { get }
```

#### Discussion

> **Note**: When accessing the bytes directly you are responsible for interpreting the layout of the tensor according to the `strides` property of this view. This means you must either ensure the logical elements are contiguous, or dynamically handle nontrivial striding. If the view has an [`interleaveLayout`](ndarray/mutablerawview/interleavelayout.md), the strides for that dimension are block strides and must be interpreted accordingly — see [`NDArray.InterleaveLayout`](ndarray/interleavelayout-swift.struct.md).

## See Also

- [var scalarType: NDArray.ScalarType](ndarray/mutablerawview/scalartype.md)
  The scalar type of the ndArray.
- [var shape: Span<Int>](ndarray/mutablerawview/shape.md)
  The shape of the ndArray.
- [var strides: Span<Int>](ndarray/mutablerawview/strides.md)
  The strides of the ndArray.
- [var interleaveLayout: NDArray.InterleaveLayout?](ndarray/mutablerawview/interleavelayout.md)
  Returns which dimension is interleaved, and by what factor it is interleaved. Or returns `nil` if there is not an interleaved dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutablerawview/mutablebytes)*