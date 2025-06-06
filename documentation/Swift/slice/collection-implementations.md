# Collection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var count: Int](slice/count.md)
  The number of elements in the collection.
- [var endIndex: Slice<Base>.Index](slice/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var first: Self.Element?](slice/first.md)
  The first element of the collection.
- [var indices: Slice<Base>.Indices](slice/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](slice/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: Slice<Base>.Index](slice/startindex.md)
  The position of the first element in a nonempty collection.
- [var underestimatedCount: Int](slice/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func distance(from: Slice<Base>.Index, to: Slice<Base>.Index) -> Int](slice/distance(from:to:).md)
  Returns the distance between two indices.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](slice/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](slice/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](slice/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func firstIndex(of: Self.Element) -> Self.Index?](slice/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](slice/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](slice/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](slice/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Slice<Base>.Index)](slice/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(Slice<Base>.Index, offsetBy: Int) -> Slice<Base>.Index](slice/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Slice<Base>.Index, offsetBy: Int, limitedBy: Slice<Base>.Index) -> Slice<Base>.Index?](slice/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Slice<Base>.Index) -> Slice<Base>.Index](slice/index(after:).md)
  Returns the position immediately after the given index.
- [func index(of: Self.Element) -> Self.Index?](slice/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](slice/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](slice/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func makeIterator() -> IndexingIterator<Self>](slice/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](slice/map(_:)-3jfli.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func popFirst() -> Self.Element?](slice/popfirst.md)
  Removes and returns the first element of the collection.
- [func prefix(Int) -> Self.SubSequence](slice/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](slice/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](slice/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](slice/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](slice/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](slice/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removeFirst() -> Self.Element](slice/removefirst-2564w.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](slice/removefirst(_:)-3pkd7.md)
  Removes the specified number of elements from the beginning of the collection.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](slice/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](slice/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](slice/split(separator:maxsplits:omittingemptysubsequences:)-5z4op.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(Int) -> Self.SubSequence](slice/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](slice/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript(Slice<Base>.Index) -> Base.Element](slice/subscript(_:)-1rloy.md)
  Accesses the element at the specified position.
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](slice/subscript(_:)-3p40a.md)
  Accesses a view of this collection with the elements at the given indices.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](slice/subscript(_:)-520wp.md)
- [subscript(Range<Slice<Base>.Index>) -> Slice<Base>](slice/subscript(_:)-5pgrv.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript<R>(R) -> Self.SubSequence](slice/subscript(_:)-5rdkr.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(Range<Self.Index>) -> Slice<Self>](slice/subscript(_:)-7bg96.md)
  Accesses a contiguous subrange of the collection’s elements.
### Type Aliases
- [typealias Index](slice/index.md)
  A type that represents a position in the collection.
- [typealias Indices](slice/indices-swift.typealias.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [typealias Iterator](slice/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [typealias SubSequence](slice/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/collection-implementations)*