# LazySequenceProtocol Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Instance Properties
- [var elements: Self](./elements-swift.property.md)
  Identical to `self`.
- [var lazy: Self.Elements](./lazy.md)
### Instance Methods
- [func compactMap<ElementOfResult>((Self.Elements.Element) -> ElementOfResult?) -> LazyMapSequence<LazyFilterSequence<LazyMapSequence<Self.Elements, ElementOfResult?>>, ElementOfResult>](./compactmap%28_%29-72vhr.md)
  Returns the non-`nil` results of mapping the given transformation over this sequence.
- [func drop(while: (Self.Elements.Element) -> Bool) -> LazyDropWhileSequence<Self.Elements>](./drop%28while%29.md)
  Returns a lazy sequence that skips any initial elements that satisfy `predicate`.
- [func flatMap<SegmentOfResult>((Self.Elements.Element) -> SegmentOfResult) -> LazySequence<FlattenSequence<LazyMapSequence<Self.Elements, SegmentOfResult>>>](./flatmap%28_%29-5g3dt.md)
  Returns the concatenated results of mapping the given transformation over this sequence.
- [func flatMap<ElementOfResult>((Self.Elements.Element) -> ElementOfResult?) -> LazyMapSequence<LazyFilterSequence<LazyMapSequence<Self.Elements, ElementOfResult?>>, ElementOfResult>](./flatmap%28_%29-5pe4l.md)
  Returns the non-`nil` results of mapping the given transformation over this sequence.
- [func joined() -> LazySequence<FlattenSequence<Self.Elements>>](./joined%28%29-2q2lq.md)
  Returns a lazy sequence that concatenates the elements of this sequence of sequences.
- [func map<U>((Self.Element) -> U) -> LazyMapSequence<Self.Elements, U>](./map%28_%29-9kh6q.md)
  Returns a `LazyMapSequence` over this `Sequence`.  The elements of the result are computed lazily, each time they are read, by calling `transform` function on a base element.
- [func prefix(while: (Self.Elements.Element) -> Bool) -> LazyPrefixWhileSequence<Self.Elements>](./prefix%28while%29.md)
  Returns a lazy sequence of the initial consecutive elements that satisfy `predicate`.
### Type Aliases
- [LazyFilterSequence.Elements](./elements.md)
  A `Sequence` that can contain the same elements as this one, possibly with a simpler type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazyfiltersequence/lazysequenceprotocol-implementations)*