# ReversedCollection

**Framework**: Swift  
**Kind**: struct

A collection that presents the elements of its base collection in reverse order.

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
struct ReversedCollection<Base> where Base : BidirectionalCollection
```

#### Overview

> **Note**: This type is the result of `x.reversed()` where `x` is a collection having bidirectional indices.

The `reversed()` method is always lazy when applied to a collection with bidirectional indices, but does not implicitly confer laziness on algorithms applied to its result.  In other words, for ordinary collections `c` having bidirectional indices:

- `c.reversed()` does not create new storage
- `c.reversed().map(f)` maps eagerly and returns a new array
- `c.lazy.reversed().map(f)` maps lazily and returns a `LazyMapCollection`

## Topics

### Instance Methods
- [func reversed() -> Base](reversedcollection/reversed.md)
  Reversing a reversed collection returns the original collection.
### Default Implementations
- [BidirectionalCollection Implementations](reversedcollection/bidirectionalcollection-implementations.md)
- [Collection Implementations](reversedcollection/collection-implementations.md)
- [LazySequenceProtocol Implementations](reversedcollection/lazysequenceprotocol-implementations.md)
- [Sequence Implementations](reversedcollection/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](bidirectionalcollection.md)
- [Collection](collection.md)
- [Copyable](copyable.md)
- [LazySequenceProtocol](lazysequenceprotocol.md)
- [RandomAccessCollection](randomaccesscollection.md)
- [Sendable](sendable.md)
- [Sequence](sequence.md)

## See Also

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
- [struct StrideTo](strideto.md)
  A sequence of values formed by striding over a half-open interval.
- [struct StrideThrough](stridethrough.md)
  A sequence of values formed by striding over a closed interval.
- [struct UnfoldSequence](unfoldsequence.md)
  A sequence whose elements are produced via repeated applications of a closure to some mutable state.
- [struct Zip2Sequence](zip2sequence.md)
  A sequence of pairs built out of two underlying sequences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Swift/reversedcollection)*