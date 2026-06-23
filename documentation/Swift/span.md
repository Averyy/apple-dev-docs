# Span

**Framework**: Swift  
**Kind**: struct

`Span<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.

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
struct Span<Element> where Element : ~Copyable
```

#### Overview

A `Span` instance is a non-owning, non-escaping view into memory. When a `Span` is created, it inherits the lifetime of the container owning the contiguous memory, ensuring temporal safety and avoiding use-after-free errors. Operations on `Span` are bounds-checked, ensuring spatial safety and avoiding buffer overflow errors.

## Topics

### Initializers
- [init()](span/init.md)
  Create an empty span.
- [init(viewing: RawSpan)](span/init(viewing:)-18wsr.md)
  View initialized raw memory as a typed span.
- [init(viewing: RawSpan)](span/init(viewing:)-9d31g.md)
  View initialized raw memory as a span of bytes.
### Instance Properties
- [var bytes: RawSpan](span/bytes-6qp42.md)
  Construct a raw span over the memory represented by this span.
- [var bytes: RawSpan](span/bytes-8rxg.md)
  A raw span over the memory represented by this span.
- [var count: Int](span/count.md)
  The number of elements in the span.
- [var indices: Range<Span<Element>.Index>](span/indices.md)
  The indices that are valid for subscripting the span, in ascending order.
- [var isEmpty: Bool](span/isempty.md)
  A Boolean value indicating whether the span is empty.
### Instance Methods
- [func extracting(Range<Span<Element>.Index>) -> Span<Element>](span/extracting(_:)-1c6e6.md)
  Constructs a new span over the items within the supplied range of indices within this span.
- [func extracting(some RangeExpression<Int>) -> Span<Element>](span/extracting(_:)-48neh.md)
  Constructs a new span over the items within the supplied range of indices within this span.
- [func extracting(UnboundedRange) -> Span<Element>](span/extracting(_:)-57peb.md)
  Constructs a new span over all the items of this span.
- [func extracting(droppingFirst: Int) -> Span<Element>](span/extracting(droppingfirst:).md)
  Returns a span over all but the given number of initial elements.
- [func extracting(droppingLast: Int) -> Span<Element>](span/extracting(droppinglast:).md)
  Returns a span over all but the given number of trailing elements.
- [func extracting(first: Int) -> Span<Element>](span/extracting(first:).md)
  Returns a span containing the initial elements of this span, up to the specified maximum length.
- [func extracting(last: Int) -> Span<Element>](span/extracting(last:).md)
  Returns a span containing the trailing elements of the span, up to the given maximum length.
- [func extracting(unchecked: ClosedRange<Span<Element>.Index>) -> Span<Element>](span/extracting(unchecked:)-46y0h.md)
  Constructs a new span over the items within the supplied range of indices within this span.
- [func extracting(unchecked: Range<Span<Element>.Index>) -> Span<Element>](span/extracting(unchecked:)-8hfj1.md)
  Constructs a new span over the items within the supplied range of indices within this span.
- [func indices(of: borrowing Span<Element>) -> Range<Span<Element>.Index>?](span/indices(of:).md)
  Returns the indices within this span where the memory represented by other is located, or nil if other is not located within this span.
- [func isIdentical(to: Span<Element>) -> Bool](span/isidentical(to:).md)
  Returns a Boolean value indicating whether two instances refer to the same memory region.
- [func isTriviallyIdentical(to: Span<Element>) -> Bool](span/istriviallyidentical(to:).md)
  Returns a Boolean value indicating whether two instances refer to the same memory region.
- [func withBytes<R, E>((RawSpan) throws(E) -> R) throws(E) -> R](span/withbytes(_:).md)
- [func withUnsafeBufferPointer<E, Result>((UnsafeBufferPointer<Element>) throws(E) -> Result) throws(E) -> Result](span/withunsafebufferpointer(_:).md)
  Calls a closure with a pointer to the viewed contiguous storage.
- [func withUnsafeBytes<E, Result>((UnsafeRawBufferPointer) throws(E) -> Result) throws(E) -> Result](span/withunsafebytes(_:).md)
  Calls the given closure with a pointer to the underlying bytes of the viewed contiguous storage.
### Subscripts
- [subscript(Span<Element>.Index) -> Element](span/subscript(_:)-2g4jz.md)
  Accesses the element at the specified index in the `Span`.
- [subscript(Span<Element>.Index) -> Element](span/subscript(_:)-3r1qm.md)
  Accesses the element at the specified index in the `Span`.
- [subscript(unchecked _: Span<Element>.Index) -> Element](span/subscript(unchecked:)-2no6f.md)
  Accesses the element at the specified index in the `Span`.
- [subscript(unchecked _: Span<Element>.Index) -> Element](span/subscript(unchecked:)-6gur1.md)
  Accesses the element at the specified index in the `Span`.
### Type Aliases
- [typealias Index](span/index.md)
  The representation for an index in `Span`.
### Default Implementations
- [BorrowingSequence Implementations](span/borrowingsequence-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [BorrowingSequence](borrowingsequence.md)
- [ContiguousBytes](../Foundation/ContiguousBytes.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [struct RawSpan](rawspan.md)
  `RawSpan` represents a contiguous region of memory which contains initialized bytes.
- [struct OutputSpan](outputspan.md)
  `OutputSpan` is a reference to a contiguous region of memory that starts with some number of initialized `Element` instances followed by uninitialized memory. It provides operations to access the items it stores, as well as to add new elements and to remove existing ones.
- [struct OutputRawSpan](outputrawspan.md)
  `OutputRawSpan` is a reference to a contiguous region of memory which starts with some number of initialized bytes, followed by uninitialized memory. It provides operations to access the bytes it stores, as well as to append and to remove bytes.
- [struct UTF8Span](utf8span.md)
  A borrowed view into contiguous memory that contains validly-encoded UTF-8 code units.
- [struct MutableSpan](mutablespan.md)
  `MutableSpan<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [struct MutableRawSpan](mutablerawspan.md)
  `MutableRawSpan` represents a contiguous region of memory which contains initialized bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/span)*