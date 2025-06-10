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
- visionOS 1.1+
- watchOS 5.2+

## Declaration

```swift
@frozen
struct Span<Element> where Element : ~Copyable
```

#### Overview

A `Span` instance is a non-owning, non-escaping view into memory. When a `Span` is created, it inherits the lifetime of the container owning the contiguous memory, ensuring temporal safety and avoiding use-after-free errors. Operations on `Span` are bounds-checked, ensuring spcial safety and avoiding buffer overflow errors.

## Topics

### Instance Properties
- [var bytes: RawSpan](span/bytes.md)
- [var count: Int](span/count.md)
  The number of elements in the span.
- [var indices: Range<Span<Element>.Index>](span/indices.md)
  The indices that are valid for subscripting the span, in ascending order.
- [var isEmpty: Bool](span/isempty.md)
  A Boolean value indicating whether the span is empty.
### Instance Methods
- [func indices(of: borrowing Span<Element>) -> Range<Span<Element>.Index>?](span/indices(of:).md)
  Returns the indices within `self` where the memory represented by `span` is located, or `nil` if `span` is not located within `self`.
- [func isIdentical(to: Span<Element>) -> Bool](span/isidentical(to:).md)
  Returns a Boolean value indicating whether two `Span` instances refer to the same region in memory.
- [func withUnsafeBufferPointer<E, Result>((UnsafeBufferPointer<Element>) throws(E) -> Result) throws(E) -> Result](span/withunsafebufferpointer(_:).md)
  Calls a closure with a pointer to the viewed contiguous storage.
- [func withUnsafeBytes<E, Result>((UnsafeRawBufferPointer) throws(E) -> Result) throws(E) -> Result](span/withunsafebytes(_:).md)
  Calls the given closure with a pointer to the underlying bytes of the viewed contiguous storage.
### Subscripts
- [subscript(Span<Element>.Index) -> Element](span/subscript(_:)-2g4jz.md)
  Accesses the element at the specified position in the `Span`.
- [subscript(Span<Element>.Index) -> Element](span/subscript(_:)-3r1qm.md)
  Accesses the element at the specified position in the `Span`.
- [subscript(unchecked _: Span<Element>.Index) -> Element](span/subscript(unchecked:)-2no6f.md)
  Accesses the element at the specified position in the `Span`.
- [subscript(unchecked _: Span<Element>.Index) -> Element](span/subscript(unchecked:)-6gur1.md)
  Accesses the element at the specified position in the `Span`.
### Type Aliases
- [typealias Index](span/index.md)
  The representation for a position in `Span`.

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [struct RawSpan](rawspan.md)
  `RawSpan` represents a contiguous region of memory which contains initialized bytes.
- [struct OutputSpan](outputspan.md)
- [struct UTF8Span](utf8span.md)
  A borrowed view into contiguous memory that contains validly-encoded UTF-8 code units.
- [struct MutableSpan](mutablespan.md)
- [struct MutableRawSpan](mutablerawspan.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/span)*