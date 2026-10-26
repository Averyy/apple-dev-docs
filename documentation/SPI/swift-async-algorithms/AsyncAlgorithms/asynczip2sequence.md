---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynczip2sequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncZip2Sequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence that concurrently awaits values from two `AsyncSequence` types and emits a tuple of the values.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
struct AsyncZip2Sequence<Base1, Base2> where Base1 : Sendable, Base1 : AsyncSequence, Base2 : Sendable, Base2 : AsyncSequence, Base1.Element : Sendable, Base2.Element : Sendable
```

## Topics

### Structures
- [AsyncZip2Sequence.Iterator](./asynczip2sequence/iterator.md)
### Instance Methods
- [func makeAsyncIterator() -> AsyncZip2Sequence<Base1, Base2>.AsyncIterator](./asynczip2sequence/makeasynciterator%28%29.md)
### Type Aliases
- [AsyncZip2Sequence.AsyncIterator](./asynczip2sequence/asynciterator.md)
- [AsyncZip2Sequence.Element](./asynczip2sequence/element.md)
### Default Implementations
- [AsyncSequence Implementations](./asynczip2sequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asynczip2sequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynczip2sequence)*