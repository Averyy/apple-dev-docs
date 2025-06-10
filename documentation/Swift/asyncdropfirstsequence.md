# AsyncDropFirstSequence

**Framework**: Swift  
**Kind**: struct

An asynchronous sequence which omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.

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
struct AsyncDropFirstSequence<Base> where Base : AsyncSequence
```

## Topics

### Structures
- [AsyncDropFirstSequence.Iterator](asyncdropfirstsequence/iterator.md)
  The iterator that produces elements of the drop-first sequence.
### Instance Methods
- [func dropFirst(Int) -> AsyncDropFirstSequence<Base>](asyncdropfirstsequence/dropfirst(_:).md)
  Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
### Type Aliases
- [AsyncDropFirstSequence.Failure](asyncdropfirstsequence/failure.md)
  The type of errors produced by this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](asyncdropfirstsequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](asyncsequence.md)
- [Copyable](copyable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [func dropFirst(Int) -> AsyncDropFirstSequence<Self>](asyncsequence/dropfirst(_:).md)
  Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [func drop(while: (Self.Element) async -> Bool) -> AsyncDropWhileSequence<Self>](asyncsequence/drop(while:)-9sp3b.md)
  Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [struct AsyncDropWhileSequence](asyncdropwhilesequence.md)
  An asynchronous sequence which omits elements from the base sequence until a given closure returns false, after which it passes through all remaining elements.
- [func drop(while: (Self.Element) async throws -> Bool) -> AsyncThrowingDropWhileSequence<Self>](asyncsequence/drop(while:)-67kgo.md)
  Omits elements from the base sequence until a given error-throwing closure returns false, after which it passes through all remaining elements.
- [struct AsyncThrowingDropWhileSequence](asyncthrowingdropwhilesequence.md)
  An asynchronous sequence which omits elements from the base sequence until a given error-throwing closure returns false, after which it passes through all remaining elements.
- [func filter((Self.Element) async -> Bool) -> AsyncFilterSequence<Self>](asyncsequence/filter(_:)-435af.md)
  Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
- [struct AsyncFilterSequence](asyncfiltersequence.md)
  An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy a given predicate.
- [func filter((Self.Element) async throws -> Bool) -> AsyncThrowingFilterSequence<Self>](asyncsequence/filter(_:)-2cc0l.md)
  Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given error-throwing predicate.
- [struct AsyncThrowingFilterSequence](asyncthrowingfiltersequence.md)
  An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given error-throwing predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncdropfirstsequence)*