---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/intersperse"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# Intersperse

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Role**: Article

Places a given value in between each element of the asynchronous sequence.

## Overview

[[Source](https://github.com/apple/swift-async-algorithms/blob/main/Sources/AsyncAlgorithms/Interspersed/AsyncInterspersedSequence.swift) | [Tests](https://github.com/apple/swift-async-algorithms/blob/main/Tests/AsyncAlgorithmsTests/Interspersed/TestInterspersed.swift)]

```swift
let numbers = [1, 2, 3].async.interspersed(with: 0)
for await number in numbers {
  print(number)
}
// prints 1 0 2 0 3

let empty = [].async.interspersed(with: 0)
// await Array(empty) == []
```

`interspersed(with:)` takes a separator value and inserts it in between every element in the asynchronous sequence.

## Detailed Design

A new method is added to `AsyncSequence`:

```swift
extension AsyncSequence {
  func interspersed(with separator: Element) -> AsyncInterspersedSequence<Self>
}
```

The new `AsyncInterspersedSequence` type represents the asynchronous sequence when the separator is inserted between each element.

When the base asynchronous sequence can throw on iteration, `AsyncInterspersedSequence` will throw on iteration. When the base does not throw, the iteration of `AsyncInterspersedSequence` does not throw either.

`AsyncInterspersedSequence` is conditionally `Sendable` when the base asynchronous sequence is `Sendable` and the element is also `Sendable`.

### Naming

This method’s and type’s name match the term of art used in other languages and libraries.

This method is a direct analog to the synchronous version [defined in the Swift Algorithms package](https://github.com/apple/swift-algorithms/blob/main/Guides/Intersperse.md).

### Comparison with other languages

**[Haskell](https://hackage.haskell.org/package/base-4.14.0.0/docs/Data-List.html#v:intersperse):** Has an `intersperse` function which takes an element and a list and ‘intersperses’ that element between the elements of the list.

**[Rust](https://docs.rs/itertools/0.9.0/itertools/trait.Itertools.html#method.intersperse):** Has a function called `intersperse` to insert a particular value between each element.

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
- [Joined](./joined.md)
- [AsyncSyncSequence](./lazy.md)
  This operation is available for all `Sequence` types.
- [Merge](./merge.md)
  Merges two or more asynchronous sequences sharing the same element type into one singular asynchronous sequence.
- [Reductions](./reductions.md)
- [RemoveDuplicates](./removeduplicates.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/intersperse)*