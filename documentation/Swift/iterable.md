# Iterable

**Framework**: Swift  
**Kind**: protocol

A type that provides sequential, borrowing access to its elements.

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
protocol Iterable<Element, Failure> : ~Copyable, ~Escapable
```

## Topics

### Associated Types
- [associatedtype BorrowingIterator : BorrowingIteratorProtocol, ~Copyable, ~Escapable](iterable/borrowingiterator.md)
  A type that provides the sequence’s iteration interface and encapsulates its iteration state.
- [associatedtype Element : ~Copyable](iterable/element.md)
  A type representing the sequence’s elements.
- [associatedtype Failure = Never](iterable/failure.md)
### Instance Properties
- [var underestimatedCount: Int](iterable/underestimatedcount.md)
  A value less than or equal to the number of elements in the sequence, calculated nondestructively.
### Instance Methods
- [func makeBorrowingIterator() -> Self.BorrowingIterator](iterable/makeborrowingiterator.md)
  Returns a borrowing iterator over the elements of this sequence.

## Relationships

### Conforming Types
- [InlineArray](inlinearray.md)
- [MutableRawSpan](mutablerawspan.md)
- [MutableSpan](mutablespan.md)
- [OutputRawSpan](outputrawspan.md)
- [OutputSpan](outputspan.md)
- [RawSpan](rawspan.md)
- [Span](span.md)
- [UniqueArray](uniquearray.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/iterable)*