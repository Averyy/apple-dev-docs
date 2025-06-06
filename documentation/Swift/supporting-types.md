# Supporting Types

**Framework**: Swift

Use wrappers, indices, and iterators in operations like slicing, flattening, and reversing a collection.

## Topics

### Slices
- [struct Slice](slice.md)
  A view into a subsequence of elements of another collection.
### Range Expressions
- [struct PartialRangeUpTo](partialrangeupto.md)
  A partial half-open interval up to, but not including, an upper bound.
- [struct PartialRangeThrough](partialrangethrough.md)
  A partial interval up to, and including, an upper bound.
- [struct PartialRangeFrom](partialrangefrom.md)
  A partial interval extending upward from a lower bound.
- [protocol RangeExpression](rangeexpression.md)
  A type that can be used to slice a collection.
- [enum UnboundedRange_](unboundedrange_.md)
  A range expression that represents the entire range of a collection.
### Type-Erasing Wrappers
- [struct AnySequence](anysequence.md)
  A type-erased sequence.
- [struct AnyCollection](anycollection.md)
  A type-erased wrapper over any collection with indices that support forward traversal.
- [struct AnyBidirectionalCollection](anybidirectionalcollection.md)
  A type-erased wrapper over any collection with indices that support bidirectional traversal.
- [struct AnyRandomAccessCollection](anyrandomaccesscollection.md)
  A type-erased wrapper over any collection with indices that support random access traversal.
- [struct AnyIterator](anyiterator.md)
  A type-erased iterator of `Element`.
- [struct AnyIndex](anyindex.md)
  A wrapper over an underlying index that hides the specific underlying type.
- [struct AnyHashable](anyhashable.md)
  A type-erased hashable value.
### Lazy Wrappers
- [struct LazySequence](lazysequence.md)
  A sequence containing the same elements as a `Base` sequence, but on which some operations such as `map` and `filter` are implemented lazily.
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
### Wrappers for Algorithms
- [struct CollectionDifference](collectiondifference.md)
  A collection of insertions and removals that describe the difference between two ordered collection states.
- [struct DropFirstSequence](dropfirstsequence.md)
  A sequence that lazily consumes and drops `n` elements from an underlying `Base` iterator before possibly returning the first available element.
- [struct DropWhileSequence](dropwhilesequence.md)
  A sequence that lazily consumes and drops `n` elements from an underlying `Base` iterator before possibly returning the first available element.
- [struct EnumeratedSequence](enumeratedsequence.md)
  An enumeration of the elements of a sequence or collection.
- [typealias FlattenCollection](flattencollection.md)
- [struct FlattenSequence](flattensequence.md)
  A sequence consisting of all the elements contained in each segment contained in some `Base` sequence.
- [struct JoinedSequence](joinedsequence.md)
  A sequence that presents the elements of a base sequence of sequences concatenated using a given separator.
- [struct PrefixSequence](prefixsequence.md)
  A sequence that only consumes up to `n` elements from an underlying `Base` iterator.
- [struct Repeated](repeated.md)
  A collection whose elements are all identical.
- [struct ReversedCollection](reversedcollection.md)
  A collection that presents the elements of its base collection in reverse order.
- [struct StrideTo](strideto.md)
  A sequence of values formed by striding over a half-open interval.
- [struct StrideThrough](stridethrough.md)
  A sequence of values formed by striding over a closed interval.
- [struct UnfoldSequence](unfoldsequence.md)
  A sequence whose elements are produced via repeated applications of a closure to some mutable state.
- [struct Zip2Sequence](zip2sequence.md)
  A sequence of pairs built out of two underlying sequences.
### Collections of Indices
- [struct DefaultIndices](defaultindices.md)
  A collection of indices for an arbitrary collection
### Indices and Iterators
- [struct IteratorSequence](iteratorsequence.md)
  A sequence built around an iterator of type `Base`.
- [struct IndexingIterator](indexingiterator.md)
  A type that iterates over a collection using its indices.
- [typealias EnumeratedIterator](enumeratediterator.md)
- [typealias SetIterator](setiterator.md)
- [struct StrideThroughIterator](stridethroughiterator.md)
  An iterator for a `StrideThrough` instance.
- [struct StrideToIterator](stridetoiterator.md)
  An iterator for a `StrideTo` instance.
### Deprecated
- [typealias DictionaryIndex](dictionaryindex.md)
- [typealias SetIndex](setindex.md)
- [typealias CountableClosedRange](countableclosedrange.md)
- [typealias CountablePartialRangeFrom](countablepartialrangefrom.md)
- [typealias CountableRange](countablerange.md)

## See Also

- [Sequence and Collection Protocols](sequence-and-collection-protocols.md)
  Write generic code that works with any collection, or build your own collection types.
- [Managed Buffers](managed-buffers.md)
  Build your own buffer-backed collection types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/supporting-types)*