# Span.BorrowingIterator

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

A type that provides the sequence’s iteration interface and encapsulates its iteration state.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@frozen
struct BorrowingIterator
```

## Topics

### Initializers
- [init(Span<Element>)](./borrowingiterator/init%28_%29.md)
### Instance Methods
- [func nextSpan(maxCount: Int) -> Span<Element>](./borrowingiterator/nextspan%28maxcount%29.md)
  Returns a span over the next group of elements that are ready to by visited, up to the specifed maximum.
- [func skip(by: Int) -> Int](./borrowingiterator/skip%28by%29.md)
  Advances the position of this iterator by the specified offset, or until the end of the underlying type’s elements.
### Type Aliases
- [Span.BorrowingIterator.Failure](./borrowingiterator/failure.md)
### Default Implementations
- [BorrowingIteratorProtocol Implementations](./borrowingiterator/borrowingiteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [BorrowingIteratorProtocol](../borrowingiteratorprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/span/borrowingiterator)*