---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchain3sequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncChain3Sequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

A concatenation of three asynchronous sequences with the same element type.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct AsyncChain3Sequence<Base1, Base2, Base3> where Base1 : AsyncSequence, Base2 : AsyncSequence, Base3 : AsyncSequence, Base1.Element == Base2.Element, Base2.Element == Base3.Element
```

## Topics

### Structures
- [AsyncChain3Sequence.Iterator](./asyncchain3sequence/iterator.md)
  The iterator for a `AsyncChain3Sequence` instance.
### Default Implementations
- [AsyncSequence Implementations](./asyncchain3sequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncchain3sequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchain3sequence)*