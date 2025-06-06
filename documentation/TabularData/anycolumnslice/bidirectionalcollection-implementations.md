# BidirectionalCollection Implementations

**Framework**: TabularData

## Topics

### Instance Properties
- [var last: Self.Element?](anycolumnslice/last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](anycolumnslice/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func dropLast(Int) -> Self.SubSequence](anycolumnslice/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func formIndex(before: inout Self.Index)](anycolumnslice/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](anycolumnslice/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](anycolumnslice/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func popLast() -> Self.Element?](anycolumnslice/poplast.md)
  Removes and returns the last element of the collection.
- [func removeLast() -> Self.Element](anycolumnslice/removelast.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](anycolumnslice/removelast(_:).md)
  Removes the given number of elements from the end of the collection.
- [func reversed() -> ReversedCollection<Self>](anycolumnslice/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func suffix(Int) -> Self.SubSequence](anycolumnslice/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumnslice/bidirectionalcollection-implementations)*