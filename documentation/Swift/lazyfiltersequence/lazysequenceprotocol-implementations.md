# LazySequenceProtocol Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var elements: Self](lazyfiltersequence/elements-swift.property.md)
  Identical to `self`.
- [var lazy: Self.Elements](lazyfiltersequence/lazy.md)
### Instance Methods
- [func compactMap<ElementOfResult>((Self.Elements.Element) -> ElementOfResult?) -> LazyMapSequence<LazyFilterSequence<LazyMapSequence<Self.Elements, ElementOfResult?>>, ElementOfResult>](lazyfiltersequence/compactmap(_:)-72vhr.md)
  Returns the non-`nil` results of mapping the given transformation over this sequence.
- [func drop(while: (Self.Elements.Element) -> Bool) -> LazyDropWhileSequence<Self.Elements>](lazyfiltersequence/drop(while:).md)
  Returns a lazy sequence that skips any initial elements that satisfy `predicate`.
- [func flatMap<SegmentOfResult>((Self.Elements.Element) -> SegmentOfResult) -> LazySequence<FlattenSequence<LazyMapSequence<Self.Elements, SegmentOfResult>>>](lazyfiltersequence/flatmap(_:)-5g3dt.md)
  Returns the concatenated results of mapping the given transformation over this sequence.
- [func flatMap<ElementOfResult>((Self.Elements.Element) -> ElementOfResult?) -> LazyMapSequence<LazyFilterSequence<LazyMapSequence<Self.Elements, ElementOfResult?>>, ElementOfResult>](lazyfiltersequence/flatmap(_:)-5pe4l.md)
  Returns the non-`nil` results of mapping the given transformation over this sequence.
- [func joined() -> LazySequence<FlattenSequence<Self.Elements>>](lazyfiltersequence/joined-2q2lq.md)
  Returns a lazy sequence that concatenates the elements of this sequence of sequences.
- [func map<U>((Self.Element) -> U) -> LazyMapSequence<Self.Elements, U>](lazyfiltersequence/map(_:)-9kh6q.md)
  Returns a `LazyMapSequence` over this `Sequence`.  The elements of the result are computed lazily, each time they are read, by calling `transform` function on a base element.
- [func prefix(while: (Self.Elements.Element) -> Bool) -> LazyPrefixWhileSequence<Self.Elements>](lazyfiltersequence/prefix(while:).md)
  Returns a lazy sequence of the initial consecutive elements that satisfy `predicate`.
### Type Aliases
- [LazyFilterSequence.Elements](lazyfiltersequence/elements.md)
  A `Sequence` that can contain the same elements as this one, possibly with a simpler type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazyfiltersequence/lazysequenceprotocol-implementations)*