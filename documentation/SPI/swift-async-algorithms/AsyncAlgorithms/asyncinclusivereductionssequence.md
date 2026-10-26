---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncinclusivereductionssequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncInclusiveReductionsSequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence containing the accumulated results of combining the elements of the asynchronous sequence using a given closure.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct AsyncInclusiveReductionsSequence<Base> where Base : AsyncSequence
```

## Topics

### Structures
- [AsyncInclusiveReductionsSequence.Iterator](./asyncinclusivereductionssequence/iterator.md)
  The iterator for an `AsyncInclusiveReductionsSequence` instance.
### Default Implementations
- [AsyncSequence Implementations](./asyncinclusivereductionssequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncinclusivereductionssequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncinclusivereductionssequence)*