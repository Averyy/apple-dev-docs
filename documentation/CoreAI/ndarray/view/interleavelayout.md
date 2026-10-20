# interleaveLayout

**Framework**: Core AI  
**Kind**: property  
**Role**: Instance Property

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

Available when `Element` conforms to `BitwiseCopyable`.

#### Discussion

See [`NDArray.InterleaveLayout`](../interleavelayout-swift.struct.md) for full documentation.

## See Also

### Inspecting the view
- [var isContiguous: Bool](./iscontiguous.md)
  Returns `true` if the elements in this view have a row-major contiguous layout.
- [var rank: Int](./rank.md)
  The rank of the tensor.
- [var shape: Span<Int>](./shape.md)
  The shape of the tensor.
- [var strides: Span<Int>](./strides.md)
  The strides of the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/view/interleavelayout)*