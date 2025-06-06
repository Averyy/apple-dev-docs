# Collection Implementations

**Framework**: Swift

## Topics

### Structures
- [CollectionOfOne.Iterator](collectionofone/iterator.md)
  An iterator that produces one or zero instances of an element.
### Instance Properties
- [var count: Int](collectionofone/count.md)
  The number of elements in the collection, which is always one.
- [var first: Self.Element?](collectionofone/first.md)
  The first element of the collection.
- [var isEmpty: Bool](collectionofone/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var underestimatedCount: Int](collectionofone/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](collectionofone/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](collectionofone/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func firstIndex(of: Self.Element) -> Self.Index?](collectionofone/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](collectionofone/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](collectionofone/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](collectionofone/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](collectionofone/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(of: Self.Element) -> Self.Index?](collectionofone/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](collectionofone/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](collectionofone/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func makeIterator() -> CollectionOfOne<Element>.Iterator](collectionofone/makeiterator.md)
  Returns an iterator over the elements of this collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](collectionofone/map(_:)-6e1xi.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(Int) -> Self.SubSequence](collectionofone/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](collectionofone/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](collectionofone/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](collectionofone/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](collectionofone/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](collectionofone/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](collectionofone/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](collectionofone/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](collectionofone/split(separator:maxsplits:omittingemptysubsequences:)-1a0oe.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(from: Self.Index) -> Self.SubSequence](collectionofone/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript<R>(R) -> Self.SubSequence](collectionofone/subscript(_:)-3dvjk.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](collectionofone/subscript(_:)-59bql.md)
- [subscript(Range<Self.Index>) -> Slice<Self>](collectionofone/subscript(_:)-5iy5s.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](collectionofone/subscript(_:)-y23p.md)
  Accesses a view of this collection with the elements at the given indices.
### Type Aliases
- [CollectionOfOne.Index](collectionofone/index.md)
  A type that represents a position in the collection.
- [CollectionOfOne.Indices](collectionofone/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [CollectionOfOne.SubSequence](collectionofone/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collectionofone/collection-implementations)*