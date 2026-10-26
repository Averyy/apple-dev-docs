---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncremoveduplicatessequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncRemoveDuplicatesSequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence that omits repeated elements by testing them with a predicate.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
struct AsyncRemoveDuplicatesSequence<Base> where Base : AsyncSequence
```

## Topics

### Structures
- [AsyncRemoveDuplicatesSequence.Iterator](./asyncremoveduplicatessequence/iterator.md)
  The iterator for an `AsyncRemoveDuplicatesSequence` instance.
### Instance Methods
- [func makeAsyncIterator() -> AsyncRemoveDuplicatesSequence<Base>.Iterator](./asyncremoveduplicatessequence/makeasynciterator%28%29.md)
### Type Aliases
- [AsyncRemoveDuplicatesSequence.Element](./asyncremoveduplicatessequence/element.md)
### Default Implementations
- [AsyncSequence Implementations](./asyncremoveduplicatessequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncremoveduplicatessequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncremoveduplicatessequence)*