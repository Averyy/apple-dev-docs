# MutableRawSpan

**Framework**: Swift  
**Kind**: struct

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
### Instance Properties
- [var byteCount: Int](mutablerawspan/bytecount.md)
- [var byteOffsets: Range<Int>](mutablerawspan/byteoffsets.md)
- [var bytes: RawSpan](mutablerawspan/bytes.md)
- [var isEmpty: Bool](mutablerawspan/isempty.md)
### Instance Methods
- [func extracting(Range<Int>) -> MutableRawSpan](mutablerawspan/extracting(_:)-18k75.md)
- [func extracting(some RangeExpression<Int>) -> MutableRawSpan](mutablerawspan/extracting(_:)-6fpo6.md)
- [func extracting((UnboundedRange_) -> ()) -> MutableRawSpan](mutablerawspan/extracting(_:)-7d5f1.md)
- [func extracting(droppingFirst: Int) -> MutableRawSpan](mutablerawspan/extracting(droppingfirst:).md)
- [func extracting(droppingLast: Int) -> MutableRawSpan](mutablerawspan/extracting(droppinglast:).md)
- [func extracting(first: Int) -> MutableRawSpan](mutablerawspan/extracting(first:).md)
- [func extracting(last: Int) -> MutableRawSpan](mutablerawspan/extracting(last:).md)
- [func extracting(unchecked: ClosedRange<Int>) -> MutableRawSpan](mutablerawspan/extracting(unchecked:)-4b7xa.md)
- [func extracting(unchecked: Range<Int>) -> MutableRawSpan](mutablerawspan/extracting(unchecked:)-7oy38.md)
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