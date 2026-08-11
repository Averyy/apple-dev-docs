# Span.BorrowingIterator

**Framework**: Swift  
**Kind**: struct

A type that provides the sequence’s iteration interface and encapsulates its iteration state.

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
@frozen
struct BorrowingIterator
```

## Topics

### Initializers
- [init(Span<Element>)](span/borrowingiterator/init(_:).md)
### Instance Methods
- [func nextSpan(maxCount: Int) -> Span<Element>](span/borrowingiterator/nextspan(maxcount:).md)
  Returns a span over the next group of elements that are ready to by visited, up to the specifed maximum.
- [func skip(by: Int) -> Int](span/borrowingiterator/skip(by:).md)
  Advances the position of this iterator by the specified offset, or until the end of the underlying type’s elements.
### Type Aliases
- [Span.BorrowingIterator.Failure](span/borrowingiterator/failure.md)
### Default Implementations
- [BorrowingIteratorProtocol Implementations](span/borrowingiterator/borrowingiteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [BorrowingIteratorProtocol](borrowingiteratorprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/span/borrowingiterator)*