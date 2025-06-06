# LazyMapSequence

**Framework**: Swift  
**Kind**: struct

A `Sequence` whose elements consist of those in a `Base` `Sequence` passed through a transform function returning `Element`. These elements are computed lazily, each time they’re read, by calling the transform function on a base element.

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
struct LazyMapSequence<Base, Element> where Base : Sequence
```

## Topics

### Instance Methods
- [func map<ElementOfResult>((Element) -> ElementOfResult) -> LazyMapSequence<Base, ElementOfResult>](lazymapsequence/map(_:)-2qa3r.md)
- [func map<ElementOfResult>((Element) -> ElementOfResult) -> LazyMapCollection<Base, ElementOfResult>](lazymapsequence/map(_:)-50gkd.md)
### Type Aliases
- [LazyMapSequence.Elements](lazymapsequence/elements.md)
  A `Sequence` that can contain the same elements as this one, possibly with a simpler type.
### Default Implementations
- [BidirectionalCollection Implementations](lazymapsequence/bidirectionalcollection-implementations.md)
- [Collection Implementations](lazymapsequence/collection-implementations.md)
- [LazySequenceProtocol Implementations](lazymapsequence/lazysequenceprotocol-implementations.md)
- [RandomAccessCollection Implementations](lazymapsequence/randomaccesscollection-implementations.md)
- [Sequence Implementations](lazymapsequence/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](bidirectionalcollection.md)
- [Collection](collection.md)
- [Copyable](copyable.md)
- [LazyCollectionProtocol](lazycollectionprotocol.md)
- [LazySequenceProtocol](lazysequenceprotocol.md)
- [RandomAccessCollection](randomaccesscollection.md)
- [Sequence](sequence.md)

## See Also

- [struct LazySequence](lazysequence.md)
  A sequence containing the same elements as a `Base` sequence, but on which some operations such as `map` and `filter` are implemented lazily.
- [struct LazyFilterSequence](lazyfiltersequence.md)
  A sequence whose elements consist of the elements of some base sequence that also satisfy a given predicate.
- [struct LazyPrefixWhileSequence](lazyprefixwhilesequence.md)
  A sequence whose elements consist of the initial consecutive elements of some base sequence that satisfy a given predicate.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazymapsequence)*