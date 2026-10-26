---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchain2sequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncChain2Sequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

A concatenation of two asynchronous sequences with the same element type.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct AsyncChain2Sequence<Base1, Base2> where Base1 : AsyncSequence, Base2 : AsyncSequence, Base1.Element == Base2.Element
```

## Topics

### Structures
- [AsyncChain2Sequence.Iterator](./asyncchain2sequence/iterator.md)
  The iterator for a `AsyncChain2Sequence` instance.
### Default Implementations
- [AsyncSequence Implementations](./asyncchain2sequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncchain2sequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchain2sequence)*