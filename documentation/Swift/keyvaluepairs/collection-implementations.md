# Collection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var count: Int](keyvaluepairs/count.md)
  The number of elements in the collection.
- [var first: Self.Element?](keyvaluepairs/first.md)
  The first element of the collection.
- [var isEmpty: Bool](keyvaluepairs/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var underestimatedCount: Int](keyvaluepairs/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](keyvaluepairs/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](keyvaluepairs/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](keyvaluepairs/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](keyvaluepairs/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](keyvaluepairs/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](keyvaluepairs/formindex(after:).md)
  Replaces the given index with its successor.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](keyvaluepairs/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func makeIterator() -> IndexingIterator<Self>](keyvaluepairs/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](keyvaluepairs/map(_:)-8tv4p.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(Int) -> Self.SubSequence](keyvaluepairs/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](keyvaluepairs/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](keyvaluepairs/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](keyvaluepairs/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](keyvaluepairs/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](keyvaluepairs/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](keyvaluepairs/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](keyvaluepairs/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func suffix(from: Self.Index) -> Self.SubSequence](keyvaluepairs/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Type Aliases
- [KeyValuePairs.Index](keyvaluepairs/index.md)
  A type that represents a position in the collection.
- [KeyValuePairs.Indices](keyvaluepairs/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [KeyValuePairs.Iterator](keyvaluepairs/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [KeyValuePairs.SubSequence](keyvaluepairs/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyvaluepairs/collection-implementations)*