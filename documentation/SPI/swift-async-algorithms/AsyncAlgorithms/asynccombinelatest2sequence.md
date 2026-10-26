---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynccombinelatest2sequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncCombineLatest2Sequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An `AsyncSequence` that combines the latest values produced from two asynchronous sequences into an asynchronous sequence of tuples.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
struct AsyncCombineLatest2Sequence<Base1, Base2> where Base1 : Sendable, Base1 : AsyncSequence, Base2 : Sendable, Base2 : AsyncSequence, Base1.Element : Sendable, Base2.Element : Sendable
```

## Topics

### Structures
- [AsyncCombineLatest2Sequence.Iterator](./asynccombinelatest2sequence/iterator.md)
### Instance Methods
- [func makeAsyncIterator() -> AsyncCombineLatest2Sequence<Base1, Base2>.AsyncIterator](./asynccombinelatest2sequence/makeasynciterator%28%29.md)
### Type Aliases
- [AsyncCombineLatest2Sequence.AsyncIterator](./asynccombinelatest2sequence/asynciterator.md)
- [AsyncCombineLatest2Sequence.Element](./asynccombinelatest2sequence/element.md)
### Default Implementations
- [AsyncSequence Implementations](./asynccombinelatest2sequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asynccombinelatest2sequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynccombinelatest2sequence)*