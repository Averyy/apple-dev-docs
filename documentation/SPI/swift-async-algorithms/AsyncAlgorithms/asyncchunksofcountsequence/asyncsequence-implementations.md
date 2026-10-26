---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchunksofcountsequence/asyncsequence-implementations"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncSequence Implementations

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Role**: API Collection

## Topics

### Instance Methods
- [func adjacentPairs() -> AsyncAdjacentPairsSequence<Self>](./adjacentpairs%28%29.md)
  An `AsyncSequence` that iterates over the adjacent pairs of the original original `AsyncSequence`.
- [func chunked(by: (Self.Element, Self.Element) -> Bool) -> AsyncChunkedByGroupSequence<Self, [Self.Element]>](./chunked%28by%29-5cpkg.md)
  Creates an asynchronous sequence that creates chunks by testing if elements belong in the same group.
- [func chunked<Signal>(by: Signal) -> AsyncChunksOfCountOrSignalSequence<Self, [Self.Element], Signal>](./chunked%28by%29-7gkpe.md)
  Creates an asynchronous sequence that creates chunks when a signal `AsyncSequence` produces an element.
- [func chunked<C>(by: AsyncTimerSequence<C>) -> AsyncChunksOfCountOrSignalSequence<Self, [Self.Element], AsyncTimerSequence<C>>](./chunked%28by%29-8r9sj.md)
  Creates an asynchronous sequence that creates chunks when an `AsyncTimerSequence` fires.
- [func chunked<Signal, Collected>(by: Signal, into: Collected.Type) -> AsyncChunksOfCountOrSignalSequence<Self, Collected, Signal>](./chunked%28by,into%29-3pq9r.md)
  Creates an asynchronous sequence that creates chunks of a given `RangeReplaceableCollection` type when a signal `AsyncSequence` produces an element.
- [func chunked<C, Collected>(by: AsyncTimerSequence<C>, into: Collected.Type) -> AsyncChunksOfCountOrSignalSequence<Self, Collected, AsyncTimerSequence<C>>](./chunked%28by,into%29-4iywh.md)
  Creates an asynchronous sequence that creates chunks of a given `RangeReplaceableCollection` type when an `AsyncTimerSequence` fires.
- [func chunked<Collected>(into: Collected.Type, by: (Self.Element, Self.Element) -> Bool) -> AsyncChunkedByGroupSequence<Self, Collected>](./chunked%28into,by%29.md)
  Creates an asynchronous sequence that creates chunks of a given `RangeReplaceableCollection` type by testing if elements belong in the same group.
- [func chunked<Subject, Collected>(into: Collected.Type, on: (Self.Element) -> Subject) -> AsyncChunkedOnProjectionSequence<Self, Subject, Collected>](./chunked%28into,on%29.md)
  Creates an asynchronous sequence that creates chunks of a given `RangeReplaceableCollection` type on the uniqueness of a given subject.
- [func chunked<Subject>(on: (Self.Element) -> Subject) -> AsyncChunkedOnProjectionSequence<Self, Subject, [Self.Element]>](./chunked%28on%29.md)
  Creates an asynchronous sequence that creates chunks on the uniqueness of a given subject.
- [func chunks(ofCount: Int) -> AsyncChunksOfCountSequence<Self, [Self.Element]>](./chunks%28ofcount%29.md)
  Creates an asynchronous sequence that creates chunks of a given count.
- [func chunks<Collected>(ofCount: Int, into: Collected.Type) -> AsyncChunksOfCountSequence<Self, Collected>](./chunks%28ofcount,into%29.md)
  Creates an asynchronous sequence that creates chunks of a given `RangeReplaceableCollection` of a given count.
- [func chunks<Signal>(ofCount: Int, or: Signal) -> AsyncChunksOfCountOrSignalSequence<Self, [Self.Element], Signal>](./chunks%28ofcount,or%29-3ubjk.md)
  Creates an asynchronous sequence that creates chunks of a given count or when a signal `AsyncSequence` produces an element.
- [func chunks<C>(ofCount: Int, or: AsyncTimerSequence<C>) -> AsyncChunksOfCountOrSignalSequence<Self, [Self.Element], AsyncTimerSequence<C>>](./chunks%28ofcount,or%29-q9o3.md)
  Creates an asynchronous sequence that creates chunks of a given count or when an `AsyncTimerSequence` fires.
- [func chunks<Signal, Collected>(ofCount: Int, or: Signal, into: Collected.Type) -> AsyncChunksOfCountOrSignalSequence<Self, Collected, Signal>](./chunks%28ofcount,or,into%29-1cawq.md)
  Creates an asynchronous sequence that creates chunks of a given `RangeReplaceableCollection` type of a given count or when a signal `AsyncSequence` produces an element.
- [func chunks<C, Collected>(ofCount: Int, or: AsyncTimerSequence<C>, into: Collected.Type) -> AsyncChunksOfCountOrSignalSequence<Self, Collected, AsyncTimerSequence<C>>](./chunks%28ofcount,or,into%29-1nzm0.md)
  Creates an asynchronous sequence that creates chunks of a given `RangeReplaceableCollection` type of a given count or when an `AsyncTimerSequence` fires.
- [func compacted<Unwrapped>() -> AsyncCompactedSequence<Self, Unwrapped>](./compacted%28%29.md)
  Returns a new `AsyncSequence` that iterates over every non-nil element from the original `AsyncSequence`.
