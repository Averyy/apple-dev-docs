# BidirectionalCollection Implementations

**Framework**: RealityKit

## Topics

### Instance Properties
- [var last: Self.Element?](jointtransforms/last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](jointtransforms/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](jointtransforms/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func distance(from: Self.Index, to: Self.Index) -> Int](jointtransforms/distance(from:to:).md)
- [func dropLast(Int) -> Self.SubSequence](jointtransforms/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func formIndex(before: inout Self.Index)](jointtransforms/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](jointtransforms/index(_:offsetby:).md)
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](jointtransforms/index(_:offsetby:limitedby:).md)
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](jointtransforms/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](jointtransforms/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](jointtransforms/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func reversed() -> ReversedCollection<Self>](jointtransforms/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func suffix(Int) -> Self.SubSequence](jointtransforms/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/jointtransforms/bidirectionalcollection-implementations)*