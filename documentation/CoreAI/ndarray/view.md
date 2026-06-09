# NDArray.View

**Framework**: Core AI  
**Kind**: struct

An immutable non-owning view over the contents of a `NDArray`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct View<Element> where Element : BitwiseCopyable
```

## Mentions

- [Integrating on-device AI models in your app with Core AI](integrating-on-device-ai-models-in-your-app-with-core-ai.md)

## Topics

### Creating a view
- [init(span: Span<Element>, shape: [Int], strides: [Int])](ndarray/view/init(span:shape:strides:).md)
  Initialize a view from a `Span`.
### Inspecting the view
- [var isContiguous: Bool](ndarray/view/iscontiguous.md)
  Returns `true` if the elements in this view have a row-major contiguous layout.
- [var rank: Int](ndarray/view/rank.md)
  The rank of the tensor.
- [var shape: Span<Int>](ndarray/view/shape.md)
  The shape of the tensor.
- [var strides: Span<Int>](ndarray/view/strides.md)
  The strides of the tensor.
### Accessing elements
- [var contiguousElements: Span<Element>?](ndarray/view/contiguouselements.md)
  Returns a `Span` over the backing memory of this view if the memory is in a contiguous layout, otherwise returns `nil`.
### Accessing memory
- [func withUnsafePointer<R, E>((UnsafePointer<Element>, Span<Int>, Span<Int>) throws(E) -> R) throws(E) -> R](ndarray/view/withunsafepointer(_:).md)
  Invokes the provided closure with the backing data and memory layout of this view.
### Instance Properties
- [var interleaveLayout: NDArray.InterleaveLayout?](ndarray/view/interleavelayout.md)
  Returns which dimension is interleaved, and by what factor it is interleaved. Or returns `nil` if there is not an interleaved dimension.
- [var rawView: NDArray.RawView](ndarray/view/rawview.md)
  Returns a raw view over the same backing data
### Instance Methods
- [func slice(at: [any NDArray.RangeExpression]) -> NDArray.View<Element>](ndarray/view/slice(at:)-32gsh.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.
- [func slice<let indexRank : Int>(at: [indexRank of any NDArray.RangeExpression]) -> NDArray.View<Element>](ndarray/view/slice(at:)-4yomr.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.

## See Also

- [NDArray.MutableView](ndarray/mutableview.md)
  A mutable view over the storage of a tensor.
- [NDArray.RawView](ndarray/rawview.md)
  A type-erased immutable view over the memory owned by a tensor.
- [NDArray.MutableRawView](ndarray/mutablerawview.md)
  A type-erased mutable view over the memory owned by a tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/view)*