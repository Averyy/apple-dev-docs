# BidirectionalCollection Implementations

**Framework**: System

## Topics

### Instance Properties
- [var last: Self.Element?](filepath/componentview/last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](filepath/componentview/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](filepath/componentview/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func distance(from: Self.Index, to: Self.Index) -> Int](filepath/componentview/distance(from:to:).md)
- [func dropLast(Int) -> Self.SubSequence](filepath/componentview/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func formIndex(before: inout Self.Index)](filepath/componentview/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](filepath/componentview/index(_:offsetby:).md)
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](filepath/componentview/index(_:offsetby:limitedby:).md)
- [func index(after: FilePath.ComponentView.Index) -> FilePath.ComponentView.Index](filepath/componentview/index(after:).md)
  Returns the position immediately after the given index.
- [func index(before: FilePath.ComponentView.Index) -> FilePath.ComponentView.Index](filepath/componentview/index(before:).md)
  Returns the position immediately before the given index.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](filepath/componentview/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](filepath/componentview/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](filepath/componentview/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func reversed() -> ReversedCollection<Self>](filepath/componentview/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func suffix(Int) -> Self.SubSequence](filepath/componentview/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/componentview/bidirectionalcollection-implementations)*