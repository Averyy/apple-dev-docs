---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncthrowinginclusivereductionssequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncThrowingInclusiveReductionsSequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence containing the accumulated results of combining the elements of the asynchronous sequence using a given error-throwing closure.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct AsyncThrowingInclusiveReductionsSequence<Base> where Base : AsyncSequence
```

## Topics

### Structures
- [AsyncThrowingInclusiveReductionsSequence.Iterator](./asyncthrowinginclusivereductionssequence/iterator.md)
  The iterator for an `AsyncThrowingInclusiveReductionsSequence` instance.
### Default Implementations
- [AsyncSequence Implementations](./asyncthrowinginclusivereductionssequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncthrowinginclusivereductionssequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncthrowinginclusivereductionssequence)*