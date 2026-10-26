---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchunkedbygroupsequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncChunkedByGroupSequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An `AsyncSequence` that chunks by testing if two elements belong to the same group.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
struct AsyncChunkedByGroupSequence<Base, Collected> where Base : AsyncSequence, Collected : RangeReplaceableCollection, Base.Element == Collected.Element
```

#### Overview

Group chunks are determined by passing two consecutive elements to a closure which tests whether they are in the same group. When the `AsyncChunkedByGroupSequence` iterator receives the first element from the base sequence, it will immediately be added to a group. When it receives the second item, it tests whether the previous item and the current item belong to the same group. If they are not in the same group, then the iterator emits the first item’s group and a new group is created containing the second item. Items declared to be in the same group accumulate until a new group is declared, or the iterator finds the end of the base sequence. When the base sequence terminates, the final group is emitted. If the base sequence throws an error, `AsyncChunkedByGroupSequence` will rethrow that error immediately and discard any current group.

```
 let numbers = [10, 20, 30, 10, 40, 40, 10, 20].async
 let chunks = numbers.chunked { $0 <= $1 }
 for await numberChunk in chunks {
   print(numberChunk)
 }
 // prints
 // [10, 20, 30]
 // [10, 40, 40]
 // [10, 20]
```

## Topics

### Structures
- [AsyncChunkedByGroupSequence.Iterator](./asyncchunkedbygroupsequence/iterator.md)
  The iterator for a `AsyncChunkedByGroupSequence` instance.
### Instance Methods
- [func makeAsyncIterator() -> AsyncChunkedByGroupSequence<Base, Collected>.Iterator](./asyncchunkedbygroupsequence/makeasynciterator%28%29.md)
### Type Aliases
- [AsyncChunkedByGroupSequence.Element](./asyncchunkedbygroupsequence/element.md)
### Default Implementations
- [AsyncSequence Implementations](./asyncchunkedbygroupsequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncchunkedbygroupsequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchunkedbygroupsequence)*