---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchunksofcountorsignalsequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncChunksOfCountOrSignalSequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An `AsyncSequence` that chunks elements into collected `RangeReplaceableCollection` instances by either count or a signal from another `AsyncSequence`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
struct AsyncChunksOfCountOrSignalSequence<Base, Collected, Signal> where Base : Sendable, Base : AsyncSequence, Collected : RangeReplaceableCollection, Signal : Sendable, Signal : AsyncSequence, Base.Element : Sendable, Base.Element == Collected.Element, Signal.Element : Sendable
```

## Topics

### Structures
- [AsyncChunksOfCountOrSignalSequence.Iterator](./asyncchunksofcountorsignalsequence/iterator.md)
  The iterator for a `AsyncChunksOfCountOrSignalSequence` instance.
### Instance Methods
- [func makeAsyncIterator() -> AsyncChunksOfCountOrSignalSequence<Base, Collected, Signal>.Iterator](./asyncchunksofcountorsignalsequence/makeasynciterator%28%29.md)
### Type Aliases
- [AsyncChunksOfCountOrSignalSequence.Element](./asyncchunksofcountorsignalsequence/element.md)
### Default Implementations
- [AsyncSequence Implementations](./asyncchunksofcountorsignalsequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncchunksofcountorsignalsequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchunksofcountorsignalsequence)*