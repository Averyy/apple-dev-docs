# Collection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var count: Int](substring/utf16view/count.md)
  The number of elements in the collection.
- [var endIndex: Substring.UTF16View.Index](substring/utf16view/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var first: Self.Element?](substring/utf16view/first.md)
  The first element of the collection.
- [var isEmpty: Bool](substring/utf16view/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: Substring.UTF16View.Index](substring/utf16view/startindex.md)
  The position of the first element in a nonempty collection.
- [var underestimatedCount: Int](substring/utf16view/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](substring/utf16view/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](substring/utf16view/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func firstIndex(of: Self.Element) -> Self.Index?](substring/utf16view/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](substring/utf16view/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](substring/utf16view/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](substring/utf16view/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func index(of: Self.Element) -> Self.Index?](substring/utf16view/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](substring/utf16view/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](substring/utf16view/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func makeIterator() -> IndexingIterator<Self>](substring/utf16view/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](substring/utf16view/map(_:)-2jwvg.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func popFirst() -> Self.Element?](substring/utf16view/popfirst.md)
  Removes and returns the first element of the collection.
- [func prefix(Int) -> Self.SubSequence](substring/utf16view/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](substring/utf16view/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](substring/utf16view/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](substring/utf16view/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](substring/utf16view/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](substring/utf16view/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removeFirst() -> Self.Element](substring/utf16view/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](substring/utf16view/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](substring/utf16view/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](substring/utf16view/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](substring/utf16view/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(from: Self.Index) -> Self.SubSequence](substring/utf16view/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript<R>(R) -> Self.SubSequence](substring/utf16view/subscript(_:)-2ljg7.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](substring/utf16view/subscript(_:)-3ijoy.md)
  Accesses a view of this collection with the elements at the given indices.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](substring/utf16view/subscript(_:)-5j3ao.md)
- [subscript(Substring.UTF16View.Index) -> Substring.UTF16View.Element](substring/utf16view/subscript(_:)-ketw.md)
  Accesses the element at the specified position.
### Type Aliases
- [Substring.UTF16View.Index](substring/utf16view/index.md)
  A type that represents a position in the collection.
- [Substring.UTF16View.Indices](substring/utf16view/indices-swift.typealias.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Substring.UTF16View.Iterator](substring/utf16view/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [Substring.UTF16View.SubSequence](substring/utf16view/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/utf16view/collection-implementations)*