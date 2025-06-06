# Collection Implementations

**Framework**: Create ML

## Topics

### Instance Properties
- [var count: Int](mldatatable/row/count.md)
  The number of elements in the collection.
- [var endIndex: Int](mldatatable/row/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var first: Self.Element?](mldatatable/row/first.md)
  The first element of the collection.
- [var indices: DefaultIndices<Self>](mldatatable/row/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](mldatatable/row/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: Int](mldatatable/row/startindex.md)
  The position of the first element in a nonempty collection.
- [var underestimatedCount: Int](mldatatable/row/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func distance(from: Self.Index, to: Self.Index) -> Int](mldatatable/row/distance(from:to:).md)
  Returns the distance between two indices.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](mldatatable/row/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](mldatatable/row/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](mldatatable/row/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](mldatatable/row/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](mldatatable/row/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](mldatatable/row/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](mldatatable/row/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](mldatatable/row/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](mldatatable/row/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Int) -> Int](mldatatable/row/index(after:).md)
  Returns the position immediately after the given index.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](mldatatable/row/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func makeIterator() -> IndexingIterator<Self>](mldatatable/row/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](mldatatable/row/map(_:)-48z0b.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(Int) -> Self.SubSequence](mldatatable/row/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](mldatatable/row/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](mldatatable/row/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](mldatatable/row/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](mldatatable/row/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](mldatatable/row/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](mldatatable/row/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](mldatatable/row/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func suffix(Int) -> Self.SubSequence](mldatatable/row/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](mldatatable/row/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
- [func trimmingPrefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](mldatatable/row/trimmingprefix(while:).md)
### Subscripts
- [subscript<R>(R) -> Self.SubSequence](mldatatable/row/subscript(_:)-1xauh.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(Int) -> (MLDataTable.Row.Key, MLDataTable.Row.Value)](mldatatable/row/subscript(_:)-26oc3.md)
  Accesses the element at the specified position.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](mldatatable/row/subscript(_:)-2n06g.md)
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](mldatatable/row/subscript(_:)-3zxzk.md)
  Accesses a view of this collection with the elements at the given indices.
- [subscript(Range<Self.Index>) -> Slice<Self>](mldatatable/row/subscript(_:)-79vvr.md)
  Accesses a contiguous subrange of the collection’s elements.
### Type Aliases
- [MLDataTable.Row.Index](mldatatable/row/index.md)
  A type that represents a position in the collection.
- [MLDataTable.Row.Indices](mldatatable/row/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [MLDataTable.Row.Iterator](mldatatable/row/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [MLDataTable.Row.SubSequence](mldatatable/row/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/row/collection-implementations)*