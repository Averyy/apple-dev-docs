# Collection Implementations

**Framework**: TabularData

## Topics

### Instance Properties
- [var count: Int](discontiguouscolumnslice/count.md)
  The number of elements in the column slice.
- [var count: Int](discontiguouscolumnslice/count-61id8.md)
  The number of elements in the collection.
- [var first: Self.Element?](discontiguouscolumnslice/first.md)
  The first element of the collection.
- [var indices: DefaultIndices<Self>](discontiguouscolumnslice/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](discontiguouscolumnslice/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var underestimatedCount: Int](discontiguouscolumnslice/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func contains<C>(C) -> Bool](discontiguouscolumnslice/contains(_:)-2xkjf.md)
  Returns a Boolean value indicating whether the collection contains the given sequence.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](discontiguouscolumnslice/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](discontiguouscolumnslice/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func firstIndex(of: Self.Element) -> Self.Index?](discontiguouscolumnslice/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](discontiguouscolumnslice/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func firstRange<C>(of: C) -> Range<Self.Index>?](discontiguouscolumnslice/firstrange(of:).md)
  Finds and returns the range of the first occurrence of a given collection within this collection.
- [func formIndex(inout Self.Index, offsetBy: Int)](discontiguouscolumnslice/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](discontiguouscolumnslice/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](discontiguouscolumnslice/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(of: Self.Element) -> Self.Index?](discontiguouscolumnslice/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](discontiguouscolumnslice/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](discontiguouscolumnslice/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func makeIterator() -> IndexingIterator<Self>](discontiguouscolumnslice/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](discontiguouscolumnslice/map(_:)-5qgwq.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func popFirst() -> Self.Element?](discontiguouscolumnslice/popfirst.md)
  Removes and returns the first element of the collection.
- [func prefix(Int) -> Self.SubSequence](discontiguouscolumnslice/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](discontiguouscolumnslice/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](discontiguouscolumnslice/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](discontiguouscolumnslice/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](discontiguouscolumnslice/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](discontiguouscolumnslice/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func ranges<C>(of: C) -> [Range<Self.Index>]](discontiguouscolumnslice/ranges(of:).md)
  Finds and returns the ranges of the all occurrences of a given sequence within the collection.
- [func removeFirst() -> Self.Element](discontiguouscolumnslice/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](discontiguouscolumnslice/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](discontiguouscolumnslice/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](discontiguouscolumnslice/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split<C>(separator: C, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](discontiguouscolumnslice/split(separator:maxsplits:omittingemptysubsequences:)-45wlq.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given separator.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](discontiguouscolumnslice/split(separator:maxsplits:omittingemptysubsequences:)-6ojpa.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(from: Self.Index) -> Self.SubSequence](discontiguouscolumnslice/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
- [func trimPrefix<Prefix>(Prefix)](discontiguouscolumnslice/trimprefix(_:).md)
  Removes `prefix` from the start of the collection.
- [func trimPrefix(while: (Self.Element) throws -> Bool) throws](discontiguouscolumnslice/trimprefix(while:).md)
- [func trimmingPrefix<Prefix>(Prefix) -> Self.SubSequence](discontiguouscolumnslice/trimmingprefix(_:).md)
  Returns a new collection of the same type by removing `prefix` from the start of the collection.
- [func trimmingPrefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](discontiguouscolumnslice/trimmingprefix(while:).md)
### Type Aliases
- [DiscontiguousColumnSlice.Indices](discontiguouscolumnslice/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [DiscontiguousColumnSlice.Iterator](discontiguouscolumnslice/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [DiscontiguousColumnSlice.SubSequence](discontiguouscolumnslice/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice/collection-implementations)*