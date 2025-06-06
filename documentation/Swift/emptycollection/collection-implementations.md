# Collection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var count: Int](emptycollection/count.md)
  The number of elements (always zero).
- [var first: Self.Element?](emptycollection/first.md)
  The first element of the collection.
- [var isEmpty: Bool](emptycollection/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var underestimatedCount: Int](emptycollection/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](emptycollection/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](emptycollection/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func firstIndex(of: Self.Element) -> Self.Index?](emptycollection/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](emptycollection/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](emptycollection/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](emptycollection/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](emptycollection/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(of: Self.Element) -> Self.Index?](emptycollection/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](emptycollection/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](emptycollection/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](emptycollection/map(_:)-6q1dq.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func popFirst() -> Self.Element?](emptycollection/popfirst.md)
  Removes and returns the first element of the collection.
- [func prefix(Int) -> Self.SubSequence](emptycollection/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](emptycollection/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](emptycollection/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](emptycollection/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](emptycollection/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](emptycollection/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removeFirst() -> Self.Element](emptycollection/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](emptycollection/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](emptycollection/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](emptycollection/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](emptycollection/split(separator:maxsplits:omittingemptysubsequences:)-4mogv.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(from: Self.Index) -> Self.SubSequence](emptycollection/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript<R>(R) -> Self.SubSequence](emptycollection/subscript(_:)-2eo9o.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](emptycollection/subscript(_:)-4a2g8.md)
  Accesses a view of this collection with the elements at the given indices.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](emptycollection/subscript(_:)-th66.md)
### Type Aliases
- [EmptyCollection.Indices](emptycollection/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [EmptyCollection.SubSequence](emptycollection/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/emptycollection/collection-implementations)*