# MutableRawSpan

**Framework**: Swift  
**Kind**: struct

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.1+
- watchOS 5.2+

## Declaration

```swift
@frozen
struct MutableRawSpan
```

## Topics

### Instance Properties
- [var byteCount: Int](mutablerawspan/bytecount.md)
- [var byteOffsets: Range<Int>](mutablerawspan/byteoffsets.md)
- [var bytes: RawSpan](mutablerawspan/bytes.md)
- [var isEmpty: Bool](mutablerawspan/isempty.md)
### Instance Methods
- [func extracting(Range<Int>) -> MutableRawSpan](mutablerawspan/extracting(_:)-18k75.md)
  Constructs a new span over the items within the supplied range of positions within this span.
- [func extracting(some RangeExpression<Int>) -> MutableRawSpan](mutablerawspan/extracting(_:)-6fpo6.md)
  Constructs a new span over the items within the supplied range of positions within this span.
- [func extracting((UnboundedRange_) -> ()) -> MutableRawSpan](mutablerawspan/extracting(_:)-7d5f1.md)
  Constructs a new span over all the items of this span.
- [func extracting(droppingFirst: Int) -> MutableRawSpan](mutablerawspan/extracting(droppingfirst:).md)
  Returns a span over all but the given number of initial elements.
- [func extracting(droppingLast: Int) -> MutableRawSpan](mutablerawspan/extracting(droppinglast:).md)
  Returns a span over all but the given number of trailing elements.
- [func extracting(first: Int) -> MutableRawSpan](mutablerawspan/extracting(first:).md)
  Returns a span containing the initial elements of this span, up to the specified maximum length.
- [func extracting(last: Int) -> MutableRawSpan](mutablerawspan/extracting(last:).md)
  Returns a span containing the final elements of the span, up to the given maximum length.
- [func extracting(unchecked: ClosedRange<Int>) -> MutableRawSpan](mutablerawspan/extracting(unchecked:)-4b7xa.md)
  Constructs a new span over the items within the supplied range of positions within this span.
- [func extracting(unchecked: Range<Int>) -> MutableRawSpan](mutablerawspan/extracting(unchecked:)-7oy38.md)
  Constructs a new span over the items within the supplied range of positions within this span.
- [func storeBytes<T>(of: T, toByteOffset: Int, as: T.Type)](mutablerawspan/storebytes(of:tobyteoffset:as:).md)
- [func storeBytes<T>(of: T, toUncheckedByteOffset: Int, as: T.Type)](mutablerawspan/storebytes(of:touncheckedbyteoffset:as:).md)
- [func unsafeLoad<T>(fromByteOffset: Int, as: T.Type) -> T](mutablerawspan/unsafeload(frombyteoffset:as:).md)
  Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [func unsafeLoad<T>(fromUncheckedByteOffset: Int, as: T.Type) -> T](mutablerawspan/unsafeload(fromuncheckedbyteoffset:as:).md)
  Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [func unsafeLoadUnaligned<T>(fromByteOffset: Int, as: T.Type) -> T](mutablerawspan/unsafeloadunaligned(frombyteoffset:as:).md)
  Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [func unsafeLoadUnaligned<T>(fromUncheckedByteOffset: Int, as: T.Type) -> T](mutablerawspan/unsafeloadunaligned(fromuncheckedbyteoffset:as:).md)
  Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [func update<S>(from: S) -> (unwritten: S.Iterator, byteOffset: Int)](mutablerawspan/update(from:)-16nqv.md)
- [func update<Element>(from: inout some IteratorProtocol) -> Int](mutablerawspan/update(from:)-9atr2.md)
- [func update(fromContentsOf: borrowing MutableRawSpan) -> Int](mutablerawspan/update(fromcontentsof:)-20his.md)
- [func update<Element>(fromContentsOf: borrowing MutableSpan<Element>) -> Int](mutablerawspan/update(fromcontentsof:)-2wzi7.md)
- [func update(fromContentsOf: RawSpan) -> Int](mutablerawspan/update(fromcontentsof:)-4x2gs.md)
- [func update<Element>(fromContentsOf: Span<Element>) -> Int](mutablerawspan/update(fromcontentsof:)-7q3x2.md)
- [func update<C>(fromContentsOf: C) -> Int](mutablerawspan/update(fromcontentsof:)-8jkkq.md)
- [func withUnsafeBytes<E, Result>((UnsafeRawBufferPointer) throws(E) -> Result) throws(E) -> Result](mutablerawspan/withunsafebytes(_:).md)
- [func withUnsafeMutableBytes<E, Result>((UnsafeMutableRawBufferPointer) throws(E) -> Result) throws(E) -> Result](mutablerawspan/withunsafemutablebytes(_:).md)

## Relationships

### Conforms To
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [struct Span](span.md)
  `Span<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [struct RawSpan](rawspan.md)
  `RawSpan` represents a contiguous region of memory which contains initialized bytes.
- [struct OutputSpan](outputspan.md)
- [struct UTF8Span](utf8span.md)
  A borrowed view into contiguous memory that contains validly-encoded UTF-8 code units.
- [struct MutableSpan](mutablespan.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablerawspan)*