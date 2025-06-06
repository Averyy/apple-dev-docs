# Collection Implementations

**Framework**: TabularData

## Topics

### Instance Properties
- [var first: Self.Element?](anycolumnslice/first.md)
  The first element of the collection.
- [var isEmpty: Bool](anycolumnslice/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var underestimatedCount: Int](anycolumnslice/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](anycolumnslice/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](anycolumnslice/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](anycolumnslice/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](anycolumnslice/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](anycolumnslice/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](anycolumnslice/formindex(after:).md)
  Replaces the given index with its successor.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](anycolumnslice/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func makeIterator() -> IndexingIterator<Self>](anycolumnslice/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](anycolumnslice/map(_:)-2yg7f.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func popFirst() -> Self.Element?](anycolumnslice/popfirst.md)
  Removes and returns the first element of the collection.
- [func prefix(Int) -> Self.SubSequence](anycolumnslice/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](anycolumnslice/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](anycolumnslice/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](anycolumnslice/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](anycolumnslice/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](anycolumnslice/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removeFirst() -> Self.Element](anycolumnslice/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](anycolumnslice/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](anycolumnslice/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](anycolumnslice/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func suffix(from: Self.Index) -> Self.SubSequence](anycolumnslice/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
- [func trimPrefix(while: (Self.Element) throws -> Bool) throws](anycolumnslice/trimprefix(while:).md)
- [func trimmingPrefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](anycolumnslice/trimmingprefix(while:).md)
### Type Aliases
- [AnyColumnSlice.Index](anycolumnslice/index.md)
  A type that represents a position in the collection.
- [AnyColumnSlice.Indices](anycolumnslice/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [AnyColumnSlice.Iterator](anycolumnslice/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [AnyColumnSlice.SubSequence](anycolumnslice/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumnslice/collection-implementations)*