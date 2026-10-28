---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/lazy"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncSyncSequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Role**: Article

This operation is available for all `Sequence` types.

## Overview

[[Source](https://github.com/apple/swift-async-algorithms/blob/main/Sources/AsyncAlgorithms/AsyncSyncSequence.swift) | [Tests](https://github.com/apple/swift-async-algorithms/blob/main/Tests/AsyncAlgorithmsTests/TestLazy.swift)]

```swift
let numbers = [1, 2, 3, 4].async
let characters = "abcde".async
```

This transformation can be useful to test operations specifically available on `AsyncSequence` but also is useful to combine with other `AsyncSequence` types to provide well known sources of data.

## Detailed Design

The `.async` property returns an `AsyncSyncSequence` that is generic upon the base `Sequence` it was constructed from.

```swift
extension Sequence {
  public var async: AsyncSyncSequence<Self> { get }
}

public struct AsyncSyncSequence<Base: Sequence>: AsyncSequence {
  ...
}

extension AsyncSyncSequence: Sendable where Base: Sendable { }
extension AsyncSyncSequence.Iterator: Sendable where Base.Iterator: Sendable { }
```

### Naming

This property’s and type’s name match the naming approaches in the Swift standard library. The property is named with a succinct name in inspiration from `.lazy`, and the type is named in reference to the lazy behavior of the constructed `AsyncSequence`.

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
- [Effects](./effects.md)
  Lists the effects of all async algorithms.
- [Intersperse](./intersperse.md)
  Places a given value in between each element of the asynchronous sequence.
- [Joined](./joined.md)
- [Merge](./merge.md)
  Merges two or more asynchronous sequences sharing the same element type into one singular asynchronous sequence.
- [Reductions](./reductions.md)
- [RemoveDuplicates](./removeduplicates.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/lazy)*