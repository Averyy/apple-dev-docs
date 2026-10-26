---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynccompactedsequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncCompactedSequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An `AsyncSequence` that iterates over every non-nil element from the original `AsyncSequence`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct AsyncCompactedSequence<Base, Element> where Base : AsyncSequence, Base.Element == Element?
```

## Topics

### Structures
- [AsyncCompactedSequence.Iterator](./asynccompactedsequence/iterator.md)
  The iterator for an `AsyncCompactedSequence` instance.
### Instance Methods
- [func makeAsyncIterator() -> AsyncCompactedSequence<Base, Element>.Iterator](./asynccompactedsequence/makeasynciterator%28%29.md)
### Default Implementations
- [AsyncSequence Implementations](./asynccompactedsequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asynccompactedsequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynccompactedsequence)*