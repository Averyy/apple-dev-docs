# SpanIterator

**Framework**: Swift  
**Kind**: struct

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
struct SpanIterator<Element> where Element : ~Copyable
```

## Topics

### Initializers
- [init(Span<Element>)](spaniterator/init(_:).md)
### Instance Methods
- [func nextSpan(maximumCount: Int) -> Span<Element>](spaniterator/nextspan(maximumcount:).md)
  Returns a span over the next group of elements that are ready to by visited, up to the specifed maximum.
- [func skip(by: Int) -> Int](spaniterator/skip(by:).md)
  Advances the position of this iterator by the specified offset, or until the end of the underlying type’s elements.
### Default Implementations
- [BorrowingIteratorProtocol Implementations](spaniterator/borrowingiteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [BorrowingIteratorProtocol](borrowingiteratorprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/spaniterator)*