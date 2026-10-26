---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/asyncsequence-implementations"
framework: "swift-configuration/Configuration"
---

# AsyncSequence Implementations

**Framework**: swift-configuration/Configuration  
**Role**: API Collection

## Topics

### Instance Properties
- [var characters: AsyncCharacterSequence<Self>](./characters.md)
- [var lines: AsyncLineSequence<Self>](./lines.md)
- [var unicodeScalars: AsyncUnicodeScalarSequence<Self>](./unicodescalars.md)
### Instance Methods
- [func adjacentPairs() -> AsyncAdjacentPairsSequence<Self>](./adjacentpairs%28%29.md)
- [func allSatisfy((Self.Element) async throws -> Bool) async rethrows -> Bool](./allsatisfy%28_%29.md)
- [func buffer(policy: AsyncBufferSequencePolicy) -> AsyncBufferSequence<Self>](./buffer%28policy%29.md)
- [func cancelOnGracefulShutdown() -> AsyncCancelOnGracefulShutdownSequence<Self>](./cancelongracefulshutdown%28%29.md)
- [func chunked<Signal>(by: Signal) -> AsyncChunksOfCountOrSignalSequence<Self, [Self.Element], Signal>](./chunked%28by%29-7z81j.md)
- [func chunked(by: (Self.Element, Self.Element) -> Bool) -> AsyncChunkedByGroupSequence<Self, [Self.Element]>](./chunked%28by%29-b6h6.md)
- [func chunked<C>(by: AsyncTimerSequence<C>) -> AsyncChunksOfCountOrSignalSequence<Self, [Self.Element], AsyncTimerSequence<C>>](./chunked%28by%29-trjw.md)
- [func chunked<Signal, Collected>(by: Signal, into: Collected.Type) -> AsyncChunksOfCountOrSignalSequence<Self, Collected, Signal>](./chunked%28by,into%29-6rvuc.md)
- [func chunked<C, Collected>(by: AsyncTimerSequence<C>, into: Collected.Type) -> AsyncChunksOfCountOrSignalSequence<Self, Collected, AsyncTimerSequence<C>>](./chunked%28by,into%29-71xda.md)
- [func chunked<Collected>(into: Collected.Type, by: (Self.Element, Self.Element) -> Bool) -> AsyncChunkedByGroupSequence<Self, Collected>](./chunked%28into,by%29.md)
- [func chunked<Subject, Collected>(into: Collected.Type, on: (Self.Element) -> Subject) -> AsyncChunkedOnProjectionSequence<Self, Subject, Collected>](./chunked%28into,on%29.md)
- [func chunked<Subject>(on: (Self.Element) -> Subject) -> AsyncChunkedOnProjectionSequence<Self, Subject, [Self.Element]>](./chunked%28on%29.md)
- [func chunks(ofCount: Int) -> AsyncChunksOfCountSequence<Self, [Self.Element]>](./chunks%28ofcount%29.md)
- [func chunks<Collected>(ofCount: Int, into: Collected.Type) -> AsyncChunksOfCountSequence<Self, Collected>](./chunks%28ofcount,into%29.md)
- [func chunks<C>(ofCount: Int, or: AsyncTimerSequence<C>) -> AsyncChunksOfCountOrSignalSequence<Self, [Self.Element], AsyncTimerSequence<C>>](./chunks%28ofcount,or%29-8u4c4.md)
- [func chunks<Signal>(ofCount: Int, or: Signal) -> AsyncChunksOfCountOrSignalSequence<Self, [Self.Element], Signal>](./chunks%28ofcount,or%29-9w0pm.md)
- [func chunks<C, Collected>(ofCount: Int, or: AsyncTimerSequence<C>, into: Collected.Type) -> AsyncChunksOfCountOrSignalSequence<Self, Collected, AsyncTimerSequence<C>>](./chunks%28ofcount,or,into%29-50hk4.md)
- [func chunks<Signal, Collected>(ofCount: Int, or: Signal, into: Collected.Type) -> AsyncChunksOfCountOrSignalSequence<Self, Collected, Signal>](./chunks%28ofcount,or,into%29-woc3.md)
- [func compactMap<ElementOfResult>((Self.Element) async -> ElementOfResult?) -> AsyncCompactMapSequence<Self, ElementOfResult>](./compactmap%28_%29-88jhv.md)
- [func compactMap<ElementOfResult>((Self.Element) async throws -> ElementOfResult?) -> AsyncThrowingCompactMapSequence<Self, ElementOfResult>](./compactmap%28_%29-8cyh2.md)
- [func compacted<Unwrapped>() -> AsyncCompactedSequence<Self, Unwrapped>](./compacted%28%29.md)
- [func contains(Self.Element) async rethrows -> Bool](./contains%28_%29.md)
- [func contains(where: (Self.Element) async throws -> Bool) async rethrows -> Bool](./contains%28where%29.md)
- [func debounce(for: Duration, tolerance: Duration?) -> AsyncDebounceSequence<Self, ContinuousClock>](./debounce%28for,tolerance%29.md)
- [func debounce<C>(for: C.Instant.Duration, tolerance: C.Instant.Duration?, clock: C) -> AsyncDebounceSequence<Self, C>](./debounce%28for,tolerance,clock%29.md)
- [func drop(while: (Self.Element) async -> Bool) -> AsyncDropWhileSequence<Self>](./drop%28while%29.md)
- [func dropFirst(Int) -> AsyncDropFirstSequence<Self>](./dropfirst%28_%29.md)
- [func filter((Self.Element) async -> Bool) -> AsyncFilterSequence<Self>](./filter%28_%29.md)
- [func first(where: (Self.Element) async throws -> Bool) async rethrows -> Self.Element?](./first%28where%29.md)
- [func flatMap<SegmentOfResult>((Self.Element) async -> SegmentOfResult) -> AsyncFlatMapSequence<Self, SegmentOfResult>](./flatmap%28_%29-1acl8.md)
- [func flatMap<SegmentOfResult>((Self.Element) async -> SegmentOfResult) -> AsyncFlatMapSequence<Self, SegmentOfResult>](./flatmap%28_%29-2tc9t.md)
- [func flatMap<SegmentOfResult>((Self.Element) async -> SegmentOfResult) -> AsyncFlatMapSequence<Self, SegmentOfResult>](./flatmap%28_%29-40jd1.md)
- [func flatMap<SegmentOfResult>((Self.Element) async throws -> SegmentOfResult) -> AsyncThrowingFlatMapSequence<Self, SegmentOfResult>](./flatmap%28_%29-czyq.md)
- [func flatMapLatest<T>((Self.Element) -> T) -> some Sendable & AsyncSequence<T.Element, Self.Failure>
](./flatmaplatest%28_%29-6muxo.md)
- [func flatMapLatest<T>((Self.Element) -> T) -> some Sendable & AsyncSequence<T.Element, T.Failure>
](./flatmaplatest%28_%29-71cnj.md)
- [func flatMapLatest<T>((Self.Element) -> T) -> some Sendable & AsyncSequence<T.Element, Self.Failure>
](./flatmaplatest%28_%29-9viao.md)
- [func interspersed(every: Int, with: () -> Self.Element) -> AsyncInterspersedSequence<Self>](./interspersed%28every,with%29-2gub0.md)
- [func interspersed(every: Int, with: Self.Element) -> AsyncInterspersedSequence<Self>](./interspersed%28every,with%29-5cdoj.md)
- [func interspersed(every: Int, with: () async -> Self.Element) -> AsyncInterspersedSequence<Self>](./interspersed%28every,with%29-6kzi3.md)
- [func interspersed(every: Int, with: () throws -> Self.Element) -> AsyncThrowingInterspersedSequence<Self>](./interspersed%28every,with%29-8zo5v.md)
- [func interspersed(every: Int, with: () async throws -> Self.Element) -> AsyncThrowingInterspersedSequence<Self>](./interspersed%28every,with%29-93s8m.md)
- [func joined() -> AsyncJoinedSequence<Self>](./joined%28%29.md)
- [func joined<Separator>(separator: Separator) -> AsyncJoinedBySeparatorSequence<Self, Separator>](./joined%28separator%29.md)
- [func makeAsyncIterator() -> some AsyncIteratorProtocol<Element, Failure>
](./makeasynciterator%28%29.md)
- [func map<Transformed>((Self.Element) async -> Transformed) -> AsyncMapSequence<Self, Transformed>](./map%28_%29-34qng.md)
- [func map<Transformed>((Self.Element) async throws -> Transformed) -> AsyncThrowingMapSequence<Self, Transformed>](./map%28_%29-4qxmz.md)
- [func mapError<MappedError>((Self.Failure) -> MappedError) -> some AsyncSequence<Self.Element, MappedError>
](./maperror%28_%29-3nohp.md)
- [func mapError<MappedError>((Self.Failure) -> MappedError) -> some Sendable & AsyncSequence<Self.Element, MappedError>
](./maperror%28_%29-aonf.md)
- [func max() async rethrows -> Self.Element?](./max%28%29.md)
- [func max(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](./max%28by%29.md)
- [func min() async rethrows -> Self.Element?](./min%28%29.md)
- [func min(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](./min%28by%29.md)
- [func prefix(Int) -> AsyncPrefixSequence<Self>](./prefix%28_%29.md)
- [func prefix(while: (Self.Element) async -> Bool) rethrows -> AsyncPrefixWhileSequence<Self>](./prefix%28while%29.md)
- [func reduce<Result>(Result, (Result, Self.Element) async throws -> Result) async rethrows -> Result](./reduce%28_,_%29.md)
- [func reduce<Result>(into: Result, (inout Result, Self.Element) async throws -> Void) async rethrows -> Result](./reduce%28into,_%29.md)
- [func reductions((Self.Element, Self.Element) async -> Self.Element) -> AsyncInclusiveReductionsSequence<Self>](./reductions%28_%29.md)
- [func reductions<Result>(Result, (Result, Self.Element) async -> Result) -> AsyncExclusiveReductionsSequence<Self, Result>](./reductions%28_,_%29-4n4af.md)
- [func reductions<Result>(Result, (Result, Self.Element) async throws -> Result) -> AsyncThrowingExclusiveReductionsSequence<Self, Result>](./reductions%28_,_%29-9tcgq.md)
- [func reductions<Result>(into: Result, (inout Result, Self.Element) async -> Void) -> AsyncExclusiveReductionsSequence<Self, Result>](./reductions%28into,_%29-5edaq.md)
- [func reductions<Result>(into: Result, (inout Result, Self.Element) async throws -> Void) -> AsyncThrowingExclusiveReductionsSequence<Self, Result>](./reductions%28into,_%29-6wzij.md)
- [func removeDuplicates() -> AsyncRemoveDuplicatesSequence<Self>](./removeduplicates%28%29.md)
- [func removeDuplicates(by: (Self.Element, Self.Element) async throws -> Bool) -> AsyncThrowingRemoveDuplicatesSequence<Self>](./removeduplicates%28by%29-738at.md)
- [func removeDuplicates(by: (Self.Element, Self.Element) async -> Bool) -> AsyncRemoveDuplicatesSequence<Self>](./removeduplicates%28by%29-lt3q.md)
- [func share(bufferingPolicy: AsyncBufferSequencePolicy) -> some Sendable & AsyncSequence<Self.Element, Self.Failure>
](./share%28bufferingpolicy%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/asyncsequence-implementations)*