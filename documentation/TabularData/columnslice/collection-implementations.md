# Collection Implementations

**Framework**: TabularData

## Topics

### Instance Properties
- [var count: Int](columnslice/count.md)
  The number of elements in the column slice.
- [var count: Int](columnslice/count-89q2u.md)
  The number of elements in the collection.
- [var first: Self.Element?](columnslice/first.md)
  The first element of the collection.
- [var isEmpty: Bool](columnslice/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var underestimatedCount: Int](columnslice/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func contains<C>(C) -> Bool](columnslice/contains(_:)-7u7b2.md)
  Returns a Boolean value indicating whether the collection contains the given sequence.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](columnslice/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](columnslice/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func firstIndex(of: Self.Element) -> Self.Index?](columnslice/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](columnslice/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func firstRange<C>(of: C) -> Range<Self.Index>?](columnslice/firstrange(of:).md)
  Finds and returns the range of the first occurrence of a given collection within this collection.
- [func formIndex(inout Self.Index, offsetBy: Int)](columnslice/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](columnslice/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](columnslice/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(of: Self.Element) -> Self.Index?](columnslice/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](columnslice/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](columnslice/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func makeIterator() -> IndexingIterator<Self>](columnslice/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](columnslice/map(_:)-5qic9.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func popFirst() -> Self.Element?](columnslice/popfirst.md)
  Removes and returns the first element of the collection.
- [func prefix(Int) -> Self.SubSequence](columnslice/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](columnslice/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](columnslice/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](columnslice/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](columnslice/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](columnslice/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func ranges<C>(of: C) -> [Range<Self.Index>]](columnslice/ranges(of:).md)
  Finds and returns the ranges of the all occurrences of a given sequence within the collection.
- [func removeFirst() -> Self.Element](columnslice/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](columnslice/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](columnslice/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](columnslice/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](columnslice/split(separator:maxsplits:omittingemptysubsequences:)-25tcz.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func split<C>(separator: C, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](columnslice/split(separator:maxsplits:omittingemptysubsequences:)-8pp7i.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given separator.
- [func suffix(from: Self.Index) -> Self.SubSequence](columnslice/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
- [func trimPrefix<Prefix>(Prefix)](columnslice/trimprefix(_:).md)
  Removes `prefix` from the start of the collection.
- [func trimPrefix(while: (Self.Element) throws -> Bool) throws](columnslice/trimprefix(while:).md)
- [func trimmingPrefix<Prefix>(Prefix) -> Self.SubSequence](columnslice/trimmingprefix(_:).md)
  Returns a new collection of the same type by removing `prefix` from the start of the collection.
- [func trimmingPrefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](columnslice/trimmingprefix(while:).md)
### Subscripts
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](columnslice/subscript(_:)-n8jc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnslice/collection-implementations)*