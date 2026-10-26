---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncthrowinginterspersedsequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncThrowingInterspersedSequence

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
struct AsyncThrowingInterspersedSequence<Base> where Base : AsyncSequence
```

## Topics

### Structures
- [AsyncThrowingInterspersedSequence.Iterator](./asyncthrowinginterspersedsequence/iterator.md)
  The iterator for an `AsyncInterspersedSequence` asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](./asyncthrowinginterspersedsequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncthrowinginterspersedsequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncthrowinginterspersedsequence)*