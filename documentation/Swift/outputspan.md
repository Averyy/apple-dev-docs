# OutputSpan

**Framework**: Swift  
**Kind**: struct

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@frozen
struct OutputSpan<Element> where Element : ~Copyable
```

## Topics

### Instance Properties
- [var available: Int](outputspan/available.md)
- [let capacity: Int](outputspan/capacity.md)
- [var count: Int](outputspan/count.md)
- [var isEmpty: Bool](outputspan/isempty.md)
- [var mutableSpan: MutableSpan<Element>](outputspan/mutablespan.md)
- [var span: Span<Element>](outputspan/span.md)
### Instance Methods
- [func append(consuming Element)](outputspan/append(_:).md)
- [func append(from: inout some IteratorProtocol<Element>)](outputspan/append(from:)-1v4ec.md)
- [func append<S>(from: S) -> S.Iterator](outputspan/append(from:)-2u87a.md)
- [func append(fromContentsOf: Span<Element>)](outputspan/append(fromcontentsof:)-1t2se.md)
- [func append(fromContentsOf: borrowing MutableSpan<Element>)](outputspan/append(fromcontentsof:)-5oou5.md)
- [func append(fromContentsOf: some Collection<Element>)](outputspan/append(fromcontentsof:)-7cg6j.md)
- [func append(repeating: Element, count: Int)](outputspan/append(repeating:count:).md)
- [func moveAppend(fromContentsOf: consuming OutputSpan<Element>)](outputspan/moveappend(fromcontentsof:)-4rh59.md)
- [func moveAppend(fromContentsOf: Slice<UnsafeMutableBufferPointer<Element>>)](outputspan/moveappend(fromcontentsof:)-4uzut.md)
- [func moveAppend(fromContentsOf: UnsafeMutableBufferPointer<Element>)](outputspan/moveappend(fromcontentsof:)-c23r.md)
- [func relinquishBorrowedBytes() -> UnsafeMutableRawBufferPointer](outputspan/relinquishborrowedbytes.md)
- [func relinquishBorrowedMemory() -> UnsafeMutableBufferPointer<Element>](outputspan/relinquishborrowedmemory.md)
- [func removeAll()](outputspan/removeall.md)
- [func removeLast() -> Element?](outputspan/removelast.md)

## See Also

- [struct Span](span.md)
  `Span<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [struct RawSpan](rawspan.md)
  `RawSpan` represents a contiguous region of memory which contains initialized bytes.
- [struct UTF8Span](utf8span.md)
  A borrowed view into contiguous memory that contains validly-encoded UTF-8 code units.
- [struct MutableSpan](mutablespan.md)
- [struct MutableRawSpan](mutablerawspan.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/outputspan)*