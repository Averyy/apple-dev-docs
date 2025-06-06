# BidirectionalCollection Implementations

**Framework**: TabularData

## Topics

### Instance Properties
- [var endIndex: Int](column/endindex.md)
  The index of the final element in the column.
- [var last: Self.Element?](column/last.md)
  The last element of the collection.
- [var startIndex: Int](column/startindex.md)
  The index of the initial element in the column.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](column/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](column/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func distance(from: Self.Index, to: Self.Index) -> Int](column/distance(from:to:).md)
- [func dropLast(Int) -> Self.SubSequence](column/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func formIndex(before: inout Self.Index)](column/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](column/index(_:offsetby:).md)
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](column/index(_:offsetby:limitedby:).md)
- [func index(after: Int) -> Int](column/index(after:).md)
  Returns the index immediately after an element index.
- [func index(before: Int) -> Int](column/index(before:).md)
  Returns the index immediately before an element index.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](column/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](column/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](column/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func reversed() -> ReversedCollection<Self>](column/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func suffix(Int) -> Self.SubSequence](column/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
### Subscripts
- [subscript(Range<Int>) -> ColumnSlice<WrappedElement>](column/subscript(_:)-gne9.md)
  Accesses a contiguous range of elements.
- [subscript(Int) -> Column<WrappedElement>.Element](column/subscript(_:)-qm4d.md)
  Accesses an element at an index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/bidirectionalcollection-implementations)*