# BidirectionalCollection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var last: Self.Element?](unsafebufferpointer/last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](unsafebufferpointer/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](unsafebufferpointer/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func dropLast(Int) -> Self.SubSequence](unsafebufferpointer/droplast(_:)-7845q.md)
  Returns a subsequence containing all but the specified number of final elements.
- [func formIndex(before: inout Int)](unsafebufferpointer/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(before: Int) -> Int](unsafebufferpointer/index(before:).md)
  Returns the position immediately before the given index.
- [func joined(separator: String) -> String](unsafebufferpointer/joined(separator:)-5do07.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](unsafebufferpointer/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](unsafebufferpointer/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](unsafebufferpointer/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func reversed() -> ReversedCollection<Self>](unsafebufferpointer/reversed-3wn4o.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func suffix(Int) -> Self.SubSequence](unsafebufferpointer/suffix(_:)-3w6qn.md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafebufferpointer/bidirectionalcollection-implementations)*