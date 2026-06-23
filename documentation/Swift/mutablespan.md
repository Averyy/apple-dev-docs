# MutableSpan

**Framework**: Swift  
**Kind**: struct

`MutableSpan<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.

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
struct MutableSpan<Element> where Element : ~Copyable
```

## Topics

### Initializers
- [init()](mutablespan/init.md)
  Create an empty span.
- [init(mutableBytes: consuming MutableRawSpan)](mutablespan/init(mutablebytes:).md)
  Convert a raw span to a typed span.
- [init(mutating: inout MutableRawSpan)](mutablespan/init(mutating:).md)
  Mutate untyped memory as a typed span.
### Instance Properties
- [var bytes: RawSpan](mutablespan/bytes-478ye.md)
  A raw span over the memory represented by this span.
- [var bytes: RawSpan](mutablespan/bytes-61tq.md)
  Construct a raw span over the memory represented by this span.
- [var count: Int](mutablespan/count.md)
  The number of elements in the span.
- [var indices: Range<MutableSpan<Element>.Index>](mutablespan/indices.md)
  The range of valid indices for subscripting the span.
- [var isEmpty: Bool](mutablespan/isempty.md)
  A Boolean value indicating whether the span is empty.
- [var mutableBytes: MutableRawSpan](mutablespan/mutablebytes-7cwoq.md)
  Construct a mutable raw span over the memory represented by this span.
- [var mutableBytes: MutableRawSpan](mutablespan/mutablebytes-9ha97.md)
  A mutable raw span over the memory represented by this span.
- [var span: Span<Element>](mutablespan/span.md)
  Borrow the underlying initialized memory for read-only access.
### Instance Methods
- [func extracting(some RangeExpression<Int>) -> MutableSpan<Element>](mutablespan/extracting(_:)-2g8w3.md)
  Constructs a new span over the items within the supplied range of indices within this span.
- [func extracting(UnboundedRange) -> MutableSpan<Element>](mutablespan/extracting(_:)-80srp.md)
  Constructs a new span over all the items of this span.
- [func extracting(Range<MutableSpan<Element>.Index>) -> MutableSpan<Element>](mutablespan/extracting(_:)-bphj.md)
  Constructs a new span over the items within the supplied range of indices within this span.
- [func extracting(droppingFirst: Int) -> MutableSpan<Element>](mutablespan/extracting(droppingfirst:).md)
  Returns a span over all but the given number of initial elements.
- [func extracting(droppingLast: Int) -> MutableSpan<Element>](mutablespan/extracting(droppinglast:).md)
  Returns a span over all but the given number of trailing elements.
- [func extracting(first: Int) -> MutableSpan<Element>](mutablespan/extracting(first:).md)
  Returns a span containing the initial elements of this span, up to the specified maximum length.
- [func extracting(last: Int) -> MutableSpan<Element>](mutablespan/extracting(last:).md)
  Returns a span containing the trailing elements of the span, up to the given maximum length.
- [func extracting(unchecked: Range<MutableSpan<Element>.Index>) -> MutableSpan<Element>](mutablespan/extracting(unchecked:)-23qq.md)
  Constructs a new span over the items within the supplied range of indices within this span.
- [func extracting(unchecked: ClosedRange<MutableSpan<Element>.Index>) -> MutableSpan<Element>](mutablespan/extracting(unchecked:)-4y8oj.md)
  Constructs a new span over the items within the supplied range of indices within this span.
- [func swapAt(MutableSpan<Element>.Index, MutableSpan<Element>.Index)](mutablespan/swapat(_:_:).md)
  Exchange the elements at the two given indices.
- [func swapAt(unchecked: MutableSpan<Element>.Index, unchecked: MutableSpan<Element>.Index)](mutablespan/swapat(unchecked:unchecked:).md)
  Exchange the elements at the two given indices.
- [func update(repeating: consuming Element)](mutablespan/update(repeating:).md)
  Update every element of this span to the given value.
- [func withBytes<R, E>((RawSpan) throws(E) -> R) throws(E) -> R](mutablespan/withbytes(_:).md)
- [func withUnsafeBufferPointer<E, Result>((UnsafeBufferPointer<Element>) throws(E) -> Result) throws(E) -> Result](mutablespan/withunsafebufferpointer(_:).md)
  Call a closure with a pointer to the viewed contiguous storage.
- [func withUnsafeBytes<E, Result>((UnsafeRawBufferPointer) throws(E) -> Result) throws(E) -> Result](mutablespan/withunsafebytes(_:).md)
  Calls the given closure with a pointer to the underlying bytes of the viewed contiguous storage.
- [func withUnsafeMutableBufferPointer<E, Result>((UnsafeMutableBufferPointer<Element>) throws(E) -> Result) throws(E) -> Result](mutablespan/withunsafemutablebufferpointer(_:).md)
  Call a closure with a pointer to the viewed mutable contiguous storage.
- [func withUnsafeMutableBytes<E, Result>((UnsafeMutableRawBufferPointer) throws(E) -> Result) throws(E) -> Result](mutablespan/withunsafemutablebytes(_:).md)
  Calls the given closure with a mutable pointer to the underlying bytes of the viewed contiguous storage.
### Subscripts
- [subscript(MutableSpan<Element>.Index) -> Element](mutablespan/subscript(_:).md)
  Accesses the element at the specified index in the `MutableSpan`.
- [subscript(unchecked _: MutableSpan<Element>.Index) -> Element](mutablespan/subscript(unchecked:).md)
  Accesses the element at the specified index in the `MutableSpan`.
### Type Aliases
- [MutableSpan.Index](mutablespan/index.md)
  The type that represents an index in a `MutableSpan`.
### Default Implementations
- [BorrowingSequence Implementations](mutablespan/borrowingsequence-implementations.md)

## Relationships

### Conforms To
- [BorrowingSequence](borrowingsequence.md)
- [ContiguousBytes](../Foundation/ContiguousBytes.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [struct Span](span.md)
  `Span<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [struct RawSpan](rawspan.md)
  `RawSpan` represents a contiguous region of memory which contains initialized bytes.
- [struct OutputSpan](outputspan.md)
  `OutputSpan` is a reference to a contiguous region of memory that starts with some number of initialized `Element` instances followed by uninitialized memory. It provides operations to access the items it stores, as well as to add new elements and to remove existing ones.
- [struct OutputRawSpan](outputrawspan.md)
  `OutputRawSpan` is a reference to a contiguous region of memory which starts with some number of initialized bytes, followed by uninitialized memory. It provides operations to access the bytes it stores, as well as to append and to remove bytes.
- [struct UTF8Span](utf8span.md)
  A borrowed view into contiguous memory that contains validly-encoded UTF-8 code units.
- [struct MutableRawSpan](mutablerawspan.md)
  `MutableRawSpan` represents a contiguous region of memory which contains initialized bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablespan)*