---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncmerge3sequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncMerge3Sequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An `AsyncSequence` that takes three upstream `AsyncSequence`s and combines their elements.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
struct AsyncMerge3Sequence<Base1, Base2, Base3> where Base1 : Sendable, Base1 : AsyncSequence, Base2 : Sendable, Base2 : AsyncSequence, Base3 : Sendable, Base3 : AsyncSequence, Base1.Element : Sendable, Base1.Element == Base2.Element, Base2.Element == Base3.Element
```

## Topics

### Structures
- [AsyncMerge3Sequence.Iterator](./asyncmerge3sequence/iterator.md)
### Type Aliases
- [AsyncMerge3Sequence.Element](./asyncmerge3sequence/element.md)
### Default Implementations
- [AsyncSequence Implementations](./asyncmerge3sequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncmerge3sequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncmerge3sequence)*