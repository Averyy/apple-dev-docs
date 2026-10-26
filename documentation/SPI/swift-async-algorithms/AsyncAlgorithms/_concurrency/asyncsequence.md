---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/_concurrency/asyncsequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncSequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: extension  
**Role**: Extended Protocol

## Declaration

```swift
extension AsyncSequence
```

## Topics

### Instance Methods
- [func adjacentPairs() -> AsyncAdjacentPairsSequence<Self>](./asyncsequence/adjacentpairs%28%29.md)
  An `AsyncSequence` that iterates over the adjacent pairs of the original original `AsyncSequence`.
- [func buffer(policy: AsyncBufferSequencePolicy) -> AsyncBufferSequence<Self>](./asyncsequence/buffer%28policy%29.md)
  Creates an asynchronous sequence that buffers elements.
- [func chunked<C>(by: AsyncTimerSequence<C>) -> AsyncChunksOfCountOrSignalSequence<Self, [Self.Element], AsyncTimerSequence<C>>](./asyncsequence/chunked%28by%29-37yae.md)
  Creates an asynchronous sequence that creates chunks when an `AsyncTimerSequence` fires.
- [func chunked<Signal>(by: Signal) -> AsyncChunksOfCountOrSignalSequence<Self, [Self.Element], Signal>](./asyncsequence/chunked%28by%29-4ywif.md)
  Creates an asynchronous sequence that creates chunks when a signal `AsyncSequence` produces an element.
- [func chunked(by: (Self.Element, Self.Element) -> Bool) -> AsyncChunkedByGroupSequence<Self, [Self.Element]>](./asyncsequence/chunked%28by%29-6ueqa.md)
  Creates an asynchronous sequence that creates chunks by testing if elements belong in the same group.
- [func chunked<C, Collected>(by: AsyncTimerSequence<C>, into: Collected.Type) -> AsyncChunksOfCountOrSignalSequence<Self, Collected, AsyncTimerSequence<C>>](./asyncsequence/chunked%28by,into%29-1mct7.md)
  Creates an asynchronous sequence that creates chunks of a given `RangeReplaceableCollection` type when an `AsyncTimerSequence` fires.
- [func chunked<Signal, Collected>(by: Signal, into: Collected.Type) -> AsyncChunksOfCountOrSignalSequence<Self, Collected, Signal>](./asyncsequence/chunked%28by,into%29-97f3o.md)
  Creates an asynchronous sequence that creates chunks of a given `RangeReplaceableCollection` type when a signal `AsyncSequence` produces an element.
- [func chunked<Collected>(into: Collected.Type, by: (Self.Element, Self.Element) -> Bool) -> AsyncChunkedByGroupSequence<Self, Collected>](./asyncsequence/chunked%28into,by%29.md)
  Creates an asynchronous sequence that creates chunks of a given `RangeReplaceableCollection` type by testing if elements belong in the same group.
- [func chunked<Subject, Collected>(into: Collected.Type, on: (Self.Element) -> Subject) -> AsyncChunkedOnProjectionSequence<Self, Subject, Collected>](./asyncsequence/chunked%28into,on%29.md)
  Creates an asynchronous sequence that creates chunks of a given `RangeReplaceableCollection` type on the uniqueness of a given subject.
- [func chunked<Subject>(on: (Self.Element) -> Subject) -> AsyncChunkedOnProjectionSequence<Self, Subject, [Self.Element]>](./asyncsequence/chunked%28on%29.md)
  Creates an asynchronous sequence that creates chunks on the uniqueness of a given subject.
- [func chunks(ofCount: Int) -> AsyncChunksOfCountSequence<Self, [Self.Element]>](./asyncsequence/chunks%28ofcount%29.md)
  Creates an asynchronous sequence that creates chunks of a given count.
- [func chunks<Collected>(ofCount: Int, into: Collected.Type) -> AsyncChunksOfCountSequence<Self, Collected>](./asyncsequence/chunks%28ofcount,into%29.md)
  Creates an asynchronous sequence that creates chunks of a given `RangeReplaceableCollection` of a given count.
