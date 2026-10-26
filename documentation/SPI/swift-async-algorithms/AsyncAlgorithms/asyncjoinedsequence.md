---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncjoinedsequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncJoinedSequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An `AsyncSequence` that concatenates`AsyncSequence` elements

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct AsyncJoinedSequence<Base> where Base : AsyncSequence, Base.Element : AsyncSequence
```

## Topics

### Structures
- [AsyncJoinedSequence.Iterator](./asyncjoinedsequence/iterator.md)
  The iterator for an `AsyncJoinedSequence` instance.
### Instance Methods
- [func makeAsyncIterator() -> AsyncJoinedSequence<Base>.Iterator](./asyncjoinedsequence/makeasynciterator%28%29.md)
### Type Aliases
- [AsyncJoinedSequence.AsyncIterator](./asyncjoinedsequence/asynciterator.md)
- [AsyncJoinedSequence.Element](./asyncjoinedsequence/element.md)
### Default Implementations
- [AsyncSequence Implementations](./asyncjoinedsequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncjoinedsequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncjoinedsequence)*