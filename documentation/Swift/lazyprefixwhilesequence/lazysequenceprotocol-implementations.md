# LazySequenceProtocol Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var elements: Self](lazyprefixwhilesequence/elements-swift.property.md)
  Identical to `self`.
- [var lazy: Self.Elements](lazyprefixwhilesequence/lazy.md)
### Instance Methods
- [func compactMap<ElementOfResult>((Self.Elements.Element) -> ElementOfResult?) -> LazyMapSequence<LazyFilterSequence<LazyMapSequence<Self.Elements, ElementOfResult?>>, ElementOfResult>](lazyprefixwhilesequence/compactmap(_:)-2xgdq.md)
  Returns the non-`nil` results of mapping the given transformation over this sequence.
- [func drop(while: (Self.Elements.Element) -> Bool) -> LazyDropWhileSequence<Self.Elements>](lazyprefixwhilesequence/drop(while:).md)
  Returns a lazy sequence that skips any initial elements that satisfy `predicate`.
- [func filter((Self.Elements.Element) -> Bool) -> LazyFilterSequence<Self.Elements>](lazyprefixwhilesequence/filter(_:).md)
  Returns the elements of `self` that satisfy `isIncluded`.
- [func flatMap<ElementOfResult>((Self.Elements.Element) -> ElementOfResult?) -> LazyMapSequence<LazyFilterSequence<LazyMapSequence<Self.Elements, ElementOfResult?>>, ElementOfResult>](lazyprefixwhilesequence/flatmap(_:)-8pzjy.md)
  Returns the non-`nil` results of mapping the given transformation over this sequence.
- [func flatMap<SegmentOfResult>((Self.Elements.Element) -> SegmentOfResult) -> LazySequence<FlattenSequence<LazyMapSequence<Self.Elements, SegmentOfResult>>>](lazyprefixwhilesequence/flatmap(_:)-907vo.md)
  Returns the concatenated results of mapping the given transformation over this sequence.
- [func joined() -> LazySequence<FlattenSequence<Self.Elements>>](lazyprefixwhilesequence/joined-h5vc.md)
  Returns a lazy sequence that concatenates the elements of this sequence of sequences.
- [func map<U>((Self.Element) -> U) -> LazyMapSequence<Self.Elements, U>](lazyprefixwhilesequence/map(_:)-24l6d.md)
  Returns a `LazyMapSequence` over this `Sequence`.  The elements of the result are computed lazily, each time they are read, by calling `transform` function on a base element.
- [func prefix(while: (Self.Elements.Element) -> Bool) -> LazyPrefixWhileSequence<Self.Elements>](lazyprefixwhilesequence/prefix(while:).md)
  Returns a lazy sequence of the initial consecutive elements that satisfy `predicate`.
### Type Aliases
- [LazyPrefixWhileSequence.Elements](lazyprefixwhilesequence/elements.md)
  A `Sequence` that can contain the same elements as this one, possibly with a simpler type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazyprefixwhilesequence/lazysequenceprotocol-implementations)*