# isContiguous

**Framework**: Core AI  
**Kind**: property  
**Role**: Instance Property

Returns `true` if the elements in this view have a row-major contiguous layout.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var isContiguous: Bool { get }
```

Available when `Element` conforms to `BitwiseCopyable`.

#### Discussion

> **Note**: If this returns `false`, then `contiguousElements` will return `nil`.

## See Also

### Inspecting the view
- [var rank: Int](./rank.md)
  The rank of the tensor.
- [var shape: Span<Int>](./shape.md)
  The shape of the tensor.
- [var strides: Span<Int>](./strides.md)
  The strides of the tensor.
- [var interleaveLayout: NDArray.InterleaveLayout?](./interleavelayout.md)
  Returns which dimension is interleaved, and by what factor it is interleaved. Or returns `nil` if there is not an interleaved dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/view/iscontiguous)*