# NDArray.MutableView

**Framework**: Core AI  
**Kind**: struct  
**Role**: Structure

A mutable view over the storage of a tensor.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct MutableView<Element> where Element : BitwiseCopyable
```

## Mentions

- [Integrating on-device AI models in your app with Core AI](../integrating-on-device-ai-models-in-your-app-with-core-ai.md)

## Topics

### Creating a mutable view
- [init(mutableSpan: consuming MutableSpan<Element>, shape: [Int], strides: [Int])](./mutableview/init%28mutablespan,shape,strides%29.md)
  Initialize a view from a `MutableSpan`.
### Inspecting the view
- [var isContiguous: Bool](./mutableview/iscontiguous.md)
  Returns `true` if the elements in this view have a row-major contiguous layout.
- [var rank: Int](./mutableview/rank.md)
  The rank of the tensor.
- [var shape: Span<Int>](./mutableview/shape.md)
  The shape of the tensor.
- [var strides: Span<Int>](./mutableview/strides.md)
  The strides of the tensor.
- [var interleaveLayout: NDArray.InterleaveLayout?](./mutableview/interleavelayout.md)
  Returns which dimension is interleaved, and by what factor it is interleaved. Or returns `nil` if there is not an interleaved dimension.
### Accessing elements
- [var contiguousElements: MutableSpan<Element>?](./mutableview/contiguouselements.md)
  Returns a `MutableSpan` over the backing memory of this view if the memory is in a contiguous layout, otherwise returns `nil`.
- [subscript<let rank : Int>(scalarAt _: InlineArray<rank, Int>) -> Element](./mutableview/subscript%28scalarat%29.md)
  Access the element at a multi-dimensional `index`.
### Writing data
- [func copyElements(from: some Sequence<Element>)](./mutableview/copyelements%28from%29.md)
  Copies the elements from `sequence` into this view in row-major order.
- [func copyElements(fromContentsOf: some Collection<Element>)](./mutableview/copyelements%28fromcontentsof%29.md)
  Copies the elements from `collection` into this view in row-major order.
### Accessing memory
- [func withUnsafeMutablePointer<R, E>((UnsafeMutablePointer<Element>, Span<Int>, Span<Int>) throws(E) -> R) throws(E) -> R](./mutableview/withunsafemutablepointer%28_%29.md)
  Invokes the provided closure with the backing data and memory layout of this view.
### Slicing the view
- [func slice<let indexRank : Int>(at: [indexRank of any NDArray.RangeExpression]) -> NDArray.MutableView<Element>](./mutableview/slice%28at%29-50cpv.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.
- [func slice(at: [any NDArray.RangeExpression]) -> NDArray.MutableView<Element>](./mutableview/slice%28at%29-qyjq.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.
- [func mutatingSlice<let indexRank : Int>(at: [indexRank of any NDArray.RangeExpression]) -> NDArray.MutableView<Element>](./mutableview/mutatingslice%28at%29-30asd.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.
- [func mutatingSlice(at: [any NDArray.RangeExpression]) -> NDArray.MutableView<Element>](./mutableview/mutatingslice%28at%29-9pmi4.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.
### Converting to other views
- [var view: NDArray.View<Element>](./mutableview/view.md)
  An immutable view of this mutable view.
- [var mutableRawView: NDArray.MutableRawView](./mutableview/mutablerawview.md)
  Returns a mutable raw view over the same data.

## See Also

### Accessing views
- [NDArray.View](./view.md)
  An immutable non-owning view over the contents of a `NDArray`.
- [NDArray.RawView](./rawview.md)
  A type-erased immutable view over the memory owned by a tensor.
- [NDArray.MutableRawView](./mutablerawview.md)
  A type-erased mutable view over the memory owned by a tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutableview)*