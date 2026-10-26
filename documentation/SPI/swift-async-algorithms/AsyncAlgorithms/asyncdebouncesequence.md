---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncdebouncesequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncDebounceSequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An `AsyncSequence` that emits the latest element after a given quiescence period has elapsed.

**Availability**:
- iOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
struct AsyncDebounceSequence<Base, C> where Base : Sendable, Base : AsyncSequence, C : Clock, Base.Element : Sendable
```

## Topics

### Structures
- [AsyncDebounceSequence.Iterator](./asyncdebouncesequence/iterator.md)
### Default Implementations
- [AsyncSequence Implementations](./asyncdebouncesequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncdebouncesequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncdebouncesequence)*