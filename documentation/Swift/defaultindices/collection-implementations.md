# Collection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var count: Int](defaultindices/count.md)
  The number of elements in the collection.
- [var endIndex: DefaultIndices<Elements>.Index](defaultindices/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var first: Self.Element?](defaultindices/first.md)
  The first element of the collection.
- [var indices: DefaultIndices<Elements>.Indices](defaultindices/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](defaultindices/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: DefaultIndices<Elements>.Index](defaultindices/startindex.md)
  The position of the first element in a nonempty collection.
- [var underestimatedCount: Int](defaultindices/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func distance(from: DefaultIndices<Elements>.Index, to: DefaultIndices<Elements>.Index) -> Int](defaultindices/distance(from:to:).md)
  Returns the distance between two indices.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](defaultindices/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](defaultindices/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](defaultindices/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func firstIndex(of: Self.Element) -> Self.Index?](defaultindices/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](defaultindices/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](defaultindices/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](defaultindices/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout DefaultIndices<Elements>.Index)](defaultindices/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(DefaultIndices<Elements>.Index, offsetBy: Int) -> DefaultIndices<Elements>.Index](defaultindices/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(DefaultIndices<Elements>.Index, offsetBy: Int, limitedBy: DefaultIndices<Elements>.Index) -> DefaultIndices<Elements>.Index?](defaultindices/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: DefaultIndices<Elements>.Index) -> DefaultIndices<Elements>.Index](defaultindices/index(after:).md)
  Returns the position immediately after the given index.
- [func index(of: Self.Element) -> Self.Index?](defaultindices/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](defaultindices/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](defaultindices/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func makeIterator() -> IndexingIterator<Self>](defaultindices/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](defaultindices/map(_:)-5p6p7.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func popFirst() -> Self.Element?](defaultindices/popfirst.md)
  Removes and returns the first element of the collection.
- [func prefix(Int) -> Self.SubSequence](defaultindices/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](defaultindices/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](defaultindices/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](defaultindices/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](defaultindices/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](defaultindices/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removeFirst() -> Self.Element](defaultindices/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](defaultindices/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](defaultindices/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](defaultindices/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](defaultindices/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(Int) -> Self.SubSequence](defaultindices/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](defaultindices/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript(DefaultIndices<Elements>.Index) -> Elements.Index](defaultindices/subscript(_:)-1grsk.md)
  Accesses the element at the specified position.
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](defaultindices/subscript(_:)-392od.md)
  Accesses a view of this collection with the elements at the given indices.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](defaultindices/subscript(_:)-4ala2.md)
- [subscript<R>(R) -> Self.SubSequence](defaultindices/subscript(_:)-4h7sp.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(Range<DefaultIndices<Elements>.Index>) -> DefaultIndices<Elements>](defaultindices/subscript(_:)-8o3ct.md)
  Accesses a contiguous subrange of the collection’s elements.
### Type Aliases
- [DefaultIndices.Index](defaultindices/index.md)
  A type that represents a position in the collection.
- [DefaultIndices.Indices](defaultindices/indices-swift.typealias.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [DefaultIndices.Iterator](defaultindices/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [DefaultIndices.SubSequence](defaultindices/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/defaultindices/collection-implementations)*