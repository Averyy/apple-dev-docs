# LazySequence

**Framework**: Swift  
**Kind**: struct

A sequence containing the same elements as a `Base` sequence, but on which some operations such as `map` and `filter` are implemented lazily.

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
struct LazySequence<Base> where Base : Sequence
```

#### Overview

- See also: `LazySequenceProtocol`

## Topics

### Instance Methods
- [func mapAnnotations<Feature, Input, Output>((Input) -> Output) -> LazyMapSequence<Base, AnnotatedFeature<Feature, Output>>](lazysequence/mapannotations(_:).md)
  Returns a lazy sequence where the elements of the result are computed each time they are read by calling transform function on the annotation of an annotated feature.
- [func mapFeatures<Input, Output, Annotation>((Input) -> Output) -> LazyMapSequence<Base, AnnotatedFeature<Output, Annotation>>](lazysequence/mapfeatures(_:).md)
  Returns a lazy sequence where the elements of the result are computed each time they are read by calling transform function on the feature of an annotated feature.
### Default Implementations
- [BidirectionalCollection Implementations](lazysequence/bidirectionalcollection-implementations.md)
- [Collection Implementations](lazysequence/collection-implementations.md)
- [LazySequenceProtocol Implementations](lazysequence/lazysequenceprotocol-implementations.md)
- [RandomAccessCollection Implementations](lazysequence/randomaccesscollection-implementations.md)
- [Sequence Implementations](lazysequence/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](bidirectionalcollection.md)
- [Collection](collection.md)
- [Copyable](copyable.md)
- [LazyCollectionProtocol](lazycollectionprotocol.md)
- [LazySequenceProtocol](lazysequenceprotocol.md)
- [RandomAccessCollection](randomaccesscollection.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [Sequence](sequence.md)

## See Also

- [struct LazyMapSequence](lazymapsequence.md)
  A `Sequence` whose elements consist of those in a `Base` `Sequence` passed through a transform function returning `Element`. These elements are computed lazily, each time they’re read, by calling the transform function on a base element.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazysequence)*