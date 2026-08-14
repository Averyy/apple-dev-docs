# RawSpan

**Framework**: Swift  
**Kind**: struct

`RawSpan` represents a contiguous region of memory which contains initialized bytes.

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
struct RawSpan
```

#### Overview

A `RawSpan` instance is a non-owning, non-escaping view into memory. When a `RawSpan` is created, it inherits the lifetime of the container owning the contiguous memory, ensuring temporal safety and avoiding use-after-free errors. Operations on `RawSpan` are bounds-checked, ensuring spatial safety and avoiding buffer overflow errors.

## Topics

### Initializers
- [init()](rawspan/init.md)
  Create an empty span.
- [init<Element>(elements: Span<Element>)](rawspan/init(elements:).md)
  View a typed span as a raw span.
- [init<Element>(unsafeElements: Span<Element>)](rawspan/init(unsafeelements:).md)
  Unsafely view a typed span as a raw span.
### Instance Properties
- [var byteCount: Int](rawspan/bytecount.md)
  The number of bytes in the span.
- [var byteOffsets: Range<Int>](rawspan/byteoffsets.md)
  The indices that are valid for subscripting the span, in ascending order.
- [var isEmpty: Bool](rawspan/isempty.md)
  A Boolean value indicating whether the span is empty.
### Instance Methods
- [func byteOffsets(of: borrowing RawSpan) -> Range<Int>?](rawspan/byteoffsets(of:).md)
  Returns the byte offsets within this span where the memory represented by other is located, or nil if other is not located within this span.
- [func extracting(Range<Int>) -> RawSpan](rawspan/extracting(_:)-2imhy.md)
  Constructs a new span over the bytes within the supplied range of positions within this span.
- [func extracting(UnboundedRange) -> RawSpan](rawspan/extracting(_:)-3elv4.md)
  Constructs a new span over all the bytes of this span.
- [func extracting(some RangeExpression<Int>) -> RawSpan](rawspan/extracting(_:)-8oy0e.md)
  Constructs a new span over the bytes within the supplied range of positions within this span.
- [func extracting(droppingFirst: Int) -> RawSpan](rawspan/extracting(droppingfirst:).md)
  Returns a span over all but the given number of initial bytes.
- [func extracting(droppingLast: Int) -> RawSpan](rawspan/extracting(droppinglast:).md)
  Returns a span over all but the given number of trailing bytes.
- [func extracting(first: Int) -> RawSpan](rawspan/extracting(first:).md)
  Returns a span containing the initial bytes of this span, up to the specified maximum length.
- [func extracting(last: Int) -> RawSpan](rawspan/extracting(last:).md)
  Returns a span containing the trailing bytes of the span, up to the given maximum length.
- [func extracting(unchecked: ClosedRange<Int>) -> RawSpan](rawspan/extracting(unchecked:)-2hjqs.md)
  Constructs a new span over the bytes within the supplied range of positions within this span.
- [func extracting(unchecked: Range<Int>) -> RawSpan](rawspan/extracting(unchecked:)-527ri.md)
  Constructs a new span over the bytes within the supplied range of positions within this span.
- [func isIdentical(to: RawSpan) -> Bool](rawspan/isidentical(to:).md)
  Returns a Boolean value indicating whether two instances refer to the same memory region.
- [func isTriviallyIdentical(to: RawSpan) -> Bool](rawspan/istriviallyidentical(to:).md)
  Returns a Boolean value indicating whether two instances refer to the same memory region.
- [func load<T>(fromByteOffset: Int, as: T.Type) -> T](rawspan/load(frombyteoffset:as:).md)
  Returns a value constructed from the raw memory at the specified offset.
- [func load<T>(fromByteOffset: Int, as: T.Type, ByteOrder) -> T](rawspan/load(frombyteoffset:as:_:).md)
  Returns a value constructed from the raw memory at the specified offset.
- [func unsafeLoad<T>(fromByteOffset: Int, as: T.Type) -> T](rawspan/unsafeload(frombyteoffset:as:).md)
  Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [func unsafeLoad<T>(fromUncheckedByteOffset: Int, as: T.Type) -> T](rawspan/unsafeload(fromuncheckedbyteoffset:as:).md)
  Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [func unsafeLoadUnaligned<T>(fromByteOffset: Int, as: T.Type) -> T](rawspan/unsafeloadunaligned(frombyteoffset:as:).md)
  Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [func unsafeLoadUnaligned<T>(fromUncheckedByteOffset: Int, as: T.Type) -> T](rawspan/unsafeloadunaligned(fromuncheckedbyteoffset:as:).md)
  Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [func withUnsafeBytes<E, Result>((UnsafeRawBufferPointer) throws(E) -> Result) throws(E) -> Result](rawspan/withunsafebytes(_:).md)
  Calls the given closure with a pointer to the underlying bytes of the viewed contiguous storage.
### Subscripts
- [subscript(Int) -> UInt8](rawspan/subscript(_:).md)
  Accesses the byte at the specified offset in the span.
- [subscript(unchecked _: Int) -> UInt8](rawspan/subscript(unchecked:).md)
  Accesses the byte at the specified offset in the span.
### Default Implementations
- [Iterable Implementations](rawspan/iterable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [ContiguousBytes](../foundation/contiguousbytes.md)
- [Iterable](iterable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [struct Span](span.md)
  `Span<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rawspan)*