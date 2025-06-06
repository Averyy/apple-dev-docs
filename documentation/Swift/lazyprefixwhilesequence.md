# LazyPrefixWhileSequence

**Framework**: Swift  
**Kind**: struct

A sequence whose elements consist of the initial consecutive elements of some base sequence that satisfy a given predicate.

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
struct LazyPrefixWhileSequence<Base> where Base : Sequence
```

#### Overview

> **Note**: When `LazyPrefixWhileSequence` wraps a collection type, the performance of accessing `endIndex` depends on how many elements satisfy the predicate at the start of the collection, and might not offer the usual performance given by the `Collection` protocol. Accessing `endIndex`, the `last` property, or calling methods that depend on moving indices might not have the documented complexity.

When `LazyPrefixWhileSequence` wraps a collection type, the performance of accessing `endIndex` depends on how many elements satisfy the predicate at the start of the collection, and might not offer the usual performance given by the `Collection` protocol. Accessing `endIndex`, the `last` property, or calling methods that depend on moving indices might not have the documented complexity.

## Topics

### Type Aliases
- [LazyPrefixWhileSequence.Element](lazyprefixwhilesequence/element.md)
  A type representing the sequence’s elements.
### Default Implementations
- [BidirectionalCollection Implementations](lazyprefixwhilesequence/bidirectionalcollection-implementations.md)
- [Collection Implementations](lazyprefixwhilesequence/collection-implementations.md)
- [LazySequenceProtocol Implementations](lazyprefixwhilesequence/lazysequenceprotocol-implementations.md)
- [Sequence Implementations](lazyprefixwhilesequence/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](bidirectionalcollection.md)
- [Collection](collection.md)
- [Copyable](copyable.md)
- [LazyCollectionProtocol](lazycollectionprotocol.md)
- [LazySequenceProtocol](lazysequenceprotocol.md)
- [Sequence](sequence.md)

## See Also

- [struct LazySequence](lazysequence.md)
  A sequence containing the same elements as a `Base` sequence, but on which some operations such as `map` and `filter` are implemented lazily.
- [struct LazyMapSequence](lazymapsequence.md)
  A `Sequence` whose elements consist of those in a `Base` `Sequence` passed through a transform function returning `Element`. These elements are computed lazily, each time they’re read, by calling the transform function on a base element.
- [struct LazyFilterSequence](lazyfiltersequence.md)
  A sequence whose elements consist of the elements of some base sequence that also satisfy a given predicate.
- [struct LazyDropWhileSequence](lazydropwhilesequence.md)
  A sequence whose elements consist of the elements that follow the initial consecutive elements of some base sequence that satisfy a given predicate.
- [typealias LazyCollection](lazycollection.md)
  A collection containing the same elements as a `Base` collection, but on which some operations such as `map` and `filter` are implemented lazily.
- [typealias LazyDropWhileCollection](lazydropwhilecollection.md)
  A lazy wrapper that includes the elements of an underlying collection after any initial consecutive elements that satisfy a predicate.
- [typealias LazyFilterCollection](lazyfiltercollection.md)
  A lazy `Collection` wrapper that includes the elements of an underlying collection that satisfy a predicate.
- [typealias LazyMapCollection](lazymapcollection.md)
  A `Collection` whose elements consist of those in a `Base` `Collection` passed through a transform function returning `Element`. These elements are computed lazily, each time they’re read, by calling the transform function on a base element.
- [typealias LazyPrefixWhileCollection](lazyprefixwhilecollection.md)
  A lazy collection wrapper that includes the initial consecutive elements of an underlying collection that satisfy a predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazyprefixwhilesequence)*