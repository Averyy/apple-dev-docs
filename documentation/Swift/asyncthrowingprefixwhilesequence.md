# AsyncThrowingPrefixWhileSequence

**Framework**: Swift  
**Kind**: struct

An asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given error-throwing predicate.

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
struct AsyncThrowingPrefixWhileSequence<Base> where Base : AsyncSequence
```

## Topics

### Structures
- [AsyncThrowingPrefixWhileSequence.Iterator](asyncthrowingprefixwhilesequence/iterator.md)
  The iterator that produces elements of the prefix-while sequence.
### Type Aliases
- [AsyncThrowingPrefixWhileSequence.Failure](asyncthrowingprefixwhilesequence/failure.md)
  The type of error produced by this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](asyncthrowingprefixwhilesequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](asyncsequence.md)
- [Copyable](copyable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [func prefix(Int) -> AsyncPrefixSequence<Self>](asyncsequence/prefix(_:).md)
  Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.
- [struct AsyncPrefixSequence](asyncprefixsequence.md)
  An asynchronous sequence, up to a specified maximum length, containing the initial elements of a base asynchronous sequence.
- [func prefix(while: (Self.Element) async -> Bool) rethrows -> AsyncPrefixWhileSequence<Self>](asyncsequence/prefix(while:)-2xy95.md)
  Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given predicate.
- [struct AsyncPrefixWhileSequence](asyncprefixwhilesequence.md)
  An asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy a given predicate.
- [func prefix(while: (Self.Element) async throws -> Bool) rethrows -> AsyncThrowingPrefixWhileSequence<Self>](asyncsequence/prefix(while:)-6yp5n.md)
  Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given error-throwing predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingprefixwhilesequence)*