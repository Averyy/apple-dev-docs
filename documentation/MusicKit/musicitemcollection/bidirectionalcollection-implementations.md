# BidirectionalCollection Implementations

**Framework**: MusicKit

## Topics

### Instance Properties
- [var last: Self.Element?](musicitemcollection/last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](musicitemcollection/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](musicitemcollection/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func dropLast(Int) -> Self.SubSequence](musicitemcollection/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func firstRange<C>(of: C) -> Range<Self.Index>?](musicitemcollection/firstrange(of:)-4wrl.md)
  Finds and returns the range of the first occurrence of a given collection within this collection.
- [func formIndex(before: inout Self.Index)](musicitemcollection/formindex(before:)-2ifs7.md)
  Replaces the given index with its predecessor.
- [func joined(separator: String) -> String](musicitemcollection/joined(separator:)-6zlx3.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](musicitemcollection/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](musicitemcollection/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](musicitemcollection/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func reversed() -> ReversedCollection<Self>](musicitemcollection/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func suffix(Int) -> Self.SubSequence](musicitemcollection/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicitemcollection/bidirectionalcollection-implementations)*