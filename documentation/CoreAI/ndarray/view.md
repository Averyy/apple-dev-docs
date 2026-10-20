# NDArray.View

**Framework**: Core AI  
**Kind**: struct  
**Role**: Structure

An immutable non-owning view over the contents of a `NDArray`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct View<Element> where Element : BitwiseCopyable
```

## Mentions

- [Integrating on-device AI models in your app with Core AI](../integrating-on-device-ai-models-in-your-app-with-core-ai.md)

## Topics

### Creating a view
- [init(span: Span<Element>, shape: [Int], strides: [Int])](./view/init%28span,shape,strides%29.md)
  Initialize a view from a `Span`.
### Inspecting the view
- [var isContiguous: Bool](./view/iscontiguous.md)
  Returns `true` if the elements in this view have a row-major contiguous layout.
- [var rank: Int](./view/rank.md)
  The rank of the tensor.
- [var shape: Span<Int>](./view/shape.md)
  The shape of the tensor.
- [var strides: Span<Int>](./view/strides.md)
  The strides of the tensor.
- [var interleaveLayout: NDArray.InterleaveLayout?](./view/interleavelayout.md)
  Returns which dimension is interleaved, and by what factor it is interleaved. Or returns `nil` if there is not an interleaved dimension.
### Accessing elements
- [var contiguousElements: Span<Element>?](./view/contiguouselements.md)
  Returns a `Span` over the backing memory of this view if the memory is in a contiguous layout, otherwise returns `nil`.
- [subscript<let rank : Int>(scalarAt _: InlineArray<rank, Int>) -> Element](./view/subscript%28scalarat%29.md)
  Access the element at a multi-dimensional `index`.
### Accessing memory
- [func withUnsafePointer<R, E>((UnsafePointer<Element>, Span<Int>, Span<Int>) throws(E) -> R) throws(E) -> R](./view/withunsafepointer%28_%29.md)
  Invokes the provided closure with the backing data and memory layout of this view.
### Slicing the view
- [func slice(at: [any NDArray.RangeExpression]) -> NDArray.View<Element>](./view/slice%28at%29-32gsh.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.
- [func slice<let indexRank : Int>(at: [indexRank of any NDArray.RangeExpression]) -> NDArray.View<Element>](./view/slice%28at%29-4yomr.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.
### Converting to a raw view
- [var rawView: NDArray.RawView](./view/rawview.md)
  Returns a raw view over the same backing data

## See Also

### Accessing views
- [NDArray.MutableView](./mutableview.md)
  A mutable view over the storage of a tensor.
- [NDArray.RawView](./rawview.md)
  A type-erased immutable view over the memory owned by a tensor.
- [NDArray.MutableRawView](./mutablerawview.md)
  A type-erased mutable view over the memory owned by a tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/view)*