# LazyPrefixWhileSequence.Iterator

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

An iterator over the initial elements traversed by a base iterator that satisfy a given predicate.

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

Available when `Base` conforms to `Sequence`.

## Overview

This is the associated iterator for the `LazyPrefixWhileSequence`, `LazyPrefixWhileCollection`, and `LazyPrefixWhileBidirectionalCollection` types.

## Topics

### Type Aliases
- [LazyPrefixWhileSequence.Iterator.Element](./iterator/element.md)
  The type of element traversed by the iterator.
### Default Implementations
- [IteratorProtocol Implementations](./iterator/iteratorprotocol-implementations.md)
- [Sequence Implementations](./iterator/sequence-implementations.md)

## Relationships

### Conforms To
- [Copyable](../copyable.md)
- [Escapable](../escapable.md)
- [IteratorProtocol](../iteratorprotocol.md)
- [Sequence](../sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazyprefixwhilesequence/iterator)*