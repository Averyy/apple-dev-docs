# LazySequenceProtocol Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var elements: Self](reversedcollection/elements-swift.property.md)
  Identical to `self`.
### Instance Methods
- [func compactMap<ElementOfResult>((Self.Elements.Element) -> ElementOfResult?) -> LazyMapSequence<LazyFilterSequence<LazyMapSequence<Self.Elements, ElementOfResult?>>, ElementOfResult>](reversedcollection/compactmap(_:)-45kvo.md)
  Returns the non-`nil` results of mapping the given transformation over this sequence.
- [func flatMap<SegmentOfResult>((Self.Elements.Element) -> SegmentOfResult) -> LazySequence<FlattenSequence<LazyMapSequence<Self.Elements, SegmentOfResult>>>](reversedcollection/flatmap(_:)-4wxgx.md)
  Returns the concatenated results of mapping the given transformation over this sequence.
- [func flatMap<ElementOfResult>((Self.Elements.Element) -> ElementOfResult?) -> LazyMapSequence<LazyFilterSequence<LazyMapSequence<Self.Elements, ElementOfResult?>>, ElementOfResult>](reversedcollection/flatmap(_:)-81zng.md)
  Returns the non-`nil` results of mapping the given transformation over this sequence.
- [func joined() -> LazySequence<FlattenSequence<Self.Elements>>](reversedcollection/joined-2x3z5.md)
  Returns a lazy sequence that concatenates the elements of this sequence of sequences.
- [func map<U>((Self.Element) -> U) -> LazyMapSequence<Self.Elements, U>](reversedcollection/map(_:)-88nu3.md)
  Returns a `LazyMapSequence` over this `Sequence`.  The elements of the result are computed lazily, each time they are read, by calling `transform` function on a base element.
### Type Aliases
- [ReversedCollection.Elements](reversedcollection/elements.md)
  A `Sequence` that can contain the same elements as this one, possibly with a simpler type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/reversedcollection/lazysequenceprotocol-implementations)*