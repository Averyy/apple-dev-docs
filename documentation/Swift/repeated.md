# Repeated

**Framework**: Swift  
**Kind**: struct

A collection whose elements are all identical.

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
struct Repeated<Element>
```

#### Overview

You create an instance of the `Repeated` collection by calling the `repeatElement(_:count:)` function. The following example creates a collection containing the name “Humperdinck” repeated five times:

```swift
let repeatedName = repeatElement("Humperdinck", count: 5)
for name in repeatedName {
    print(name)
}
// "Humperdinck"
// "Humperdinck"
// "Humperdinck"
// "Humperdinck"
// "Humperdinck"
```

## Topics

### Instance Properties
- [let count: Int](repeated/count.md)
  The number of elements in this collection.
- [let repeatedValue: Element](repeated/repeatedvalue.md)
  The value of every element in this collection.
### Default Implementations
- [BidirectionalCollection Implementations](repeated/bidirectionalcollection-implementations.md)
- [Collection Implementations](repeated/collection-implementations.md)
- [RandomAccessCollection Implementations](repeated/randomaccesscollection-implementations.md)
- [Sequence Implementations](repeated/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](bidirectionalcollection.md)
- [Collection](collection.md)
- [Copyable](copyable.md)
- [DataProtocol](../Foundation/DataProtocol.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/repeated)*