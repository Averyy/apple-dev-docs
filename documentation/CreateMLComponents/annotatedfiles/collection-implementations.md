# Collection Implementations

**Framework**: Create ML Components

## Topics

### Instance Properties
- [var count: Int](annotatedfiles/count.md)
  The number of elements in the collection.
- [var first: Self.Element?](annotatedfiles/first.md)
  The first element of the collection.
- [var indices: DefaultIndices<Self>](annotatedfiles/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](annotatedfiles/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var underestimatedCount: Int](annotatedfiles/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func distance(from: Self.Index, to: Self.Index) -> Int](annotatedfiles/distance(from:to:).md)
  Returns the distance between two indices.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](annotatedfiles/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](annotatedfiles/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](annotatedfiles/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func firstIndex(of: Self.Element) -> Self.Index?](annotatedfiles/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](annotatedfiles/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func firstRange<C>(of: C) -> Range<Self.Index>?](annotatedfiles/firstrange(of:).md)
  Finds and returns the range of the first occurrence of a given collection within this collection.
- [func formIndex(inout Self.Index, offsetBy: Int)](annotatedfiles/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](annotatedfiles/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](annotatedfiles/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](annotatedfiles/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](annotatedfiles/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(of: Self.Element) -> Self.Index?](annotatedfiles/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](annotatedfiles/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](annotatedfiles/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func makeIterator() -> IndexingIterator<Self>](annotatedfiles/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](annotatedfiles/map(_:)-t09c.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(Int) -> Self.SubSequence](annotatedfiles/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](annotatedfiles/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](annotatedfiles/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](annotatedfiles/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](annotatedfiles/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](annotatedfiles/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func ranges<C>(of: C) -> [Range<Self.Index>]](annotatedfiles/ranges(of:).md)
  Finds and returns the ranges of the all occurrences of a given sequence within the collection.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](annotatedfiles/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](annotatedfiles/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](annotatedfiles/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(Int) -> Self.SubSequence](annotatedfiles/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](annotatedfiles/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
- [func trimmingPrefix<Prefix>(Prefix) -> Self.SubSequence](annotatedfiles/trimmingprefix(_:).md)
  Returns a new collection of the same type by removing `prefix` from the start of the collection.
- [func trimmingPrefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](annotatedfiles/trimmingprefix(while:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/annotatedfiles/collection-implementations)*