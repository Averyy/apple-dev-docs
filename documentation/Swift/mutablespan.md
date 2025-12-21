# MutableSpan

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
struct MutableSpan<Element> where Element : ~Copyable
```

## Topics

### Initializers
- [init()](mutablespan/init.md)
### Instance Properties
- [var bytes: RawSpan](mutablespan/bytes.md)
  Construct a RawSpan over the memory represented by this span
- [var count: Int](mutablespan/count.md)
- [var indices: Range<MutableSpan<Element>.Index>](mutablespan/indices.md)
- [var isEmpty: Bool](mutablespan/isempty.md)
- [var mutableBytes: MutableRawSpan](mutablespan/mutablebytes.md)
  Construct a MutableRawSpan over the memory represented by this span
- [var span: Span<Element>](mutablespan/span.md)
### Instance Methods
- [func extracting(some RangeExpression<Int>) -> MutableSpan<Element>](mutablespan/extracting(_:)-2g8w3.md)
- [func extracting((UnboundedRange_) -> ()) -> MutableSpan<Element>](mutablespan/extracting(_:)-80srp.md)
- [func extracting(Range<MutableSpan<Element>.Index>) -> MutableSpan<Element>](mutablespan/extracting(_:)-bphj.md)
- [func extracting(droppingFirst: Int) -> MutableSpan<Element>](mutablespan/extracting(droppingfirst:).md)
- [func extracting(droppingLast: Int) -> MutableSpan<Element>](mutablespan/extracting(droppinglast:).md)
- [func extracting(first: Int) -> MutableSpan<Element>](mutablespan/extracting(first:).md)
- [func extracting(last: Int) -> MutableSpan<Element>](mutablespan/extracting(last:).md)
- [func extracting(unchecked: Range<MutableSpan<Element>.Index>) -> MutableSpan<Element>](mutablespan/extracting(unchecked:)-23qq.md)
- [func extracting(unchecked: ClosedRange<MutableSpan<Element>.Index>) -> MutableSpan<Element>](mutablespan/extracting(unchecked:)-4y8oj.md)
- [func swapAt(MutableSpan<Element>.Index, MutableSpan<Element>.Index)](mutablespan/swapat(_:_:).md)
- [func swapAt(unchecked: MutableSpan<Element>.Index, unchecked: MutableSpan<Element>.Index)](mutablespan/swapat(unchecked:unchecked:).md)
- [func update(repeating: consuming Element)](mutablespan/update(repeating:).md)
- [func withUnsafeBufferPointer<E, Result>((UnsafeBufferPointer<Element>) throws(E) -> Result) throws(E) -> Result](mutablespan/withunsafebufferpointer(_:).md)
- [func withUnsafeBytes<E, Result>((UnsafeRawBufferPointer) throws(E) -> Result) throws(E) -> Result](mutablespan/withunsafebytes(_:).md)
- [func withUnsafeMutableBufferPointer<E, Result>((UnsafeMutableBufferPointer<Element>) throws(E) -> Result) throws(E) -> Result](mutablespan/withunsafemutablebufferpointer(_:).md)
- [func withUnsafeMutableBytes<E, Result>((UnsafeMutableRawBufferPointer) throws(E) -> Result) throws(E) -> Result](mutablespan/withunsafemutablebytes(_:).md)
### Subscripts
- [subscript(MutableSpan<Element>.Index) -> Element](mutablespan/subscript(_:).md)
  Accesses the element at the specified position in the `Span`.
- [subscript(unchecked _: MutableSpan<Element>.Index) -> Element](mutablespan/subscript(unchecked:).md)
  Accesses the element at the specified position in the `Span`.
### Type Aliases
- [MutableSpan.Index](mutablespan/index.md)

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
- [struct MutableRawSpan](mutablerawspan.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablespan)*