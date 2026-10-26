---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncexclusivereductionssequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncExclusiveReductionsSequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence of applying a transform to the element of an asynchronous sequence and the previously transformed result.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct AsyncExclusiveReductionsSequence<Base, Element> where Base : AsyncSequence
```

## Topics

### Structures
- [AsyncExclusiveReductionsSequence.Iterator](./asyncexclusivereductionssequence/iterator.md)
  The iterator for an `AsyncExclusiveReductionsSequence` instance.
### Default Implementations
- [AsyncSequence Implementations](./asyncexclusivereductionssequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncexclusivereductionssequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncexclusivereductionssequence)*