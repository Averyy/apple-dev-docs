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
- visionOS 1.1+
- watchOS 5.2+

## Declaration

```swift
@frozen
struct RawSpan
```

#### Overview

A `RawSpan` instance is a non-owning, non-escaping view into memory. When a `RawSpan` is created, it inherits the lifetime of the container owning the contiguous memory, ensuring temporal safety and avoiding use-after-free errors. Operations on `RawSpan` are bounds-checked, ensuring spcial safety and avoiding buffer overflow errors.

## Topics

### Instance Properties
- [var byteCount: Int](rawspan/bytecount.md)
  The number of bytes in the span.
- [var byteOffsets: Range<Int>](rawspan/byteoffsets.md)
  The indices that are valid for subscripting the span, in ascending order.
- [var isEmpty: Bool](rawspan/isempty.md)
  A Boolean value indicating whether the span is empty.
### Instance Methods
- [func byteOffsets(of: borrowing RawSpan) -> Range<Int>?](rawspan/byteoffsets(of:).md)
  Returns the offsets where the memory of `span` is located within the memory represented by `self`
- [func isIdentical(to: RawSpan) -> Bool](rawspan/isidentical(to:).md)
  Returns a Boolean value indicating whether two `RawSpan` instances refer to the same region in memory.
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

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [struct Span](span.md)
  `Span<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [struct OutputSpan](outputspan.md)
- [struct UTF8Span](utf8span.md)
  A borrowed view into contiguous memory that contains validly-encoded UTF-8 code units.
- [struct MutableSpan](mutablespan.md)
- [struct MutableRawSpan](mutablerawspan.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rawspan)*