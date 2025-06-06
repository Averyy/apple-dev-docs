# BidirectionalCollection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var last: Self.Element?](substring/last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](substring/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](substring/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func distance(from: Substring.Index, to: Substring.Index) -> Int](substring/distance(from:to:).md)
  Returns the distance between two indices.
- [func dropLast(Int) -> Self.SubSequence](substring/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func formIndex(before: inout Self.Index)](substring/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(Substring.Index, offsetBy: Int) -> Substring.Index](substring/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Substring.Index, offsetBy: Int, limitedBy: Substring.Index) -> Substring.Index?](substring/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Substring.Index) -> Substring.Index](substring/index(after:).md)
  Returns the position immediately after the given index.
- [func index(before: Substring.Index) -> Substring.Index](substring/index(before:).md)
  Returns the position immediately before the given index.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](substring/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](substring/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](substring/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func popLast() -> Self.Element?](substring/poplast-7k3s0.md)
  Removes and returns the last element of the collection.
- [func removeLast() -> Self.Element](substring/removelast-2gcne.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](substring/removelast(_:)-8r1d9.md)
  Removes the given number of elements from the end of the collection.
- [func reversed() -> ReversedCollection<Self>](substring/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func suffix(Int) -> Self.SubSequence](substring/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
### Subscripts
- [subscript(Range<Substring.Index>) -> Substring](substring/subscript(_:)-6e3qj.md)
  Accesses a contiguous subrange of the collection’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/bidirectionalcollection-implementations)*