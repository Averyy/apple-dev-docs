# MutableSpan

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
struct MutableSpan<Element> where Element : ~Copyable
```

## Topics

### Instance Properties
- [var bytes: RawSpan](mutablespan/bytes.md)
  Construct a RawSpan over the memory represented by this span
- [var count: Int](mutablespan/count.md)
- [var indices: Range<MutableSpan<Element>.Index>](mutablespan/indices.md)
- [var isEmpty: Bool](mutablespan/isempty.md)
- [var span: Span<Element>](mutablespan/span.md)
### Instance Methods
- [func extracting(some RangeExpression<Int>) -> MutableSpan<Element>](mutablespan/extracting(_:)-2g8w3.md)
  Constructs a new span over the items within the supplied range of positions within this span.
- [func extracting((UnboundedRange_) -> ()) -> MutableSpan<Element>](mutablespan/extracting(_:)-80srp.md)
  Constructs a new span over all the items of this span.
- [func extracting(Range<MutableSpan<Element>.Index>) -> MutableSpan<Element>](mutablespan/extracting(_:)-bphj.md)
  Constructs a new span over the items within the supplied range of positions within this span.
- [func extracting(droppingFirst: Int) -> MutableSpan<Element>](mutablespan/extracting(droppingfirst:).md)
  Returns a span over all but the given number of initial elements.
- [func extracting(droppingLast: Int) -> MutableSpan<Element>](mutablespan/extracting(droppinglast:).md)
  Returns a span over all but the given number of trailing elements.
- [func extracting(first: Int) -> MutableSpan<Element>](mutablespan/extracting(first:).md)
  Returns a span containing the initial elements of this span, up to the specified maximum length.
- [func extracting(last: Int) -> MutableSpan<Element>](mutablespan/extracting(last:).md)
  Returns a span containing the final elements of the span, up to the given maximum length.
- [func extracting(unchecked: Range<MutableSpan<Element>.Index>) -> MutableSpan<Element>](mutablespan/extracting(unchecked:)-23qq.md)
  Constructs a new span over the items within the supplied range of positions within this span.
- [func extracting(unchecked: ClosedRange<MutableSpan<Element>.Index>) -> MutableSpan<Element>](mutablespan/extracting(unchecked:)-4y8oj.md)
  Constructs a new span over the items within the supplied range of positions within this span.
- [func moveUpdate(fromContentsOf: Slice<UnsafeMutableBufferPointer<Element>>) -> MutableSpan<Element>.Index](mutablespan/moveupdate(fromcontentsof:)-58xhz.md)
- [func moveUpdate(fromContentsOf: UnsafeMutableBufferPointer<Element>) -> MutableSpan<Element>.Index](mutablespan/moveupdate(fromcontentsof:)-6ugek.md)
- [func swapAt(MutableSpan<Element>.Index, MutableSpan<Element>.Index)](mutablespan/swapat(_:_:).md)
- [func swapAt(unchecked: MutableSpan<Element>.Index, unchecked: MutableSpan<Element>.Index)](mutablespan/swapat(unchecked:unchecked:).md)
- [func update(from: inout some IteratorProtocol<Element>) -> MutableSpan<Element>.Index](mutablespan/update(from:)-167zz.md)
- [func update(from: inout some IteratorProtocol<Element>) -> MutableSpan<Element>.Index](mutablespan/update(from:)-5gkco.md)
- [func update<S>(from: S) -> (unwritten: S.Iterator, index: MutableSpan<Element>.Index)](mutablespan/update(from:)-76or.md)
- [func update<S>(from: S) -> (unwritten: S.Iterator, index: MutableSpan<Element>.Index)](mutablespan/update(from:)-9sp45.md)
- [func update(fromContentsOf: borrowing MutableSpan<Element>) -> MutableSpan<Element>.Index](mutablespan/update(fromcontentsof:)-12gmk.md)
- [func update(fromContentsOf: some Collection<Element>) -> MutableSpan<Element>.Index](mutablespan/update(fromcontentsof:)-31fdu.md)
- [func update(fromContentsOf: some Collection<Element>) -> MutableSpan<Element>.Index](mutablespan/update(fromcontentsof:)-37er7.md)
- [func update(fromContentsOf: borrowing MutableSpan<Element>) -> MutableSpan<Element>.Index](mutablespan/update(fromcontentsof:)-6stp1.md)
- [func update(fromContentsOf: Span<Element>) -> MutableSpan<Element>.Index](mutablespan/update(fromcontentsof:)-72v9q.md)
- [func update(fromContentsOf: Span<Element>) -> MutableSpan<Element>.Index](mutablespan/update(fromcontentsof:)-9gon4.md)
- [func update(repeating: Element)](mutablespan/update(repeating:)-6n0yn.md)
- [func update(repeating: consuming Element)](mutablespan/update(repeating:)-6welb.md)
- [func withUnsafeBufferPointer<E, Result>((UnsafeBufferPointer<Element>) throws(E) -> Result) throws(E) -> Result](mutablespan/withunsafebufferpointer(_:).md)
- [func withUnsafeBytes<E, Result>((UnsafeRawBufferPointer) throws(E) -> Result) throws(E) -> Result](mutablespan/withunsafebytes(_:).md)
- [func withUnsafeMutableBufferPointer<E, Result>((UnsafeMutableBufferPointer<Element>) throws(E) -> Result) throws(E) -> Result](mutablespan/withunsafemutablebufferpointer(_:).md)
- [func withUnsafeMutableBytes<E, Result>((UnsafeMutableRawBufferPointer) throws(E) -> Result) throws(E) -> Result](mutablespan/withunsafemutablebytes(_:).md)
### Subscripts
- [subscript(MutableSpan<Element>.Index) -> Element](mutablespan/subscript(_:)-2bznv.md)
  Accesses the element at the specified position in the `Span`.
- [subscript(MutableSpan<Element>.Index) -> Element](mutablespan/subscript(_:)-2n34d.md)
  Accesses the element at the specified position in the `Span`.
- [subscript(unchecked _: MutableSpan<Element>.Index) -> Element](mutablespan/subscript(unchecked:)-19s3c.md)
  Accesses the element at the specified position in the `Span`.
- [subscript(unchecked _: MutableSpan<Element>.Index) -> Element](mutablespan/subscript(unchecked:)-jf5f.md)
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