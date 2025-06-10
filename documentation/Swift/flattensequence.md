# FlattenSequence

**Framework**: Swift  
**Kind**: struct

A sequence consisting of all the elements contained in each segment contained in some `Base` sequence.

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
struct FlattenSequence<Base> where Base : Sequence, Base.Element : Sequence
```

#### Overview

The elements of this view are a concatenation of the elements of each sequence in the base.

The `joined` method is always lazy, but does not implicitly confer laziness on algorithms applied to its result.  In other words, for ordinary sequences `s`:

- `s.joined()` does not create new storage
- `s.joined().map(f)` maps eagerly and returns a new array
- `s.lazy.joined().map(f)` maps lazily and returns a `LazyMapSequence`

## Topics

### Instance Methods
- [func formIndex(inout FlattenSequence<Base>.Index, offsetBy: Int)](flattensequence/formindex(_:offsetby:).md)
- [func formIndex(inout FlattenSequence<Base>.Index, offsetBy: Int, limitedBy: FlattenSequence<Base>.Index) -> Bool](flattensequence/formindex(_:offsetby:limitedby:).md)
### Default Implementations
- [BidirectionalCollection Implementations](flattensequence/bidirectionalcollection-implementations.md)
- [Collection Implementations](flattensequence/collection-implementations.md)
- [Sequence Implementations](flattensequence/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](bidirectionalcollection.md)
- [Collection](collection.md)
- [Copyable](copyable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/flattensequence)*