# rank

**Framework**: Core AI  
**Kind**: property

The rank of the tensor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var rank: Int { get }
```

#### Discussion

Equivalent to `shape.count`.

## See Also

- [var isContiguous: Bool](ndarray/mutableview/iscontiguous.md)
  Returns `true` if the elements in this view have a row-major contiguous layout.
- [var shape: Span<Int>](ndarray/mutableview/shape.md)
  The shape of the tensor.
- [var strides: Span<Int>](ndarray/mutableview/strides.md)
  The strides of the tensor.
- [var interleaveLayout: NDArray.InterleaveLayout?](ndarray/mutableview/interleavelayout.md)
  Returns which dimension is interleaved, and by what factor it is interleaved. Or returns `nil` if there is not an interleaved dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutableview/rank)*