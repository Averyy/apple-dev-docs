# LazySequenceProtocol Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var elements: Self](lazydropwhilesequence/elements-swift.property.md)
  Identical to `self`.
- [var lazy: Self.Elements](lazydropwhilesequence/lazy.md)
### Instance Methods
- [func compactMap<ElementOfResult>((Self.Elements.Element) -> ElementOfResult?) -> LazyMapSequence<LazyFilterSequence<LazyMapSequence<Self.Elements, ElementOfResult?>>, ElementOfResult>](lazydropwhilesequence/compactmap(_:)-9ksui.md)
  Returns the non-`nil` results of mapping the given transformation over this sequence.
- [func drop(while: (Self.Elements.Element) -> Bool) -> LazyDropWhileSequence<Self.Elements>](lazydropwhilesequence/drop(while:).md)
  Returns a lazy sequence that skips any initial elements that satisfy `predicate`.
- [func filter((Self.Elements.Element) -> Bool) -> LazyFilterSequence<Self.Elements>](lazydropwhilesequence/filter(_:).md)
  Returns the elements of `self` that satisfy `isIncluded`.
- [func flatMap<SegmentOfResult>((Self.Elements.Element) -> SegmentOfResult) -> LazySequence<FlattenSequence<LazyMapSequence<Self.Elements, SegmentOfResult>>>](lazydropwhilesequence/flatmap(_:)-6szox.md)
  Returns the concatenated results of mapping the given transformation over this sequence.
- [func flatMap<ElementOfResult>((Self.Elements.Element) -> ElementOfResult?) -> LazyMapSequence<LazyFilterSequence<LazyMapSequence<Self.Elements, ElementOfResult?>>, ElementOfResult>](lazydropwhilesequence/flatmap(_:)-726ic.md)
  Returns the non-`nil` results of mapping the given transformation over this sequence.
- [func joined() -> LazySequence<FlattenSequence<Self.Elements>>](lazydropwhilesequence/joined-3lx90.md)
  Returns a lazy sequence that concatenates the elements of this sequence of sequences.
- [func map<U>((Self.Element) -> U) -> LazyMapSequence<Self.Elements, U>](lazydropwhilesequence/map(_:)-3n26j.md)
  Returns a `LazyMapSequence` over this `Sequence`.  The elements of the result are computed lazily, each time they are read, by calling `transform` function on a base element.
- [func prefix(while: (Self.Elements.Element) -> Bool) -> LazyPrefixWhileSequence<Self.Elements>](lazydropwhilesequence/prefix(while:).md)
  Returns a lazy sequence of the initial consecutive elements that satisfy `predicate`.
### Type Aliases
- [LazyDropWhileSequence.Elements](lazydropwhilesequence/elements.md)
  A `Sequence` that can contain the same elements as this one, possibly with a simpler type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazydropwhilesequence/lazysequenceprotocol-implementations)*