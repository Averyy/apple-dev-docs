---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncadjacentpairssequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncAdjacentPairsSequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An `AsyncSequence` that iterates over the adjacent pairs of the original `AsyncSequence`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct AsyncAdjacentPairsSequence<Base> where Base : AsyncSequence
```

## Topics

### Structures
- [AsyncAdjacentPairsSequence.Iterator](./asyncadjacentpairssequence/iterator.md)
  The iterator for an `AsyncAdjacentPairsSequence` instance.
### Instance Methods
- [func makeAsyncIterator() -> AsyncAdjacentPairsSequence<Base>.Iterator](./asyncadjacentpairssequence/makeasynciterator%28%29.md)
### Type Aliases
- [AsyncAdjacentPairsSequence.Element](./asyncadjacentpairssequence/element.md)
### Default Implementations
- [AsyncSequence Implementations](./asyncadjacentpairssequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncadjacentpairssequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncadjacentpairssequence)*