# Collection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var count: Int](substring/count.md)
  The number of elements in the collection.
- [var endIndex: Substring.Index](substring/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var first: Self.Element?](substring/first.md)
  The first element of the collection.
- [var indices: DefaultIndices<Self>](substring/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](substring/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: Substring.Index](substring/startindex.md)
  The position of the first element in a nonempty collection.
- [var underestimatedCount: Int](substring/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](substring/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](substring/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func firstIndex(of: Self.Element) -> Self.Index?](substring/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](substring/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](substring/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](substring/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](substring/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(of: Self.Element) -> Self.Index?](substring/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](substring/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](substring/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func makeIterator() -> IndexingIterator<Self>](substring/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](substring/map(_:)-5p6oh.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func popFirst() -> Self.Element?](substring/popfirst.md)
  Removes and returns the first element of the collection.
- [func prefix(Int) -> Self.SubSequence](substring/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](substring/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](substring/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](substring/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](substring/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](substring/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removeFirst() -> Self.Element](substring/removefirst-5bf95.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](substring/removefirst(_:)-5qb6j.md)
  Removes the specified number of elements from the beginning of the collection.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](substring/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](substring/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](substring/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(from: Self.Index) -> Self.SubSequence](substring/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript(Substring.Index) -> Character](substring/subscript(_:)-2nr4p.md)
  Accesses the element at the specified position.
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](substring/subscript(_:)-392pj.md)
  Accesses a view of this collection with the elements at the given indices.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](substring/subscript(_:)-4al8g.md)
- [subscript<R>(R) -> Self.SubSequence](substring/subscript(_:)-4h7r7.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
### Type Aliases
- [Substring.Index](substring/index.md)
  A type that represents a position in the collection.
- [Substring.Indices](substring/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Substring.Iterator](substring/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [Substring.SubSequence](substring/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/collection-implementations)*