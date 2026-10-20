# LazySequenceProtocol Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Instance Properties
- [var elements: Self](./elements-swift.property.md)
  Identical to `self`.
### Instance Methods
- [func compactMap<ElementOfResult>((Self.Elements.Element) -> ElementOfResult?) -> LazyMapSequence<LazyFilterSequence<LazyMapSequence<Self.Elements, ElementOfResult?>>, ElementOfResult>](./compactmap%28_%29-188bn.md)
  Returns the non-`nil` results of mapping the given transformation over this sequence.
- [func filter((Self.Elements.Element) -> Bool) -> LazyFilterSequence<Self.Elements>](./filter%28_%29-7stzr.md)
  Returns the elements of `self` that satisfy `isIncluded`.
- [func flatMap<SegmentOfResult>((Self.Elements.Element) -> SegmentOfResult) -> LazySequence<FlattenSequence<LazyMapSequence<Self.Elements, SegmentOfResult>>>](./flatmap%28_%29-1q7p9.md)
  Returns the concatenated results of mapping the given transformation over this sequence.
- [func flatMap<ElementOfResult>((Self.Elements.Element) -> ElementOfResult?) -> LazyMapSequence<LazyFilterSequence<LazyMapSequence<Self.Elements, ElementOfResult?>>, ElementOfResult>](./flatmap%28_%29-6ng42.md)
  Returns the non-`nil` results of mapping the given transformation over this sequence.
- [func joined() -> LazySequence<FlattenSequence<Self.Elements>>](./joined%28%29-3bqi4.md)
  Returns a lazy sequence that concatenates the elements of this sequence of sequences.
- [func map<U>((Self.Element) -> U) -> LazyMapSequence<Self.Elements, U>](./map%28_%29-87fp1.md)
  Returns a `LazyMapSequence` over this `Sequence`.  The elements of the result are computed lazily, each time they are read, by calling `transform` function on a base element.
### Type Aliases
- [typealias Elements](./elements.md)
  A `Sequence` that can contain the same elements as this one, possibly with a simpler type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/lazysequenceprotocol-implementations)*