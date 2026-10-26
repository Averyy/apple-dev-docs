---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncmerge2sequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncMerge2Sequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An `AsyncSequence` that takes two upstream `AsyncSequence`s and combines their elements.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
struct AsyncMerge2Sequence<Base1, Base2> where Base1 : Sendable, Base1 : AsyncSequence, Base2 : Sendable, Base2 : AsyncSequence, Base1.Element : Sendable, Base1.Element == Base2.Element
```

## Topics

### Structures
- [AsyncMerge2Sequence.Iterator](./asyncmerge2sequence/iterator.md)
### Type Aliases
- [AsyncMerge2Sequence.Element](./asyncmerge2sequence/element.md)
### Default Implementations
- [AsyncSequence Implementations](./asyncmerge2sequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncmerge2sequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncmerge2sequence)*