- [func chunks<C>(ofCount: Int, or: AsyncTimerSequence<C>) -> AsyncChunksOfCountOrSignalSequence<Self, [Self.Element], AsyncTimerSequence<C>>](./asyncsequence/chunks%28ofcount,or%29-5di6d.md)
  Creates an asynchronous sequence that creates chunks of a given count or when an `AsyncTimerSequence` fires.
- [func chunks<Signal>(ofCount: Int, or: Signal) -> AsyncChunksOfCountOrSignalSequence<Self, [Self.Element], Signal>](./asyncsequence/chunks%28ofcount,or%29-jf5u.md)
  Creates an asynchronous sequence that creates chunks of a given count or when a signal `AsyncSequence` produces an element.
- [func chunks<C, Collected>(ofCount: Int, or: AsyncTimerSequence<C>, into: Collected.Type) -> AsyncChunksOfCountOrSignalSequence<Self, Collected, AsyncTimerSequence<C>>](./asyncsequence/chunks%28ofcount,or,into%29-26oi5.md)
  Creates an asynchronous sequence that creates chunks of a given `RangeReplaceableCollection` type of a given count or when an `AsyncTimerSequence` fires.
- [func chunks<Signal, Collected>(ofCount: Int, or: Signal, into: Collected.Type) -> AsyncChunksOfCountOrSignalSequence<Self, Collected, Signal>](./asyncsequence/chunks%28ofcount,or,into%29-88z89.md)
  Creates an asynchronous sequence that creates chunks of a given `RangeReplaceableCollection` type of a given count or when a signal `AsyncSequence` produces an element.
- [func compacted<Unwrapped>() -> AsyncCompactedSequence<Self, Unwrapped>](./asyncsequence/compacted%28%29.md)
  Returns a new `AsyncSequence` that iterates over every non-nil element from the original `AsyncSequence`.
- [func debounce(for: Duration, tolerance: Duration?) -> AsyncDebounceSequence<Self, ContinuousClock>](./asyncsequence/debounce%28for,tolerance%29.md)
  Creates an asynchronous sequence that emits the latest element after a given quiescence period has elapsed.
- [func debounce<C>(for: C.Instant.Duration, tolerance: C.Instant.Duration?, clock: C) -> AsyncDebounceSequence<Self, C>](./asyncsequence/debounce%28for,tolerance,clock%29.md)
  Creates an asynchronous sequence that emits the latest element after a given quiescence period has elapsed by using a specified Clock.
- [func flatMapLatest<T>((Self.Element) -> T) -> some Sendable & AsyncSequence<T.Element, Self.Failure>
](./asyncsequence/flatmaplatest%28_%29-1liqq.md)
- [func flatMapLatest<T>((Self.Element) -> T) -> some Sendable & AsyncSequence<T.Element, Self.Failure>
](./asyncsequence/flatmaplatest%28_%29-3v327.md)
  Transforms elements into new asynchronous sequences, emitting elements from the most recent inner sequence.
- [func flatMapLatest<T>((Self.Element) -> T) -> some Sendable & AsyncSequence<T.Element, T.Failure>
](./asyncsequence/flatmaplatest%28_%29-46quo.md)
- [func interspersed(every: Int, with: () throws -> Self.Element) -> AsyncThrowingInterspersedSequence<Self>](./asyncsequence/interspersed%28every,with%29-37jjm.md)
  Returns a new asynchronous sequence containing the elements of this asynchronous sequence, inserting the given separator between each element.
- [func interspersed(every: Int, with: Self.Element) -> AsyncInterspersedSequence<Self>](./asyncsequence/interspersed%28every,with%29-48okb.md)
  Returns a new asynchronous sequence containing the elements of this asynchronous sequence, inserting the given separator between each element.
- [func interspersed(every: Int, with: () async -> Self.Element) -> AsyncInterspersedSequence<Self>](./asyncsequence/interspersed%28every,with%29-6z30d.md)
  Returns a new asynchronous sequence containing the elements of this asynchronous sequence, inserting the given separator between each element.
- [func interspersed(every: Int, with: () -> Self.Element) -> AsyncInterspersedSequence<Self>](./asyncsequence/interspersed%28every,with%29-7cm54.md)
  Returns a new asynchronous sequence containing the elements of this asynchronous sequence, inserting the given separator between each element.
