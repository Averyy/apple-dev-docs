# Collection Implementations

**Framework**: Swift

## Topics

### Structures
- [DiscontiguousSlice.Index](discontiguousslice/index.md)
  A position in a `DiscontiguousSlice`.
### Instance Properties
- [var count: Int](discontiguousslice/count.md)
  The number of elements in the collection.
- [var count: Int](discontiguousslice/count-37f7u.md)
  The number of elements in the collection.
- [var endIndex: DiscontiguousSlice<Base>.Index](discontiguousslice/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var first: Self.Element?](discontiguousslice/first.md)
  The first element of the collection.
- [var indices: DefaultIndices<Self>](discontiguousslice/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](discontiguousslice/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var isEmpty: Bool](discontiguousslice/isempty-6y6jl.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: DiscontiguousSlice<Base>.Index](discontiguousslice/startindex.md)
  The position of the first element in a nonempty collection.
- [var underestimatedCount: Int](discontiguousslice/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func distance(from: DiscontiguousSlice<Base>.Index, to: DiscontiguousSlice<Base>.Index) -> Int](discontiguousslice/distance(from:to:).md)
  Returns the distance between two indices.
- [func distance(from: Self.Index, to: Self.Index) -> Int](discontiguousslice/distance(from:to:)-7p9uz.md)
  Returns the distance between two indices.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](discontiguousslice/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](discontiguousslice/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](discontiguousslice/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func firstIndex(of: Self.Element) -> Self.Index?](discontiguousslice/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](discontiguousslice/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](discontiguousslice/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](discontiguousslice/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](discontiguousslice/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](discontiguousslice/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](discontiguousslice/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: DiscontiguousSlice<Base>.Index) -> DiscontiguousSlice<Base>.Index](discontiguousslice/index(after:).md)
  Returns the position immediately after the given index.
- [func index(of: Self.Element) -> Self.Index?](discontiguousslice/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](discontiguousslice/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](discontiguousslice/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func makeIterator() -> IndexingIterator<Self>](discontiguousslice/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](discontiguousslice/map(_:)-44xuh.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func popFirst() -> Self.Element?](discontiguousslice/popfirst.md)
  Removes and returns the first element of the collection.
- [func prefix(Int) -> Self.SubSequence](discontiguousslice/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](discontiguousslice/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](discontiguousslice/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](discontiguousslice/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](discontiguousslice/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](discontiguousslice/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removeFirst() -> Self.Element](discontiguousslice/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](discontiguousslice/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](discontiguousslice/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](discontiguousslice/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](discontiguousslice/split(separator:maxsplits:omittingemptysubsequences:)-5ji1p.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(Int) -> Self.SubSequence](discontiguousslice/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](discontiguousslice/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript(Range<DiscontiguousSlice<Base>.Index>) -> DiscontiguousSlice<Base>](discontiguousslice/subscript(_:)-1ra8t.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](discontiguousslice/subscript(_:)-1ytel.md)
- [subscript(DiscontiguousSlice<Base>.Index) -> Base.Element](discontiguousslice/subscript(_:)-8h9i0.md)
  Accesses the element at the specified position.
### Type Aliases
- [DiscontiguousSlice.Indices](discontiguousslice/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [DiscontiguousSlice.SubSequence](discontiguousslice/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/discontiguousslice/collection-implementations)*