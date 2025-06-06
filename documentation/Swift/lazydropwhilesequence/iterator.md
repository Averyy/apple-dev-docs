# LazyDropWhileSequence.Iterator

**Framework**: Swift  
**Kind**: struct

An iterator over the elements traversed by a base iterator that follow the initial consecutive elements that satisfy a given predicate.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@frozen
struct Iterator
```

#### Overview

This is the associated iterator for the `LazyDropWhileSequence`, `LazyDropWhileCollection`, and `LazyDropWhileBidirectionalCollection` types.

## Topics

### Type Aliases
- [LazyDropWhileSequence.Iterator.Element](lazydropwhilesequence/iterator/element.md)
  The type of element traversed by the iterator.
### Default Implementations
- [IteratorProtocol Implementations](lazydropwhilesequence/iterator/iteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [IteratorProtocol](iteratorprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazydropwhilesequence/iterator)*