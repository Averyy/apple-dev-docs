---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynccombinelatest3sequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncCombineLatest3Sequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An `AsyncSequence` that combines the latest values produced from three asynchronous sequences into an asynchronous sequence of tuples.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
struct AsyncCombineLatest3Sequence<Base1, Base2, Base3> where Base1 : Sendable, Base1 : AsyncSequence, Base2 : Sendable, Base2 : AsyncSequence, Base3 : Sendable, Base3 : AsyncSequence, Base1.Element : Sendable, Base2.Element : Sendable, Base3.Element : Sendable
```

## Topics

### Structures
- [AsyncCombineLatest3Sequence.Iterator](./asynccombinelatest3sequence/iterator.md)
### Instance Methods
- [func makeAsyncIterator() -> AsyncCombineLatest3Sequence<Base1, Base2, Base3>.AsyncIterator](./asynccombinelatest3sequence/makeasynciterator%28%29.md)
### Type Aliases
- [AsyncCombineLatest3Sequence.AsyncIterator](./asynccombinelatest3sequence/asynciterator.md)
- [AsyncCombineLatest3Sequence.Element](./asynccombinelatest3sequence/element.md)
### Default Implementations
- [AsyncSequence Implementations](./asynccombinelatest3sequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asynccombinelatest3sequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynccombinelatest3sequence)*