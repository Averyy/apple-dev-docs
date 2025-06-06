# Collection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var count: Int](substring/utf8view/count.md)
  The number of elements in the collection.
- [var endIndex: Substring.UTF8View.Index](substring/utf8view/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var first: Self.Element?](substring/utf8view/first.md)
  The first element of the collection.
- [var indices: Substring.UTF8View.Indices](substring/utf8view/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](substring/utf8view/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: Substring.UTF8View.Index](substring/utf8view/startindex.md)
  The position of the first element in a nonempty collection.
- [var underestimatedCount: Int](substring/utf8view/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func distance(from: Substring.UTF8View.Index, to: Substring.UTF8View.Index) -> Int](substring/utf8view/distance(from:to:).md)
  Returns the distance between two indices.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](substring/utf8view/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](substring/utf8view/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func firstIndex(of: Self.Element) -> Self.Index?](substring/utf8view/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](substring/utf8view/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](substring/utf8view/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](substring/utf8view/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Substring.UTF8View.Index)](substring/utf8view/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(Substring.UTF8View.Index, offsetBy: Int) -> Substring.UTF8View.Index](substring/utf8view/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Substring.UTF8View.Index, offsetBy: Int, limitedBy: Substring.UTF8View.Index) -> Substring.UTF8View.Index?](substring/utf8view/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Substring.UTF8View.Index) -> Substring.UTF8View.Index](substring/utf8view/index(after:).md)
  Returns the position immediately after the given index.
- [func index(of: Self.Element) -> Self.Index?](substring/utf8view/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](substring/utf8view/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](substring/utf8view/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func makeIterator() -> IndexingIterator<Self>](substring/utf8view/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](substring/utf8view/map(_:)-3dhqn.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func popFirst() -> Self.Element?](substring/utf8view/popfirst.md)
  Removes and returns the first element of the collection.
- [func prefix(Int) -> Self.SubSequence](substring/utf8view/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](substring/utf8view/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](substring/utf8view/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](substring/utf8view/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](substring/utf8view/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](substring/utf8view/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removeFirst() -> Self.Element](substring/utf8view/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](substring/utf8view/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](substring/utf8view/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](substring/utf8view/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](substring/utf8view/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(from: Self.Index) -> Self.SubSequence](substring/utf8view/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](substring/utf8view/subscript(_:)-3zacs.md)
- [subscript<R>(R) -> Self.SubSequence](substring/utf8view/subscript(_:)-6liln.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(Range<Substring.UTF8View.Index>) -> Substring.UTF8View](substring/utf8view/subscript(_:)-7hfz9.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](substring/utf8view/subscript(_:)-9ouv5.md)
  Accesses a view of this collection with the elements at the given indices.
- [subscript(Substring.UTF8View.Index) -> Substring.UTF8View.Element](substring/utf8view/subscript(_:)-goc1.md)
  Accesses the element at the specified position.
### Type Aliases
- [Substring.UTF8View.Index](substring/utf8view/index.md)
  A type that represents a position in the collection.
- [Substring.UTF8View.Indices](substring/utf8view/indices-swift.typealias.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Substring.UTF8View.Iterator](substring/utf8view/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [Substring.UTF8View.SubSequence](substring/utf8view/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/utf8view/collection-implementations)*