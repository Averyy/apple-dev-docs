# BorrowingIteratorProtocol

**Framework**: Swift  
**Kind**: protocol

A type that provides borrowed access to the values of a borrowing sequence.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol BorrowingIteratorProtocol<Element, Failure> : ~Copyable, ~Escapable
```

## Topics

### Associated Types
- [associatedtype Element : ~Copyable](borrowingiteratorprotocol/element.md)
- [associatedtype Failure : Error = Never](borrowingiteratorprotocol/failure.md)
### Instance Methods
- [func nextSpan() throws(Self.Failure) -> Span<Self.Element>](borrowingiteratorprotocol/nextspan.md)
  Returns a span over the next group of elements that are ready to by visited, up to the specifed maximum.
- [func nextSpan(maxCount: Int) throws(Self.Failure) -> Span<Self.Element>](borrowingiteratorprotocol/nextspan(maxcount:).md)
  Returns a span over the next group of elements that are ready to by visited, up to the specifed maximum.
- [func skip(by: Int) throws(Self.Failure) -> Int](borrowingiteratorprotocol/skip(by:).md)
  Advances the position of this iterator by the specified offset, or until the end of the underlying type’s elements.

## Relationships

### Conforming Types
- [BorrowingIteratorAdapter](borrowingiteratoradapter.md)
- [Span.BorrowingIterator](span/borrowingiterator.md)

## See Also

- [protocol IteratorProtocol](iteratorprotocol.md)
  A type that supplies the values of a sequence one at a time.
- [struct BorrowingIteratorAdapter](borrowingiteratoradapter.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/borrowingiteratorprotocol)*