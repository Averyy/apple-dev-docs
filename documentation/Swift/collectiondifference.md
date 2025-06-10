# CollectionDifference

**Framework**: Swift  
**Kind**: struct

A collection of insertions and removals that describe the difference between two ordered collection states.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct CollectionDifference<ChangeElement>
```

## Topics

### Initializers
- [init?<Changes>(Changes)](collectiondifference/init(_:).md)
  Creates a new collection difference from a collection of changes.
### Instance Properties
- [let insertions: [CollectionDifference<ChangeElement>.Change]](collectiondifference/insertions.md)
  The insertions contained by this difference, from lowest offset to highest.
- [let removals: [CollectionDifference<ChangeElement>.Change]](collectiondifference/removals.md)
  The removals contained by this difference, from lowest offset to highest.
### Instance Methods
- [func formIndex(inout CollectionDifference<ChangeElement>.Index, offsetBy: Int)](collectiondifference/formindex(_:offsetby:).md)
- [func index(before: CollectionDifference<ChangeElement>.Index) -> CollectionDifference<ChangeElement>.Index](collectiondifference/index(before:).md)
- [func inferringMoves() -> CollectionDifference<ChangeElement>](collectiondifference/inferringmoves.md)
  Returns a new collection difference with associations between individual elements that have been removed and inserted only once.
- [func inverse() -> CollectionDifference<ChangeElement>](collectiondifference/inverse.md)
### Enumerations
- [CollectionDifference.Change](collectiondifference/change.md)
  A single change to a collection.
### Default Implementations
- [Collection Implementations](collectiondifference/collection-implementations.md)
- [Decodable Implementations](collectiondifference/decodable-implementations.md)
- [Encodable Implementations](collectiondifference/encodable-implementations.md)
- [Equatable Implementations](collectiondifference/equatable-implementations.md)
- [Hashable Implementations](collectiondifference/hashable-implementations.md)
- [Sequence Implementations](collectiondifference/sequence-implementations.md)

## Relationships

### Conforms To
- [Collection](collection.md)
- [Copyable](copyable.md)
- [Decodable](decodable.md)
- [Encodable](encodable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [Sequence](sequence.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collectiondifference)*