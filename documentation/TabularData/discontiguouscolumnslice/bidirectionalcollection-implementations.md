# BidirectionalCollection Implementations

**Framework**: TabularData

## Topics

### Instance Properties
- [var endIndex: Int](discontiguouscolumnslice/endindex.md)
  The index of the final element in the column slice.
- [var last: Self.Element?](discontiguouscolumnslice/last.md)
  The last element of the collection.
- [var startIndex: Int](discontiguouscolumnslice/startindex.md)
  The index of the initial element in the column slice.
### Instance Methods
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](discontiguouscolumnslice/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](discontiguouscolumnslice/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func distance(from: Self.Index, to: Self.Index) -> Int](discontiguouscolumnslice/distance(from:to:).md)
- [func dropLast(Int) -> Self.SubSequence](discontiguouscolumnslice/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func formIndex(before: inout Self.Index)](discontiguouscolumnslice/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](discontiguouscolumnslice/index(_:offsetby:).md)
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](discontiguouscolumnslice/index(_:offsetby:limitedby:).md)
- [func index(after: Int) -> Int](discontiguouscolumnslice/index(after:).md)
  Returns the index immediately after an element index.
- [func index(before: Int) -> Int](discontiguouscolumnslice/index(before:).md)
  Returns the index immediately before an element index.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](discontiguouscolumnslice/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](discontiguouscolumnslice/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](discontiguouscolumnslice/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func popLast() -> Self.Element?](discontiguouscolumnslice/poplast.md)
  Removes and returns the last element of the collection.
- [func removeLast() -> Self.Element](discontiguouscolumnslice/removelast.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](discontiguouscolumnslice/removelast(_:).md)
  Removes the given number of elements from the end of the collection.
- [func reversed() -> ReversedCollection<Self>](discontiguouscolumnslice/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func suffix(Int) -> Self.SubSequence](discontiguouscolumnslice/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
### Subscripts
- [subscript(Range<Int>) -> DiscontiguousColumnSlice<WrappedElement>](discontiguouscolumnslice/subscript(_:)-8rd2f.md)
  Accesses a contiguous range of elements.
- [subscript(Int) -> DiscontiguousColumnSlice<WrappedElement>.Element](discontiguouscolumnslice/subscript(_:)-9y37v.md)
  Accesses an element at an index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice/bidirectionalcollection-implementations)*