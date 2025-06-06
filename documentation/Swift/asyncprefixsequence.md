# AsyncPrefixSequence

**Framework**: Swift  
**Kind**: struct

An asynchronous sequence, up to a specified maximum length, containing the initial elements of a base asynchronous sequence.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct AsyncPrefixSequence<Base> where Base : AsyncSequence
```

## Topics

### Structures
- [AsyncPrefixSequence.Iterator](asyncprefixsequence/iterator.md)
  The iterator that produces elements of the prefix sequence.
### Type Aliases
- [AsyncPrefixSequence.Failure](asyncprefixsequence/failure.md)
  The type of the error that can be produced by the sequence.
### Default Implementations
- [AsyncSequence Implementations](asyncprefixsequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](asyncsequence.md)
- [Copyable](copyable.md)
- [Sendable](sendable.md)

## See Also

- [func prefix(Int) -> AsyncPrefixSequence<Self>](asyncsequence/prefix(_:).md)
  Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.
- [func prefix(while: (Self.Element) async -> Bool) rethrows -> AsyncPrefixWhileSequence<Self>](asyncsequence/prefix(while:)-2xy95.md)
  Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given predicate.
- [struct AsyncPrefixWhileSequence](asyncprefixwhilesequence.md)
  An asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy a given predicate.
- [func prefix(while: (Self.Element) async throws -> Bool) rethrows -> AsyncThrowingPrefixWhileSequence<Self>](asyncsequence/prefix(while:)-6yp5n.md)
  Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given error-throwing predicate.
- [struct AsyncThrowingPrefixWhileSequence](asyncthrowingprefixwhilesequence.md)
  An asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given error-throwing predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncprefixsequence)*