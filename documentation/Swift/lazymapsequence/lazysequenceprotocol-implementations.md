# LazySequenceProtocol Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var elements: Self](lazymapsequence/elements-swift.property.md)
  Identical to `self`.
- [var lazy: Self.Elements](lazymapsequence/lazy.md)
### Instance Methods
- [func compactMap<ElementOfResult>((Self.Elements.Element) -> ElementOfResult?) -> LazyMapSequence<LazyFilterSequence<LazyMapSequence<Self.Elements, ElementOfResult?>>, ElementOfResult>](lazymapsequence/compactmap(_:)-9pvcf.md)
  Returns the non-`nil` results of mapping the given transformation over this sequence.
- [func drop(while: (Self.Elements.Element) -> Bool) -> LazyDropWhileSequence<Self.Elements>](lazymapsequence/drop(while:).md)
  Returns a lazy sequence that skips any initial elements that satisfy `predicate`.
- [func filter((Self.Elements.Element) -> Bool) -> LazyFilterSequence<Self.Elements>](lazymapsequence/filter(_:).md)
  Returns the elements of `self` that satisfy `isIncluded`.
- [func flatMap<ElementOfResult>((Self.Elements.Element) -> ElementOfResult?) -> LazyMapSequence<LazyFilterSequence<LazyMapSequence<Self.Elements, ElementOfResult?>>, ElementOfResult>](lazymapsequence/flatmap(_:)-94qg.md)
  Returns the non-`nil` results of mapping the given transformation over this sequence.
- [func flatMap<SegmentOfResult>((Self.Elements.Element) -> SegmentOfResult) -> LazySequence<FlattenSequence<LazyMapSequence<Self.Elements, SegmentOfResult>>>](lazymapsequence/flatmap(_:)-q9wd.md)
  Returns the concatenated results of mapping the given transformation over this sequence.
- [func joined() -> LazySequence<FlattenSequence<Self.Elements>>](lazymapsequence/joined-3sfyr.md)
  Returns a lazy sequence that concatenates the elements of this sequence of sequences.
- [func map<U>((Self.Element) -> U) -> LazyMapSequence<Self.Elements, U>](lazymapsequence/map(_:)-8mwhr.md)
  Returns a `LazyMapSequence` over this `Sequence`.  The elements of the result are computed lazily, each time they are read, by calling `transform` function on a base element.
- [func prefix(while: (Self.Elements.Element) -> Bool) -> LazyPrefixWhileSequence<Self.Elements>](lazymapsequence/prefix(while:).md)
  Returns a lazy sequence of the initial consecutive elements that satisfy `predicate`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazymapsequence/lazysequenceprotocol-implementations)*