- [func debounce(for: Duration, tolerance: Duration?) -> AsyncDebounceSequence<Self, ContinuousClock>](./debounce%28for,tolerance%29.md)
  Creates an asynchronous sequence that emits the latest element after a given quiescence period has elapsed.
- [func debounce<C>(for: C.Instant.Duration, tolerance: C.Instant.Duration?, clock: C) -> AsyncDebounceSequence<Self, C>](./debounce%28for,tolerance,clock%29.md)
  Creates an asynchronous sequence that emits the latest element after a given quiescence period has elapsed by using a specified Clock.
- [func interspersed(every: Int, with: () -> Self.Element) -> AsyncInterspersedSequence<Self>](./interspersed%28every,with%29-24mtj.md)
  Returns a new asynchronous sequence containing the elements of this asynchronous sequence, inserting the given separator between each element.
- [func interspersed(every: Int, with: Self.Element) -> AsyncInterspersedSequence<Self>](./interspersed%28every,with%29-2vznp.md)
  Returns a new asynchronous sequence containing the elements of this asynchronous sequence, inserting the given separator between each element.
- [func interspersed(every: Int, with: () throws -> Self.Element) -> AsyncThrowingInterspersedSequence<Self>](./interspersed%28every,with%29-4cusj.md)
  Returns a new asynchronous sequence containing the elements of this asynchronous sequence, inserting the given separator between each element.
- [func interspersed(every: Int, with: () async throws -> Self.Element) -> AsyncThrowingInterspersedSequence<Self>](./interspersed%28every,with%29-5ovib.md)
  Returns a new asynchronous sequence containing the elements of this asynchronous sequence, inserting the given separator between each element.
- [func interspersed(every: Int, with: () async -> Self.Element) -> AsyncInterspersedSequence<Self>](./interspersed%28every,with%29-9mbda.md)
  Returns a new asynchronous sequence containing the elements of this asynchronous sequence, inserting the given separator between each element.
- [func joined() -> AsyncJoinedSequence<Self>](./joined%28%29.md)
  Concatenate an `AsyncSequence` of `AsyncSequence` elements
- [func joined<Separator>(separator: Separator) -> AsyncJoinedBySeparatorSequence<Self, Separator>](./joined%28separator%29.md)
  Concatenate an `AsyncSequence` of `AsyncSequence` elements with a separator.
- [func mapError<MappedError>((Self.Failure) -> MappedError) -> some Sendable & AsyncSequence<Self.Element, MappedError>
](./maperror%28_%29-1k4j6.md)
  Converts any failure into a new error.
- [func mapError<MappedError>((Self.Failure) -> MappedError) -> some AsyncSequence<Self.Element, MappedError>
](./maperror%28_%29-4j050.md)
  Converts any failure into a new error.
- [func reductions((Self.Element, Self.Element) async -> Self.Element) -> AsyncInclusiveReductionsSequence<Self>](./reductions%28_%29.md)
  Returns an asynchronous sequence containing the accumulated results of combining the elements of the asynchronous sequence using the given closure.
- [func reductions<Result>(Result, (Result, Self.Element) async throws -> Result) -> AsyncThrowingExclusiveReductionsSequence<Self, Result>](./reductions%28_,_%29-5cznd.md)
  Returns an asynchronous sequence containing the accumulated results of combining the elements of the asynchronous sequence using the given error-throwing closure.
- [func reductions<Result>(Result, (Result, Self.Element) async -> Result) -> AsyncExclusiveReductionsSequence<Self, Result>](./reductions%28_,_%29-7rhy3.md)
  Returns an asynchronous sequence containing the accumulated results of combining the elements of the asynchronous sequence using the given closure.
- [func reductions<Result>(into: Result, (inout Result, Self.Element) async throws -> Void) -> AsyncThrowingExclusiveReductionsSequence<Self, Result>](./reductions%28into,_%29-3mzh0.md)
  Returns an asynchronous sequence containing the accumulated results of combining the elements of the asynchronous sequence using the given error-throwing closure.
- [func reductions<Result>(into: Result, (inout Result, Self.Element) async -> Void) -> AsyncExclusiveReductionsSequence<Self, Result>](./reductions%28into,_%29-wzc3.md)
  Returns an asynchronous sequence containing the accumulated results of combining the elements of the asynchronous sequence using the given closure.
- [func removeDuplicates() -> AsyncRemoveDuplicatesSequence<Self>](./removeduplicates%28%29.md)
  Creates an asynchronous sequence that omits repeated elements.
- [func removeDuplicates(by: (Self.Element, Self.Element) async -> Bool) -> AsyncRemoveDuplicatesSequence<Self>](./removeduplicates%28by%29-3r4jh.md)
  Creates an asynchronous sequence that omits repeated elements by testing them with a predicate.
- [func removeDuplicates(by: (Self.Element, Self.Element) async throws -> Bool) -> AsyncThrowingRemoveDuplicatesSequence<Self>](./removeduplicates%28by%29-9qau3.md)
  Creates an asynchronous sequence that omits repeated elements by testing them with an error-throwing predicate.
- [func share(bufferingPolicy: AsyncBufferSequencePolicy) -> some Sendable & AsyncSequence<Self.Element, Self.Failure>
](./share%28bufferingpolicy%29.md)
  Creates a shared async sequence that allows multiple concurrent iterations over a single source.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchunksofcountsequence/asyncsequence-implementations)*