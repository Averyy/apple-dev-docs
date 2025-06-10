# BidirectionalCollection Implementations

**Framework**: Foundation Models

## Topics

### Instance Properties
- [var last: Self.Element?](transcript/toolcalls/last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](transcript/toolcalls/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](transcript/toolcalls/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func dropLast(Int) -> Self.SubSequence](transcript/toolcalls/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func formIndex(before: inout Self.Index)](transcript/toolcalls/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](transcript/toolcalls/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](transcript/toolcalls/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](transcript/toolcalls/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func reversed() -> ReversedCollection<Self>](transcript/toolcalls/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func suffix(Int) -> Self.SubSequence](transcript/toolcalls/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/toolcalls/bidirectionalcollection-implementations)*