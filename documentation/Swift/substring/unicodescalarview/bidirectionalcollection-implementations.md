# BidirectionalCollection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var last: Self.Element?](substring/unicodescalarview/last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](substring/unicodescalarview/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](substring/unicodescalarview/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func dropLast(Int) -> Self.SubSequence](substring/unicodescalarview/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func formIndex(before: inout Substring.UnicodeScalarView.Index)](substring/unicodescalarview/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(before: Substring.UnicodeScalarView.Index) -> Substring.UnicodeScalarView.Index](substring/unicodescalarview/index(before:).md)
  Returns the position immediately before the given index.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](substring/unicodescalarview/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](substring/unicodescalarview/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](substring/unicodescalarview/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func popLast() -> Self.Element?](substring/unicodescalarview/poplast-7f9to.md)
  Removes and returns the last element of the collection.
- [func removeLast() -> Self.Element](substring/unicodescalarview/removelast-8b12x.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](substring/unicodescalarview/removelast(_:)-4vtt6.md)
  Removes the given number of elements from the end of the collection.
- [func reversed() -> ReversedCollection<Self>](substring/unicodescalarview/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func suffix(Int) -> Self.SubSequence](substring/unicodescalarview/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/unicodescalarview/bidirectionalcollection-implementations)*