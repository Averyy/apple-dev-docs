# Collection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var count: Int](substring/unicodescalarview/count.md)
  The number of elements in the collection.
- [var endIndex: Substring.UnicodeScalarView.Index](substring/unicodescalarview/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var first: Self.Element?](substring/unicodescalarview/first.md)
  The first element of the collection.
- [var isEmpty: Bool](substring/unicodescalarview/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: Substring.UnicodeScalarView.Index](substring/unicodescalarview/startindex.md)
  The position of the first element in a nonempty collection.
- [var underestimatedCount: Int](substring/unicodescalarview/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](substring/unicodescalarview/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](substring/unicodescalarview/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func firstIndex(of: Self.Element) -> Self.Index?](substring/unicodescalarview/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](substring/unicodescalarview/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](substring/unicodescalarview/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](substring/unicodescalarview/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func index(of: Self.Element) -> Self.Index?](substring/unicodescalarview/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](substring/unicodescalarview/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](substring/unicodescalarview/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func makeIterator() -> IndexingIterator<Self>](substring/unicodescalarview/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](substring/unicodescalarview/map(_:)-3wgri.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func popFirst() -> Self.Element?](substring/unicodescalarview/popfirst.md)
  Removes and returns the first element of the collection.
- [func prefix(Int) -> Self.SubSequence](substring/unicodescalarview/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](substring/unicodescalarview/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](substring/unicodescalarview/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](substring/unicodescalarview/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](substring/unicodescalarview/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](substring/unicodescalarview/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removeFirst() -> Self.Element](substring/unicodescalarview/removefirst-2wary.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](substring/unicodescalarview/removefirst(_:)-2iv78.md)
  Removes the specified number of elements from the beginning of the collection.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](substring/unicodescalarview/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](substring/unicodescalarview/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](substring/unicodescalarview/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(from: Self.Index) -> Self.SubSequence](substring/unicodescalarview/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript(Substring.UnicodeScalarView.Index) -> Substring.UnicodeScalarView.Element](substring/unicodescalarview/subscript(_:)-57h51.md)
  Accesses the element at the specified position.
- [subscript<R>(R) -> Self.SubSequence](substring/unicodescalarview/subscript(_:)-7ylky.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](substring/unicodescalarview/subscript(_:)-9p7x7.md)
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](substring/unicodescalarview/subscript(_:)-zsz3.md)
  Accesses a view of this collection with the elements at the given indices.
### Type Aliases
- [Substring.UnicodeScalarView.Index](substring/unicodescalarview/index.md)
  A type that represents a position in the collection.
- [Substring.UnicodeScalarView.Indices](substring/unicodescalarview/indices-swift.typealias.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Substring.UnicodeScalarView.Iterator](substring/unicodescalarview/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [Substring.UnicodeScalarView.SubSequence](substring/unicodescalarview/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/unicodescalarview/collection-implementations)*