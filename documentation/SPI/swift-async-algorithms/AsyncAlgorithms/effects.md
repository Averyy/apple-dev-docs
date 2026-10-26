---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/effects"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# Effects

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Role**: Article

Lists the effects of all async algorithms.

#### Overview

| Type | Throws | Sendability |
| --- | --- | --- |
| `AsyncAdjacentPairsSequence` | rethrows | Conditional |
| `AsyncBufferedByteIterator` | throws | Not Sendable |
| `AsyncBufferSequence` | rethrows | Conditional |
| `AsyncBufferSequence.Iterator` | rethrows | Not Sendable |
| `AsyncChain2Sequence` | rethrows | Conditional |
| `AsyncChain2Sequence.Iterator` | rethrows | Not Sendable |
| `AsyncChain3Sequence` | rethrows | Conditional |
| `AsyncChain3Sequence.Iterator` | rethrows | Not Sendable |
| `AsyncChannel` | non-throwing | Sendable |
| `AsyncChannel.Iterator` | non-throwing | Not Sendable |
| `AsyncChunkedByGroupSequence` | rethrows | Conditional |
| `AsyncChunkedByGroupSequence.Iterator` | rethrows | Not Sendable |
| `AsyncChunkedOnProjectionSequence` | rethrows | Conditional |
| `AsyncChunkedOnProjectionSequence.Iterator` | rethrows | Not Sendable |
| `AsyncChunksOfCountOrSignalSequence` | rethrows | Sendable |
| `AsyncChunksOfCountOrSignalSequence.Iterator` | rethrows | Not Sendable |
| `AsyncChunksOfCountSequence` | rethrows | Conditional |
| `AsyncChunksOfCountSequence.Iterator` | rethrows | Not Sendable |
| `AsyncCombineLatest2Sequence` | rethrows | Sendable |
| `AsyncCombineLatest2Sequence.Iterator` | rethrows | Not Sendable |
| `AsyncCombineLatest3Sequence` | rethrows | Sendable |
| `AsyncCombineLatest3Sequence.Iterator` | rethrows | Not Sendable |
| `AsyncCompactedSequence` | rethrows | Conditional |
| `AsyncCompactedSequence.Iterator` | rethrows | Not Sendable |
| `AsyncDebounceSequence` | rethrows | Sendable |
| `AsyncDebounceSequence.Iterator` | rethrows | Not Sendable |
| `AsyncExclusiveReductionsSequence` | rethrows | Conditional |
| `AsyncExclusiveReductionsSequence.Iterator` | rethrows | Not Sendable |
| `AsyncInclusiveReductionsSequence` | rethrows | Conditional |
| `AsyncInclusiveReductionsSequence.Iterator` | rethrows | Not Sendable |
| `AsyncInterspersedSequence` | rethrows | Conditional |
| `AsyncInterspersedSequence.Iterator` | rethrows | Not Sendable |
| `AsyncJoinedSequence` | rethrows | Conditional |
| `AsyncJoinedSequence.Iterator` | rethrows | Not Sendable |
| `AsyncSyncSequence` | non-throwing | Conditional |
| `AsyncSyncSequence.Iterator` | non-throwing | Not Sendable |
| `AsyncLimitBuffer` | non-throwing | Sendable |
| `AsyncMerge2Sequence` | rethrows | Sendable |
| `AsyncMerge2Sequence.Iterator` | rethrows | Not Sendable |
| `AsyncMerge3Sequence` | rethrows | Sendable |
| `AsyncMerge3Sequence.Iterator` | rethrows | Not Sendable |
| `AsyncRemoveDuplicatesSequence` | rethrows | Conditional |
| `AsyncRemoveDuplicatesSequence.Iterator` | rethrows | Not Sendable |
| `AsyncThrottleSequence` | rethrows | Conditional |
| `AsyncThrottleSequence.Iterator` | rethrows | Not Sendable |
| `AsyncThrowingChannel` | throws | Sendable |
| `AsyncThrowingChannel.Iterator` | throws | Not Sendable |
| `AsyncThrowingExclusiveReductionsSequence` | throws | Conditional |
| `AsyncThrowingExclusiveReductionsSequence.Iterator` | throws | Not Sendable |
| `AsyncThrowingInclusiveReductionsSequence` | throws | Conditional |
| `AsyncThrowingInclusiveReductionsSequence.Iterator` | throws | Not Sendable |
| `AsyncTimerSequence` | non-throwing | Sendable |
| `AsyncTimerSequence.Iterator` | non-throwing | Not Sendable |
| `AsyncZip2Sequence` | rethrows | Sendable |
| `AsyncZip2Sequence.Iterator` | rethrows | Not Sendable |
| `AsyncZip3Sequence` | rethrows | Sendable |
| `AsyncZip3Sequence.Iterator` | rethrows | Not Sendable |

## See Also

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
- [Intersperse](./intersperse.md)
  Places a given value in between each element of the asynchronous sequence.
- [Joined](./joined.md)
- [AsyncSyncSequence](./lazy.md)
  This operation is available for all `Sequence` types.
- [Merge](./merge.md)
  Merges two or more asynchronous sequences sharing the same element type into one singular asynchronous sequence.
- [Reductions](./reductions.md)
- [RemoveDuplicates](./removeduplicates.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/effects)*