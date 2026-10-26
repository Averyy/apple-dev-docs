---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncthrowingexclusivereductionssequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncThrowingExclusiveReductionsSequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence of applying an error-throwing transform to the element of an asynchronous sequence and the previously transformed result.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct AsyncThrowingExclusiveReductionsSequence<Base, Element> where Base : AsyncSequence
```

## Topics

### Structures
- [AsyncThrowingExclusiveReductionsSequence.Iterator](./asyncthrowingexclusivereductionssequence/iterator.md)
  The iterator for an `AsyncThrowingExclusiveReductionsSequence` instance.
### Default Implementations
- [AsyncSequence Implementations](./asyncthrowingexclusivereductionssequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncthrowingexclusivereductionssequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncthrowingexclusivereductionssequence)*