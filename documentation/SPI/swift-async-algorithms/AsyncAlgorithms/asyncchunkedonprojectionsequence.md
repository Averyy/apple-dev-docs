---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchunkedonprojectionsequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncChunkedOnProjectionSequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An `AsyncSequence` that chunks on a subject when it differs from the last element.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
struct AsyncChunkedOnProjectionSequence<Base, Subject, Collected> where Base : AsyncSequence, Subject : Equatable, Collected : RangeReplaceableCollection, Base.Element == Collected.Element
```

## Topics

### Structures
- [AsyncChunkedOnProjectionSequence.Iterator](./asyncchunkedonprojectionsequence/iterator.md)
  The iterator for a `AsyncChunkedOnProjectionSequence` instance.
### Instance Methods
- [func makeAsyncIterator() -> AsyncChunkedOnProjectionSequence<Base, Subject, Collected>.Iterator](./asyncchunkedonprojectionsequence/makeasynciterator%28%29.md)
### Type Aliases
- [AsyncChunkedOnProjectionSequence.Element](./asyncchunkedonprojectionsequence/element.md)
### Default Implementations
- [AsyncSequence Implementations](./asyncchunkedonprojectionsequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncchunkedonprojectionsequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchunkedonprojectionsequence)*