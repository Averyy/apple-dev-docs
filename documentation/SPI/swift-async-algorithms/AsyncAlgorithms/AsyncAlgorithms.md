---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncAlgorithms

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: module  
**Role**: Framework

**Swift Async Algorithms** is an open-source package of asynchronous sequence and advanced algorithms that involve concurrency, along with their related types.

#### Overview

This package has three main goals:

- First-class integration with `async/await`
- Provide a home for time-based algorithms
- Be cross-platform and open source

## Topics

### Getting Started
- [AdjacentPairs](./adjacentpairs.md)
- [AsyncBufferedByteIterator](./bufferedbytes.md)
  Provides a highly efficient iterator useful for iterating byte sequences derived from asynchronous read functions.
- [Chain](./chain.md)
  Chains two or more asynchronous sequences together sequentially.
- [Channel](./channel.md)
- [Chunked](./chunked.md)
- [Collection Initializers](./collections.md)
- [Combine Latest](./combinelatest.md)
  Combines the latest values produced from two or more asynchronous sequences into an asynchronous sequence of tuples.
- [Compacted](./compacted.md)
- [Debounce](./debounce.md)
- [Effects](./effects.md)
  Lists the effects of all async algorithms.
- [Intersperse](./intersperse.md)
  Places a given value in between each element of the asynchronous sequence.
- [Joined](./joined.md)
- [AsyncSyncSequence](./lazy.md)
  This operation is available for all `Sequence` types.
- [Merge](./merge.md)
  Merges two or more asynchronous sequences sharing the same element type into one singular asynchronous sequence.
- [Reductions](./reductions.md)
- [RemoveDuplicates](./removeduplicates.md)
- [Share](./share.md)
- [Throttle](./throttle.md)
- [Timer](./timer.md)
- [Zip](./zip.md)
  Combines the latest values produced from two or more asynchronous sequences into an asynchronous sequence of tuples.
### Articles
- [FlatMapLatest](./flatmaplatest.md)
### Classes
- [class AsyncChannel](./asyncchannel.md)
  A channel for sending elements from one task to another with back pressure.
- [class AsyncThrowingChannel](./asyncthrowingchannel.md)
  An error-throwing channel for sending elements from on task to another with back pressure.
### Structures
- [struct AsyncAdjacentPairsSequence](./asyncadjacentpairssequence.md)
  An `AsyncSequence` that iterates over the adjacent pairs of the original `AsyncSequence`.
- [struct AsyncBufferSequence](./asyncbuffersequence.md)
  An `AsyncSequence` that buffers elements in regard to a policy.
- [struct AsyncBufferSequencePolicy](./asyncbuffersequencepolicy.md)
  A policy dictating the buffering behaviour of an [`AsyncBufferSequence`](./asyncbuffersequence.md)
- [struct AsyncBufferedByteIterator](./asyncbufferedbyteiterator.md)
  An `AsyncIterator` that provides a convenient and high-performance implementation of a common architecture for `AsyncSequence` of `UInt8`, otherwise known as byte streams.
- [struct AsyncChain2Sequence](./asyncchain2sequence.md)
  A concatenation of two asynchronous sequences with the same element type.
- [struct AsyncChain3Sequence](./asyncchain3sequence.md)
  A concatenation of three asynchronous sequences with the same element type.
- [struct AsyncChunkedByGroupSequence](./asyncchunkedbygroupsequence.md)
  An `AsyncSequence` that chunks by testing if two elements belong to the same group.
- [struct AsyncChunkedOnProjectionSequence](./asyncchunkedonprojectionsequence.md)
  An `AsyncSequence` that chunks on a subject when it differs from the last element.
- [struct AsyncChunksOfCountOrSignalSequence](./asyncchunksofcountorsignalsequence.md)
  An `AsyncSequence` that chunks elements into collected `RangeReplaceableCollection` instances by either count or a signal from another `AsyncSequence`.
- [struct AsyncChunksOfCountSequence](./asyncchunksofcountsequence.md)
  An `AsyncSequence` that chunks elements into `RangeReplaceableCollection` instances of at least a given count.
- [struct AsyncCombineLatest2Sequence](./asynccombinelatest2sequence.md)
  An `AsyncSequence` that combines the latest values produced from two asynchronous sequences into an asynchronous sequence of tuples.
- [struct AsyncCombineLatest3Sequence](./asynccombinelatest3sequence.md)
  An `AsyncSequence` that combines the latest values produced from three asynchronous sequences into an asynchronous sequence of tuples.
- [struct AsyncCompactedSequence](./asynccompactedsequence.md)
  An `AsyncSequence` that iterates over every non-nil element from the original `AsyncSequence`.
- [struct AsyncDebounceSequence](./asyncdebouncesequence.md)
  An `AsyncSequence` that emits the latest element after a given quiescence period has elapsed.
- [struct AsyncExclusiveReductionsSequence](./asyncexclusivereductionssequence.md)
  An asynchronous sequence of applying a transform to the element of an asynchronous sequence and the previously transformed result.
- [struct AsyncInclusiveReductionsSequence](./asyncinclusivereductionssequence.md)
  An asynchronous sequence containing the accumulated results of combining the elements of the asynchronous sequence using a given closure.
- [struct AsyncInterspersedSequence](./asyncinterspersedsequence.md)
  An asynchronous sequence that presents the elements of a base asynchronous sequence of elements with a separator between each of those elements.
