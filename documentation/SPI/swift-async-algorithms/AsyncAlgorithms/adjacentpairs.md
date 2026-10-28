---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/adjacentpairs"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AdjacentPairs

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Role**: Article

## Overview

- Author(s): [László Teveli](https://github.com/tevelee)

[[Source](https://github.com/apple/swift-async-algorithms/blob/main/Sources/AsyncAlgorithms/AsyncAdjacentPairsSequence.swift) | [Tests](https://github.com/apple/swift-async-algorithms/blob/main/Tests/AsyncAlgorithmsTests/TestAdjacentPairs.swift)]

The `adjacentPairs()` API serve the purpose of collecting adjacent values. This operation is available for any `AsyncSequence` by calling the `adjacentPairs()` method.

```swift
extension AsyncSequence {
  public func adjacentPairs() -> AsyncAdjacentPairsSequence<Self>
}
```

## Detailed Design

The `adjacentPairs()` algorithm produces elements of tuple (size of 2), containing a pair of the original `Element` type.

The interface for this algorithm is available on all `AsyncSequence` types. The returned `AsyncAdjacentPairsSequence` conditionally conforms to `Sendable`.

Its iterator keeps track of the previous element returned in the `next()` function and updates it in every turn.

```swift
for await (first, second) in (1...5).async.adjacentPairs() {
   print("First: \(first), Second: \(second)")
}

// First: 1, Second: 2
// First: 2, Second: 3
// First: 3, Second: 4
// First: 4, Second: 5
```

It composes well with the [Dictionary.init(_:uniquingKeysWith:)](https://github.com/apple/swift-async-algorithms/blob/main/Guides/Collections.md) API that deals with `AsyncSequence` of tuples.

```swift
Dictionary(uniqueKeysWithValues: url.lines.adjacentPairs())
```

## Alternatives Considered

This functionality is often written as a `zip` of a sequence together with itself, dropping its first element (`zip(source, source.dropFirst())`).

It’s such a dominant use-case, the [swift-algorithms](https://github.com/apple/swift-algorithms) package also [introduced](https://github.com/apple/swift-algorithms/pull/119) it to its collection of algorithms.

## Credits/Inspiration

The synchronous counterpart in [swift-algorithms](https://github.com/apple/swift-algorithms/blob/main/Guides/AdjacentPairs.md).

## See Also

### Getting Started
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


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/adjacentpairs)*