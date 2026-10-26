---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/compacted"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# Compacted

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Role**: Article

#### Overview

- Author(s): [Philippe Hausler](https://github.com/phausler)

[ [Source](https://github.com/apple/swift-async-algorithms/blob/main/Sources/AsyncAlgorithms/AsyncCompactedSequence.swift) | [Tests](https://github.com/apple/swift-async-algorithms/blob/main/Tests/AsyncAlgorithmsTests/TestCompacted.swift) ]

#### Introduction

Just as it is common for `Sequence` types that contain optional values to need to `.compactMap { $0 }`, `AsyncSequence` types have the same use cases. This common task means that the type must employ a closure to test the optional value. This can be done more efficiently for both execution performance as well as API efficiency of typing.

#### Proposed Solution

Similar to the Swift Algorithms package we propose that a new method be added to `AsyncSequence` to fit this need.

```swift
extension AsyncSequence {
  public func compacted<Unwrapped>() -> AsyncCompactedSequence<Self, Unwrapped>
    where Element == Unwrapped?
}
```

This is equivalent to writing `.compactMap { $0 }` from a behavioral standpoint but is easier to reason about and is more efficient since it does not need to execute or store a closure.

#### Detailed Design

The `AsyncCompactedSequence` type from an effects standpoint works just like `AsyncCompactMapSequence`. When the base asynchronous sequence throws, the iteration of `AsyncCompactedSequence` can throw. Likewise if the base does not throw then the iteration of `AsyncCompactedSequence` does not throw. This type is conditionally `Sendable` when the base, base element, and base iterator are `Sendable.

```swift
public struct AsyncCompactedSequence<Base: AsyncSequence, Element>: AsyncSequence
  where Base.Element == Element? {

  public struct Iterator: AsyncIteratorProtocol {
    public mutating func next() async rethrows -> Element?
  }

  public func makeAsyncIterator() -> Iterator {
    Iterator(base.makeAsyncIterator())
  }
}

extension AsyncCompactedSequence: Sendable 
  where 
    Base: Sendable, Base.Element: Sendable, 
    Base.AsyncIterator: Sendable { }
  
extension AsyncCompactedSequence.Iterator: Sendable 
  where 
    Base: Sendable, Base.Element: Sendable, 
    Base.AsyncIterator: Sendable { }
```

#### Credits/Inspiration

This transformation function is a direct analog to the synchronous version [defined in the Swift Algorithms package](https://github.com/apple/swift-algorithms/blob/main/Guides/Compacted.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/compacted)*