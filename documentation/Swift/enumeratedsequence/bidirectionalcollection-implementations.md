# BidirectionalCollection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var last: Self.Element?](enumeratedsequence/last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](enumeratedsequence/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func distance(from: Self.Index, to: Self.Index) -> Int](enumeratedsequence/distance(from:to:)-90p1a.md)
- [func formIndex(before: inout Self.Index)](enumeratedsequence/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](enumeratedsequence/index(_:offsetby:)-5oheh.md)
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](enumeratedsequence/index(_:offsetby:limitedby:)-3spm1.md)
- [func index(before: EnumeratedSequence<Base>.Index) -> EnumeratedSequence<Base>.Index](enumeratedsequence/index(before:).md)
  Returns the position immediately before the given index.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](enumeratedsequence/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](enumeratedsequence/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/enumeratedsequence/bidirectionalcollection-implementations)*