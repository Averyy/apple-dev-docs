# Collection Implementations

**Framework**: Swift

## Topics

### Structures
- [CollectionDifference.Index](collectiondifference/index.md)
  The position of a collection difference.
### Instance Properties
- [var count: Int](collectiondifference/count.md)
  The number of elements in the collection.
- [var endIndex: CollectionDifference<ChangeElement>.Index](collectiondifference/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var first: Self.Element?](collectiondifference/first.md)
  The first element of the collection.
- [var indices: DefaultIndices<Self>](collectiondifference/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](collectiondifference/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: CollectionDifference<ChangeElement>.Index](collectiondifference/startindex.md)
  The position of the first element in a nonempty collection.
- [var underestimatedCount: Int](collectiondifference/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func distance(from: CollectionDifference<ChangeElement>.Index, to: CollectionDifference<ChangeElement>.Index) -> Int](collectiondifference/distance(from:to:).md)
  Returns the distance between two indices.
- [func distance(from: Self.Index, to: Self.Index) -> Int](collectiondifference/distance(from:to:)-945d8.md)
  Returns the distance between two indices.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](collectiondifference/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](collectiondifference/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](collectiondifference/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func firstIndex(of: Self.Element) -> Self.Index?](collectiondifference/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](collectiondifference/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](collectiondifference/formindex(_:offsetby:)-21k4b.md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](collectiondifference/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](collectiondifference/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](collectiondifference/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](collectiondifference/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: CollectionDifference<ChangeElement>.Index) -> CollectionDifference<ChangeElement>.Index](collectiondifference/index(after:).md)
  Returns the position immediately after the given index.
- [func index(of: Self.Element) -> Self.Index?](collectiondifference/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](collectiondifference/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](collectiondifference/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func makeIterator() -> IndexingIterator<Self>](collectiondifference/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](collectiondifference/map(_:)-zouk.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(Int) -> Self.SubSequence](collectiondifference/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](collectiondifference/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](collectiondifference/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](collectiondifference/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](collectiondifference/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](collectiondifference/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](collectiondifference/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](collectiondifference/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](collectiondifference/split(separator:maxsplits:omittingemptysubsequences:)-1dhc.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(Int) -> Self.SubSequence](collectiondifference/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](collectiondifference/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript(CollectionDifference<ChangeElement>.Index) -> CollectionDifference<ChangeElement>.Element](collectiondifference/subscript(_:).md)
  Accesses the element at the specified position.
- [subscript(Range<Self.Index>) -> Slice<Self>](collectiondifference/subscript(_:)-22qdy.md)
  Accesses a contiguous subrange of the collection’s elements.
### Type Aliases
- [CollectionDifference.Indices](collectiondifference/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [CollectionDifference.Iterator](collectiondifference/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [CollectionDifference.SubSequence](collectiondifference/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collectiondifference/collection-implementations)*