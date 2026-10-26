---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncinterspersedsequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncInterspersedSequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence that presents the elements of a base asynchronous sequence of elements with a separator between each of those elements.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
struct AsyncInterspersedSequence<Base> where Base : AsyncSequence
```

## Topics

### Structures
- [AsyncInterspersedSequence.Iterator](./asyncinterspersedsequence/iterator.md)
  The iterator for an `AsyncInterspersedSequence` asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](./asyncinterspersedsequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncinterspersedsequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncinterspersedsequence)*