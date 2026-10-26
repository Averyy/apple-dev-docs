---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/chain"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# Chain

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Role**: Article

Chains two or more asynchronous sequences together sequentially.

#### Overview

[[Source](https://github.com/apple/swift-async-algorithms/blob/main/Sources/AsyncAlgorithms/AsyncChain2Sequence.swift), [Source](https://github.com/apple/swift-async-algorithms/blob/main/Sources/AsyncAlgorithms/AsyncChain3Sequence.swift) | [Tests](https://github.com/apple/swift-async-algorithms/blob/main/Tests/AsyncAlgorithmsTests/TestChain.swift)]

Chains two or more asynchronous sequences together sequentially where the elements from the resulting asynchronous sequence are comprised in order from the elements of the first asynchronous sequence and then the second (and so on) or until an error occurs.

This operation is available for all `AsyncSequence` types who share the same `Element` type.

```swift
let preamble = [
  "// Some header to add as a preamble",
  "//",
  ""
].async
let lines = chain(preamble, URL(fileURLWithPath: "/tmp/Sample.swift").lines)

for try await line in lines {
  print(line)
}
```

The above example shows how two `AsyncSequence` types can be chained together. In this case it prepends a preamble to the `lines` content of the file.

#### Detailed Design

This function family and the associated family of return types are prime candidates for variadic generics. Until that proposal is accepted, these will be implemented in terms of two- and three-base sequence cases.

```swift
public func chain<Base1: AsyncSequence, Base2: AsyncSequence>(_ s1: Base1, _ s2: Base2) -> AsyncChain2Sequence<Base1, Base2> where Base1.Element == Base2.Element

public func chain<Base1: AsyncSequence, Base2: AsyncSequence, Base3: AsyncSequence>(_ s1: Base1, _ s2: Base2, _ s3: Base3) -> AsyncChain3Sequence<Base1, Base2, Base3>

public struct AsyncChain2Sequence<Base1: AsyncSequence, Base2: AsyncSequence> where Base1.Element == Base2.Element {
  public typealias Element = Base1.Element

  public struct Iterator: AsyncIteratorProtocol {
    public mutating func next() async rethrows -> Element?
  }

  public func makeAsyncIterator() -> Iterator
}

extension AsyncChain2Sequence: Sendable where Base1: Sendable, Base2: Sendable { }
extension AsyncChain2Sequence.Iterator: Sendable where Base1.AsyncIterator: Sendable, Base2.AsyncIterator: Sendable { }

public struct AsyncChain3Sequence<Base1: AsyncSequence, Base2: AsyncSequence, Base3: AsyncSequence> where Base1.Element == Base2.Element, Base1.Element == Base3.Element {
  public typealias Element = Base1.Element

  public struct Iterator: AsyncIteratorProtocol {
    public mutating func next() async rethrows -> Element?
  }

  public func makeAsyncIterator() -> Iterator
}

extension AsyncChain3Sequence: Sendable where Base1: Sendable, Base2: Sendable, Base3: Sendable { }
extension AsyncChain3Sequence.Iterator: Sendable where Base1.AsyncIterator: Sendable, Base2.AsyncIterator: Sendable, Base3.AsyncIterator: Sendable { }
```

The `chain(_:...)` function takes two or more sequences as arguments.

The resulting `AsyncChainSequence` type is an asynchronous sequence, with conditional conformance to `Sendable` when the arguments also conform to it.

When any of the asynchronous sequences being chained together come to their end of iteration, the `AsyncChainSequence` iteration proceeds to the next asynchronous sequence. When the last asynchronous sequence reaches the end of iteration, the `AsyncChainSequence` then ends its iteration.

At any point in time, if one of the comprising asynchronous sequences throws an error during iteration, the resulting `AsyncChainSequence` iteration will throw that error and end iteration. The throwing behavior of `AsyncChainSequence` is that it will throw when any of its comprising bases throw, and will not throw when all of its comprising bases do not throw.

##### Naming

This function’s and type’s name match the term of art used in other languages and libraries.

This combinator function is a direct analog to the synchronous version [defined in the Swift Algorithms package](https://github.com/apple/swift-algorithms/blob/main/Guides/Chain.md).

## See Also

### Getting Started
- [AdjacentPairs](./adjacentpairs.md)
- [AsyncBufferedByteIterator](./bufferedbytes.md)
  Provides a highly efficient iterator useful for iterating byte sequences derived from asynchronous read functions.
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

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/chain)*