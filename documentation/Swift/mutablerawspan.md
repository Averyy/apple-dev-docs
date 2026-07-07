# MutableRawSpan

**Framework**: Swift  
**Kind**: struct

`MutableRawSpan` represents a contiguous region of memory which contains initialized bytes.

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
struct MutableRawSpan
```

## Topics

### Initializers
- [init()](mutablerawspan/init.md)
  Create an empty span.
- [init<Element>(elements: consuming MutableSpan<Element>)](mutablerawspan/init(elements:).md)
  Convert a typed span to a raw span.
- [init<Element>(mutating: inout MutableSpan<Element>)](mutablerawspan/init(mutating:).md)
  Mutate the elements of a typed span as bytes.
- [init<Element>(unsafeElements: consuming MutableSpan<Element>)](mutablerawspan/init(unsafeelements:).md)
  Unsafely convert a typed span to a raw span.
### Instance Properties
- [var byteCount: Int](mutablerawspan/bytecount.md)
  The number of bytes in the span.
- [var byteOffsets: Range<Int>](mutablerawspan/byteoffsets.md)
  The valid byte offsets for accessing this span, in ascending order.
- [var bytes: RawSpan](mutablerawspan/bytes.md)
  Borrow the underlying initialized memory for read-only access.
- [var isEmpty: Bool](mutablerawspan/isempty.md)
  A Boolean value indicating whether the span is empty.
### Instance Methods
- [func extracting(Range<Int>) -> MutableRawSpan](mutablerawspan/extracting(_:)-18k75.md)
  Constructs a new span over the bytes within the supplied range of positions within this span.
- [func extracting(some RangeExpression<Int>) -> MutableRawSpan](mutablerawspan/extracting(_:)-6fpo6.md)
  Constructs a new span over the bytes within the supplied range of positions within this span.
- [func extracting(UnboundedRange) -> MutableRawSpan](mutablerawspan/extracting(_:)-7d5f1.md)
  Constructs a new span over all the bytes of this span.
- [func extracting(droppingFirst: Int) -> MutableRawSpan](mutablerawspan/extracting(droppingfirst:).md)
  Returns a span over all but the given number of initial bytes.
- [func extracting(droppingLast: Int) -> MutableRawSpan](mutablerawspan/extracting(droppinglast:).md)
  Returns a span over all but the given number of trailing bytes.
- [func extracting(first: Int) -> MutableRawSpan](mutablerawspan/extracting(first:).md)
  Returns a span containing the initial bytes of this span, up to the specified maximum length.
- [func extracting(last: Int) -> MutableRawSpan](mutablerawspan/extracting(last:).md)
  Returns a span containing the trailing bytes of the span, up to the given maximum length.
- [func extracting(unchecked: ClosedRange<Int>) -> MutableRawSpan](mutablerawspan/extracting(unchecked:)-4b7xa.md)
  Constructs a new span over the bytes within the supplied range of positions within this span.
- [func extracting(unchecked: Range<Int>) -> MutableRawSpan](mutablerawspan/extracting(unchecked:)-7oy38.md)
  Constructs a new span over the bytes within the supplied range of positions within this span.
- [func load<T>(fromByteOffset: Int, as: T.Type) -> T](mutablerawspan/load(frombyteoffset:as:).md)
  Returns a value constructed from the raw memory at the specified offset.
- [func load<T>(fromByteOffset: Int, as: T.Type, ByteOrder) -> T](mutablerawspan/load(frombyteoffset:as:_:).md)
  Returns a value constructed from the raw memory at the specified offset.
- [func storeBytes<T>(of: T, toByteOffset: Int, as: T.Type)](mutablerawspan/storebytes(of:tobyteoffset:as:)-1afju.md)
  Stores the given value’s bytes to the specified offset into the span’s memory.
- [func storeBytes<T>(of: T, toByteOffset: Int, as: T.Type)](mutablerawspan/storebytes(of:tobyteoffset:as:)-37pwo.md)
  Stores the given value’s bytes into the span’s raw memory at the specified byte offset.
- [func storeBytes<T>(of: T, toByteOffset: Int, as: T.Type, ByteOrder)](mutablerawspan/storebytes(of:tobyteoffset:as:_:).md)
  Stores the given value’s bytes to the specified offset into the span’s memory.
- [func storeBytes<T>(of: T, toUncheckedByteOffset: Int, as: T.Type)](mutablerawspan/storebytes(of:touncheckedbyteoffset:as:).md)
  Stores the given value’s bytes into the span’s raw memory at the specified byte offset.
- [func storeBytes<T>(repeating: T, count: Int, as: T.Type)](mutablerawspan/storebytes(repeating:count:as:)-6822y.md)
  Stores the given value’s bytes repeatedly into this span’s memory.
- [func storeBytes<T>(repeating: T, count: Int, as: T.Type)](mutablerawspan/storebytes(repeating:count:as:)-7cd7p.md)
  Stores the given value’s bytes repeatedly into this span’s memory.
- [func storeBytes<T>(repeating: T, count: Int, as: T.Type, ByteOrder)](mutablerawspan/storebytes(repeating:count:as:_:).md)
  Stores the given value’s bytes repeatedly into this span’s memory.
- [func unsafeLoad<T>(fromByteOffset: Int, as: T.Type) -> T](mutablerawspan/unsafeload(frombyteoffset:as:).md)
  Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [func unsafeLoad<T>(fromUncheckedByteOffset: Int, as: T.Type) -> T](mutablerawspan/unsafeload(fromuncheckedbyteoffset:as:).md)
  Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [func unsafeLoadUnaligned<T>(fromByteOffset: Int, as: T.Type) -> T](mutablerawspan/unsafeloadunaligned(frombyteoffset:as:).md)
  Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [func unsafeLoadUnaligned<T>(fromUncheckedByteOffset: Int, as: T.Type) -> T](mutablerawspan/unsafeloadunaligned(fromuncheckedbyteoffset:as:).md)
  Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [func withUnsafeBytes<E, Result>((UnsafeRawBufferPointer) throws(E) -> Result) throws(E) -> Result](mutablerawspan/withunsafebytes(_:).md)
  Calls the given closure with a pointer to the underlying bytes of the viewed contiguous storage.
- [func withUnsafeMutableBytes<E, Result>((UnsafeMutableRawBufferPointer) throws(E) -> Result) throws(E) -> Result](mutablerawspan/withunsafemutablebytes(_:).md)
  Calls the given closure with a mutable pointer to the underlying bytes of the viewed contiguous storage.
### Subscripts
- [subscript(Int) -> UInt8](mutablerawspan/subscript(_:).md)
  Accesses the byte at the specified offset in the span.
- [subscript(unchecked _: Int) -> UInt8](mutablerawspan/subscript(unchecked:).md)
  Accesses the byte at the specified offset in the span.
### Default Implementations
- [BorrowingSequence Implementations](mutablerawspan/borrowingsequence-implementations.md)

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
- [struct MutableSpan](mutablespan.md)
  `MutableSpan<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [struct SpanIterator](spaniterator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablerawspan)*