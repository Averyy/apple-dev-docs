# isContiguous

**Framework**: Core AI  
**Kind**: property

Returns `true` if the elements in this view have a row-major contiguous layout.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var isContiguous: Bool { get }
```

#### Discussion

> **Note**: If this returns `false`, then `contiguousElements` will return `nil`.

## See Also

- [var rank: Int](ndarray/view/rank.md)
  The rank of the tensor.
- [var shape: Span<Int>](ndarray/view/shape.md)
  The shape of the tensor.
- [var strides: Span<Int>](ndarray/view/strides.md)
  The strides of the tensor.
- [var interleaveLayout: NDArray.InterleaveLayout?](ndarray/view/interleavelayout.md)
  Returns which dimension is interleaved, and by what factor it is interleaved. Or returns `nil` if there is not an interleaved dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/view/iscontiguous)*