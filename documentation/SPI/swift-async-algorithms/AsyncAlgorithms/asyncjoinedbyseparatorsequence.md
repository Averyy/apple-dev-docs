---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncjoinedbyseparatorsequence"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncJoinedBySeparatorSequence

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

An `AsyncSequence` that concatenates `AsyncSequence` elements with a separator.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
struct AsyncJoinedBySeparatorSequence<Base, Separator> where Base : AsyncSequence, Separator : AsyncSequence, Base.Element : AsyncSequence, Separator.Element == Base.Element.Element
```

## Topics

### Structures
- [AsyncJoinedBySeparatorSequence.Iterator](./asyncjoinedbyseparatorsequence/iterator.md)
  The iterator for an `AsyncJoinedBySeparatorSequence` instance.
### Instance Methods
- [func makeAsyncIterator() -> AsyncJoinedBySeparatorSequence<Base, Separator>.Iterator](./asyncjoinedbyseparatorsequence/makeasynciterator%28%29.md)
### Type Aliases
- [AsyncJoinedBySeparatorSequence.AsyncIterator](./asyncjoinedbyseparatorsequence/asynciterator.md)
- [AsyncJoinedBySeparatorSequence.Element](./asyncjoinedbyseparatorsequence/element.md)
### Default Implementations
- [AsyncSequence Implementations](./asyncjoinedbyseparatorsequence/asyncsequence-implementations.md)
- [AsyncSequence Implementations](./asyncjoinedbyseparatorsequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncjoinedbyseparatorsequence)*