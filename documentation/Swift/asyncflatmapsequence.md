# AsyncFlatMapSequence

**Framework**: Swift  
**Kind**: struct

An asynchronous sequence that concatenates the results of calling a given transformation with each element of this sequence.

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
struct AsyncFlatMapSequence<Base, SegmentOfResult> where Base : AsyncSequence, SegmentOfResult : AsyncSequence
```

## Topics

### Structures
- [AsyncFlatMapSequence.Iterator](asyncflatmapsequence/iterator.md)
  The iterator that produces elements of the flat map sequence.
### Type Aliases
- [AsyncFlatMapSequence.Failure](asyncflatmapsequence/failure.md)
  The type of error produced by this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](asyncflatmapsequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](asyncsequence.md)
- [Copyable](copyable.md)
- [Sendable](sendable.md)

## See Also

- [func map<Transformed>((Self.Element) async -> Transformed) -> AsyncMapSequence<Self, Transformed>](asyncsequence/map(_:)-1q1k3.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [struct AsyncMapSequence](asyncmapsequence.md)
  An asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [func map<Transformed>((Self.Element) async throws -> Transformed) -> AsyncThrowingMapSequence<Self, Transformed>](asyncsequence/map(_:)-70wgb.md)
  Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [struct AsyncThrowingMapSequence](asyncthrowingmapsequence.md)
  An asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [func compactMap<ElementOfResult>((Self.Element) async -> ElementOfResult?) -> AsyncCompactMapSequence<Self, ElementOfResult>](asyncsequence/compactmap(_:)-gfdq.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [struct AsyncCompactMapSequence](asynccompactmapsequence.md)
  An asynchronous sequence that maps a given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [func compactMap<ElementOfResult>((Self.Element) async throws -> ElementOfResult?) -> AsyncThrowingCompactMapSequence<Self, ElementOfResult>](asyncsequence/compactmap(_:)-1f8zn.md)
  Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [struct AsyncThrowingCompactMapSequence](asyncthrowingcompactmapsequence.md)
  An asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [struct AsyncThrowingFlatMapSequence](asyncthrowingflatmapsequence.md)
  An asynchronous sequence that concatenates the results of calling a given error-throwing transformation with each element of this sequence.
- [func reduce<Result>(Result, (Result, Self.Element) async throws -> Result) async rethrows -> Result](asyncsequence/reduce(_:_:).md)
  Returns the result of combining the elements of the asynchronous sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) async throws -> Void) async rethrows -> Result](asyncsequence/reduce(into:_:).md)
  Returns the result of combining the elements of the asynchronous sequence using the given closure, given a mutable initial value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncflatmapsequence)*