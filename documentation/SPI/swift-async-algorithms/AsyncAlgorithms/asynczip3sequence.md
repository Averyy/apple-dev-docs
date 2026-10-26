---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynczip3sequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncZip3Sequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence that concurrently awaits values from three `AsyncSequence` types and emits a tuple of the values.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
struct AsyncZip3Sequence<Base1, Base2, Base3> where Base1 : Sendable, Base1 : AsyncSequence, Base2 : Sendable, Base2 : AsyncSequence, Base3 : Sendable, Base3 : AsyncSequence, Base1.Element : Sendable, Base2.Element : Sendable, Base3.Element : Sendable
```

## Topics

### Structures
- [AsyncZip3Sequence.Iterator](./asynczip3sequence/iterator.md)
### Instance Methods
- [func makeAsyncIterator() -> AsyncZip3Sequence<Base1, Base2, Base3>.AsyncIterator](./asynczip3sequence/makeasynciterator%28%29.md)
### Type Aliases
- [AsyncZip3Sequence.AsyncIterator](./asynczip3sequence/asynciterator.md)
- [AsyncZip3Sequence.Element](./asynczip3sequence/element.md)
### Default Implementations
- [AsyncSequence Implementations](./asynczip3sequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asynczip3sequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynczip3sequence)*