# BidirectionalCollection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var indices: Substring.UTF16View.Indices](substring/utf16view/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var last: Self.Element?](substring/utf16view/last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](substring/utf16view/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](substring/utf16view/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func distance(from: Substring.UTF16View.Index, to: Substring.UTF16View.Index) -> Int](substring/utf16view/distance(from:to:).md)
  Returns the distance between two indices.
- [func dropLast(Int) -> Self.SubSequence](substring/utf16view/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func formIndex(after: inout Substring.UTF16View.Index)](substring/utf16view/formindex(after:).md)
  Replaces the given index with its successor.
- [func formIndex(before: inout Substring.UTF16View.Index)](substring/utf16view/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(Substring.UTF16View.Index, offsetBy: Int) -> Substring.UTF16View.Index](substring/utf16view/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Substring.UTF16View.Index, offsetBy: Int, limitedBy: Substring.UTF16View.Index) -> Substring.UTF16View.Index?](substring/utf16view/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Substring.UTF16View.Index) -> Substring.UTF16View.Index](substring/utf16view/index(after:).md)
  Returns the position immediately after the given index.
- [func index(before: Substring.UTF16View.Index) -> Substring.UTF16View.Index](substring/utf16view/index(before:).md)
  Returns the position immediately before the given index.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](substring/utf16view/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](substring/utf16view/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](substring/utf16view/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func popLast() -> Self.Element?](substring/utf16view/poplast.md)
  Removes and returns the last element of the collection.
- [func removeLast() -> Self.Element](substring/utf16view/removelast.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](substring/utf16view/removelast(_:).md)
  Removes the given number of elements from the end of the collection.
- [func reversed() -> ReversedCollection<Self>](substring/utf16view/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func suffix(Int) -> Self.SubSequence](substring/utf16view/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
### Subscripts
- [subscript(Range<Substring.UTF16View.Index>) -> Substring.UTF16View](substring/utf16view/subscript(_:)-20thk.md)
  Accesses a contiguous subrange of the collection’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/utf16view/bidirectionalcollection-implementations)*