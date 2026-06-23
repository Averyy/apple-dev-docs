# OutputSpan

**Framework**: Swift  
**Kind**: struct

`OutputSpan` is a reference to a contiguous region of memory that starts with some number of initialized `Element` instances followed by uninitialized memory. It provides operations to access the items it stores, as well as to add new elements and to remove existing ones.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
@frozen
struct OutputSpan<Element> where Element : ~Copyable
```

## Topics

### Initializers
- [init()](outputspan/init.md)
  Create an OutputSpan with zero capacity.
- [init(buffer: UnsafeMutableBufferPointer<Element>, initializedCount: Int)](outputspan/init(buffer:initializedcount:)-3tbg3.md)
  Unsafely create an OutputSpan over partly-initialized memory.
- [init(buffer: borrowing Slice<UnsafeMutableBufferPointer<Element>>, initializedCount: Int)](outputspan/init(buffer:initializedcount:)-vie3.md)
  Unsafely create an OutputSpan over partly-initialized memory.
### Instance Properties
- [let capacity: Int](outputspan/capacity.md)
  The total number of elements that this output span can contain.
- [var count: Int](outputspan/count.md)
  The number of initialized elements in this span.
- [var freeCapacity: Int](outputspan/freecapacity.md)
  The number of additional elements that can be added to this span.
- [var indices: Range<OutputSpan<Element>.Index>](outputspan/indices.md)
  The range of initialized indices for this `OutputSpan`.
- [var isEmpty: Bool](outputspan/isempty.md)
  A Boolean value indicating whether the span is empty.
- [var isFull: Bool](outputspan/isfull.md)
  A Boolean value indicating whether the span is full.
- [var mutableSpan: MutableSpan<Element>](outputspan/mutablespan.md)
  Exclusively borrow the underlying initialized memory for mutation.
- [var span: Span<Element>](outputspan/span.md)
  Borrow the underlying initialized memory for read-only access.
### Instance Methods
- [func append(consuming Element)](outputspan/append(_:).md)
  Append a single element to this span.
- [func append(repeating: Element, count: Int)](outputspan/append(repeating:count:).md)
  Repeatedly append an element to this span.
- [func finalize(for: Slice<UnsafeMutableBufferPointer<Element>>) -> Int](outputspan/finalize(for:)-5utkq.md)
  Consume the output span and return the number of initialized elements.
- [func finalize(for: UnsafeMutableBufferPointer<Element>) -> Int](outputspan/finalize(for:)-83pw0.md)
  Consume the output span and return the number of initialized elements.
- [func removeAll()](outputspan/removeall.md)
  Remove all this span’s elements and return its memory to the uninitialized state.
- [func removeLast() -> Element](outputspan/removelast.md)
  Remove the last initialized element from this span.
- [func removeLast(Int)](outputspan/removelast(_:).md)
  Remove the last n elements of this span, returning the memory they occupy to the uninitialized state.
- [func swapAt(OutputSpan<Element>.Index, OutputSpan<Element>.Index)](outputspan/swapat(_:_:).md)
  Exchange the elements at the two given indices.
- [func swapAt(unchecked: OutputSpan<Element>.Index, unchecked: OutputSpan<Element>.Index)](outputspan/swapat(unchecked:unchecked:).md)
  Exchange the elements at the two given indices.
- [func withBytes<R, E>((RawSpan) throws(E) -> R) throws(E) -> R](outputspan/withbytes(_:).md)
- [func withUnsafeMutableBufferPointer<E, R>((UnsafeMutableBufferPointer<Element>, inout Int) throws(E) -> R) throws(E) -> R](outputspan/withunsafemutablebufferpointer(_:).md)
  Call the given closure with the unsafe buffer pointer addressed by this OutputSpan and a mutable reference to its count of initialized elements.
### Subscripts
- [subscript(OutputSpan<Element>.Index) -> Element](outputspan/subscript(_:).md)
  Accesses the element at the specified index.
- [subscript(unchecked _: OutputSpan<Element>.Index) -> Element](outputspan/subscript(unchecked:).md)
  Accesses the element at the specified index.
### Type Aliases
- [OutputSpan.Index](outputspan/index.md)
  The type that represents an initialized index in an `OutputSpan`.

## Relationships

### Conforms To
- [ContiguousBytes](../Foundation/ContiguousBytes.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [struct Span](span.md)
  `Span<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [struct RawSpan](rawspan.md)
  `RawSpan` represents a contiguous region of memory which contains initialized bytes.
- [struct OutputRawSpan](outputrawspan.md)
  `OutputRawSpan` is a reference to a contiguous region of memory which starts with some number of initialized bytes, followed by uninitialized memory. It provides operations to access the bytes it stores, as well as to append and to remove bytes.
- [struct UTF8Span](utf8span.md)
  A borrowed view into contiguous memory that contains validly-encoded UTF-8 code units.
- [struct MutableSpan](mutablespan.md)
  `MutableSpan<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [struct MutableRawSpan](mutablerawspan.md)
  `MutableRawSpan` represents a contiguous region of memory which contains initialized bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/outputspan)*