# BorrowingSequence

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
protocol BorrowingSequence<Element> : ~Copyable, ~Escapable
```

## Topics

### Associated Types
- [associatedtype BorrowingIterator : BorrowingIteratorProtocol, ~Copyable, ~Escapable](borrowingsequence/borrowingiterator.md)
  A type that provides the sequence’s iteration interface and encapsulates its iteration state.
- [associatedtype Element : ~Copyable](borrowingsequence/element.md)
  A type representing the sequence’s elements.
### Instance Properties
- [var underestimatedCount: Int](borrowingsequence/underestimatedcount.md)
  A value less than or equal to the number of elements in the sequence, calculated nondestructively.
### Instance Methods
- [func makeBorrowingIterator() -> Self.BorrowingIterator](borrowingsequence/makeborrowingiterator.md)
  Returns a borrowing iterator over the elements of this sequence.

## Relationships

### Conforming Types
- [InlineArray](inlinearray.md)
- [MutableRawSpan](mutablerawspan.md)
- [MutableSpan](mutablespan.md)
- [RawSpan](rawspan.md)
- [Span](span.md)

## See Also

- [protocol IteratorProtocol](iteratorprotocol.md)
  A type that supplies the values of a sequence one at a time.
- [protocol BorrowingIteratorProtocol](borrowingiteratorprotocol.md)
  A type that provides borrowed access to the values of a borrowing sequence.
- [struct BorrowingIteratorAdapter](borrowingiteratoradapter.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/borrowingsequence)*