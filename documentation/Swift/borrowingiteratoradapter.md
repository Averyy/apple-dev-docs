# BorrowingIteratorAdapter

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
@frozen
struct BorrowingIteratorAdapter<Iterator> where Iterator : IteratorProtocol
```

## Topics

### Initializers
- [init(iterator: Iterator)](borrowingiteratoradapter/init(iterator:).md)
### Instance Methods
- [func nextSpan(maximumCount: Int) -> Span<Iterator.Element>](borrowingiteratoradapter/nextspan(maximumcount:).md)
  Returns a span over the next group of elements that are ready to by visited, up to the specifed maximum.
### Type Aliases
- [BorrowingIteratorAdapter.Element](borrowingiteratoradapter/element.md)
### Default Implementations
- [BorrowingIteratorProtocol Implementations](borrowingiteratoradapter/borrowingiteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [BorrowingIteratorProtocol](borrowingiteratorprotocol.md)

## See Also

- [protocol IteratorProtocol](iteratorprotocol.md)
  A type that supplies the values of a sequence one at a time.
- [protocol BorrowingIteratorProtocol](borrowingiteratorprotocol.md)
  A type that provides borrowed access to the values of a borrowing sequence.
- [protocol BorrowingSequence](borrowingsequence.md)
  A type that provides sequential, borrowing access to its elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/borrowingiteratoradapter)*