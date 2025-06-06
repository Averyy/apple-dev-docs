# LazySequenceProtocol Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var elements: LazySequence<Base>.Elements](lazysequence/elements-swift.property.md)
  The `Base` (presumably non-lazy) sequence from which `self` was created.
- [var lazy: LazySequence<Self.Elements>](lazysequence/lazy.md)
### Instance Methods
- [func compactMap<ElementOfResult>((Self.Elements.Element) -> ElementOfResult?) -> LazyMapSequence<LazyFilterSequence<LazyMapSequence<Self.Elements, ElementOfResult?>>, ElementOfResult>](lazysequence/compactmap(_:)-73i9g.md)
  Returns the non-`nil` results of mapping the given transformation over this sequence.
- [func drop(while: (Self.Elements.Element) -> Bool) -> LazyDropWhileSequence<Self.Elements>](lazysequence/drop(while:).md)
  Returns a lazy sequence that skips any initial elements that satisfy `predicate`.
- [func filter((Self.Elements.Element) -> Bool) -> LazyFilterSequence<Self.Elements>](lazysequence/filter(_:).md)
  Returns the elements of `self` that satisfy `isIncluded`.
- [func flatMap<ElementOfResult>((Self.Elements.Element) -> ElementOfResult?) -> LazyMapSequence<LazyFilterSequence<LazyMapSequence<Self.Elements, ElementOfResult?>>, ElementOfResult>](lazysequence/flatmap(_:)-102bh.md)
  Returns the non-`nil` results of mapping the given transformation over this sequence.
- [func flatMap<SegmentOfResult>((Self.Elements.Element) -> SegmentOfResult) -> LazySequence<FlattenSequence<LazyMapSequence<Self.Elements, SegmentOfResult>>>](lazysequence/flatmap(_:)-7fl2l.md)
  Returns the concatenated results of mapping the given transformation over this sequence.
- [func joined() -> LazySequence<FlattenSequence<Self.Elements>>](lazysequence/joined-2zoe4.md)
  Returns a lazy sequence that concatenates the elements of this sequence of sequences.
- [func map<U>((Self.Element) -> U) -> LazyMapSequence<Self.Elements, U>](lazysequence/map(_:)-5eh3s.md)
  Returns a `LazyMapSequence` over this `Sequence`.  The elements of the result are computed lazily, each time they are read, by calling `transform` function on a base element.
- [func prefix(while: (Self.Elements.Element) -> Bool) -> LazyPrefixWhileSequence<Self.Elements>](lazysequence/prefix(while:).md)
  Returns a lazy sequence of the initial consecutive elements that satisfy `predicate`.
### Type Aliases
- [LazySequence.Elements](lazysequence/elements-swift.typealias.md)
  A `Sequence` that can contain the same elements as this one, possibly with a simpler type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazysequence/lazysequenceprotocol-implementations)*