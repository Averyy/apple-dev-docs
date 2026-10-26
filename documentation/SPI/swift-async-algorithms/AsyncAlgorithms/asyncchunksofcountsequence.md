---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchunksofcountsequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncChunksOfCountSequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An `AsyncSequence` that chunks elements into `RangeReplaceableCollection` instances of at least a given count.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
struct AsyncChunksOfCountSequence<Base, Collected> where Base : AsyncSequence, Collected : RangeReplaceableCollection, Base.Element == Collected.Element
```

## Topics

### Structures
- [AsyncChunksOfCountSequence.Iterator](./asyncchunksofcountsequence/iterator.md)
  The iterator for a `AsyncChunksOfCountSequence` instance.
### Instance Methods
- [func makeAsyncIterator() -> AsyncChunksOfCountSequence<Base, Collected>.Iterator](./asyncchunksofcountsequence/makeasynciterator%28%29.md)
### Type Aliases
- [AsyncChunksOfCountSequence.Element](./asyncchunksofcountsequence/element.md)
### Default Implementations
- [AsyncSequence Implementations](./asyncchunksofcountsequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncchunksofcountsequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchunksofcountsequence)*