- [func interspersed(every: Int, with: () async throws -> Self.Element) -> AsyncThrowingInterspersedSequence<Self>](./asyncsequence/interspersed%28every,with%29-pxz3.md)
  Returns a new asynchronous sequence containing the elements of this asynchronous sequence, inserting the given separator between each element.
- [func joined() -> AsyncJoinedSequence<Self>](./asyncsequence/joined%28%29.md)
  Concatenate an `AsyncSequence` of `AsyncSequence` elements
- [func joined<Separator>(separator: Separator) -> AsyncJoinedBySeparatorSequence<Self, Separator>](./asyncsequence/joined%28separator%29.md)
  Concatenate an `AsyncSequence` of `AsyncSequence` elements with a separator.
- [func mapError<MappedError>((Self.Failure) -> MappedError) -> some AsyncSequence<Self.Element, MappedError>
](./asyncsequence/maperror%28_%29-3f42g.md)
  Converts any failure into a new error.
- [func mapError<MappedError>((Self.Failure) -> MappedError) -> some Sendable & AsyncSequence<Self.Element, MappedError>
](./asyncsequence/maperror%28_%29-lejj.md)
  Converts any failure into a new error.
- [func reductions((Self.Element, Self.Element) async throws -> Self.Element) -> AsyncThrowingInclusiveReductionsSequence<Self>](./asyncsequence/reductions%28_%29-4efsu.md)
  Returns an asynchronous sequence containing the accumulated results of combining the elements of the asynchronous sequence using the given error-throwing closure.
- [func reductions((Self.Element, Self.Element) async -> Self.Element) -> AsyncInclusiveReductionsSequence<Self>](./asyncsequence/reductions%28_%29-58t9p.md)
  Returns an asynchronous sequence containing the accumulated results of combining the elements of the asynchronous sequence using the given closure.
- [func reductions<Result>(Result, (Result, Self.Element) async -> Result) -> AsyncExclusiveReductionsSequence<Self, Result>](./asyncsequence/reductions%28_,_%29-50jy3.md)
  Returns an asynchronous sequence containing the accumulated results of combining the elements of the asynchronous sequence using the given closure.
- [func reductions<Result>(Result, (Result, Self.Element) async throws -> Result) -> AsyncThrowingExclusiveReductionsSequence<Self, Result>](./asyncsequence/reductions%28_,_%29-8lxv9.md)
  Returns an asynchronous sequence containing the accumulated results of combining the elements of the asynchronous sequence using the given error-throwing closure.
- [func reductions<Result>(into: Result, (inout Result, Self.Element) async -> Void) -> AsyncExclusiveReductionsSequence<Self, Result>](./asyncsequence/reductions%28into,_%29-1ghas.md)
  Returns an asynchronous sequence containing the accumulated results of combining the elements of the asynchronous sequence using the given closure.
- [func reductions<Result>(into: Result, (inout Result, Self.Element) async throws -> Void) -> AsyncThrowingExclusiveReductionsSequence<Self, Result>](./asyncsequence/reductions%28into,_%29-t4an.md)
  Returns an asynchronous sequence containing the accumulated results of combining the elements of the asynchronous sequence using the given error-throwing closure.
- [func removeDuplicates() -> AsyncRemoveDuplicatesSequence<Self>](./asyncsequence/removeduplicates%28%29.md)
  Creates an asynchronous sequence that omits repeated elements.
- [func removeDuplicates(by: (Self.Element, Self.Element) async throws -> Bool) -> AsyncThrowingRemoveDuplicatesSequence<Self>](./asyncsequence/removeduplicates%28by%29-6epc2.md)
  Creates an asynchronous sequence that omits repeated elements by testing them with an error-throwing predicate.
- [func removeDuplicates(by: (Self.Element, Self.Element) async -> Bool) -> AsyncRemoveDuplicatesSequence<Self>](./asyncsequence/removeduplicates%28by%29-7geff.md)
  Creates an asynchronous sequence that omits repeated elements by testing them with a predicate.
- [func share(bufferingPolicy: AsyncBufferSequencePolicy) -> some Sendable & AsyncSequence<Self.Element, Self.Failure>
](./asyncsequence/share%28bufferingpolicy%29.md)
  Creates a shared async sequence that allows multiple concurrent iterations over a single source.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/_concurrency/asyncsequence)*