- [struct AsyncJoinedBySeparatorSequence](./asyncjoinedbyseparatorsequence.md)
  An `AsyncSequence` that concatenates `AsyncSequence` elements with a separator.
- [struct AsyncJoinedSequence](./asyncjoinedsequence.md)
  An `AsyncSequence` that concatenates`AsyncSequence` elements
- [struct AsyncMerge2Sequence](./asyncmerge2sequence.md)
  An `AsyncSequence` that takes two upstream `AsyncSequence`s and combines their elements.
- [struct AsyncMerge3Sequence](./asyncmerge3sequence.md)
  An `AsyncSequence` that takes three upstream `AsyncSequence`s and combines their elements.
- [struct AsyncRemoveDuplicatesSequence](./asyncremoveduplicatessequence.md)
  An asynchronous sequence that omits repeated elements by testing them with a predicate.
- [struct AsyncSyncSequence](./asyncsyncsequence.md)
  An asynchronous sequence composed from a synchronous sequence.
- [struct AsyncThrowingExclusiveReductionsSequence](./asyncthrowingexclusivereductionssequence.md)
  An asynchronous sequence of applying an error-throwing transform to the element of an asynchronous sequence and the previously transformed result.
- [struct AsyncThrowingInclusiveReductionsSequence](./asyncthrowinginclusivereductionssequence.md)
  An asynchronous sequence containing the accumulated results of combining the elements of the asynchronous sequence using a given error-throwing closure.
- [struct AsyncThrowingInterspersedSequence](./asyncthrowinginterspersedsequence.md)
  An asynchronous sequence that presents the elements of a base asynchronous sequence of elements with a separator between each of those elements.
- [struct AsyncThrowingRemoveDuplicatesSequence](./asyncthrowingremoveduplicatessequence.md)
  An asynchronous sequence that omits repeated elements by testing them with an error-throwing predicate.
- [struct AsyncTimerSequence](./asynctimersequence.md)
  An `AsyncSequence` that produces elements at regular intervals.
- [struct AsyncZip2Sequence](./asynczip2sequence.md)
  An asynchronous sequence that concurrently awaits values from two `AsyncSequence` types and emits a tuple of the values.
- [struct AsyncZip3Sequence](./asynczip3sequence.md)
  An asynchronous sequence that concurrently awaits values from three `AsyncSequence` types and emits a tuple of the values.
- [struct MultiProducerSingleConsumerAsyncChannel](./multiproducersingleconsumerasyncchannel.md)
  A multi-producer single-consumer channel.
- [struct MultiProducerSingleConsumerAsyncChannelAlreadyFinishedError](./multiproducersingleconsumerasyncchannelalreadyfinishederror.md)
  An error that is thrown from the various `send` methods of the [`MultiProducerSingleConsumerAsyncChannel.Source`](./multiproducersingleconsumerasyncchannel/source.md).
### Functions
- [func chain<Base1, Base2>(Base1, Base2) -> AsyncChain2Sequence<Base1, Base2>](./chain%28_,_%29.md)
  Returns a new asynchronous sequence that iterates over the two given asynchronous sequences, one followed by the other.
- [func chain<Base1, Base2, Base3>(Base1, Base2, Base3) -> AsyncChain3Sequence<Base1, Base2, Base3>](./chain%28_,_,_%29.md)
  Returns a new asynchronous sequence that iterates over the three given asynchronous sequences, one followed by the other.
- [func combineLatest<Base1, Base2>(Base1, Base2) -> AsyncCombineLatest2Sequence<Base1, Base2>](./combinelatest%28_,_%29.md)
  Creates an asynchronous sequence that combines the latest values from two `AsyncSequence` types by emitting a tuple of the values. [`combineLatest(_:_:)`](./combinelatest%28_,_%29.md) only emits a value whenever any of the base `AsyncSequence`s emit a value (so long as each of the bases have emitted at least one value).
- [func combineLatest<Base1, Base2, Base3>(Base1, Base2, Base3) -> AsyncCombineLatest3Sequence<Base1, Base2, Base3>](./combinelatest%28_,_,_%29.md)
  Creates an asynchronous sequence that combines the latest values from three `AsyncSequence` types by emitting a tuple of the values. [`combineLatest(_:_:_:)`](./combinelatest%28_,_,_%29.md) only emits a value whenever any of the base `AsyncSequence`s emit a value (so long as each of the bases have emitted at least one value).
- [func merge<Base1, Base2>(Base1, Base2) -> AsyncMerge2Sequence<Base1, Base2>](./merge%28_,_%29.md)
  Creates an asynchronous sequence of elements from two underlying asynchronous sequences
- [func merge<Base1, Base2, Base3>(Base1, Base2, Base3) -> AsyncMerge3Sequence<Base1, Base2, Base3>](./merge%28_,_,_%29.md)
  Creates an asynchronous sequence of elements from two underlying asynchronous sequences
- [func zip<Base1, Base2>(Base1, Base2) -> AsyncZip2Sequence<Base1, Base2>](./zip%28_,_%29.md)
  Creates an asynchronous sequence that concurrently awaits values from two `AsyncSequence` types and emits a tuple of the values.
- [func zip<Base1, Base2, Base3>(Base1, Base2, Base3) -> AsyncZip3Sequence<Base1, Base2, Base3>](./zip%28_,_,_%29.md)
  Creates an asynchronous sequence that concurrently awaits values from three `AsyncSequence` types and emits a tuple of the values.
### Extended Modules
- [Swift](./swift.md)
- [_Concurrency](./_concurrency.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms)*