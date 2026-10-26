---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncthrowingremoveduplicatessequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncThrowingRemoveDuplicatesSequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence that omits repeated elements by testing them with an error-throwing predicate.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
struct AsyncThrowingRemoveDuplicatesSequence<Base> where Base : AsyncSequence
```

## Topics

### Structures
- [AsyncThrowingRemoveDuplicatesSequence.Iterator](./asyncthrowingremoveduplicatessequence/iterator.md)
  The iterator for an `AsyncThrowingRemoveDuplicatesSequence` instance.
### Instance Methods
- [func makeAsyncIterator() -> AsyncThrowingRemoveDuplicatesSequence<Base>.Iterator](./asyncthrowingremoveduplicatessequence/makeasynciterator%28%29.md)
### Type Aliases
- [AsyncThrowingRemoveDuplicatesSequence.Element](./asyncthrowingremoveduplicatessequence/element.md)
### Default Implementations
- [AsyncSequence Implementations](./asyncthrowingremoveduplicatessequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncthrowingremoveduplicatessequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncthrowingremoveduplicatessequence)*