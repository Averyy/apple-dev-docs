# BidirectionalCollection Implementations

**Framework**: TabularData

## Topics

### Instance Properties
- [var last: Self.Element?](dataframe/rows-swift.struct/last.md)
  The last element of the collection.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](dataframe/rows-swift.struct/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](dataframe/rows-swift.struct/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func distance(from: Self.Index, to: Self.Index) -> Int](dataframe/rows-swift.struct/distance(from:to:).md)
- [func dropLast(Int) -> Self.SubSequence](dataframe/rows-swift.struct/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func formIndex(before: inout Self.Index)](dataframe/rows-swift.struct/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](dataframe/rows-swift.struct/index(_:offsetby:).md)
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](dataframe/rows-swift.struct/index(_:offsetby:limitedby:).md)
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](dataframe/rows-swift.struct/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](dataframe/rows-swift.struct/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](dataframe/rows-swift.struct/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func popLast() -> Self.Element?](dataframe/rows-swift.struct/poplast.md)
  Removes and returns the last element of the collection.
- [func removeLast() -> Self.Element](dataframe/rows-swift.struct/removelast.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](dataframe/rows-swift.struct/removelast(_:).md)
  Removes the given number of elements from the end of the collection.
- [func reversed() -> ReversedCollection<Self>](dataframe/rows-swift.struct/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func suffix(Int) -> Self.SubSequence](dataframe/rows-swift.struct/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/rows-swift.struct/bidirectionalcollection-implementations)*