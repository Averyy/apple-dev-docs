# Collection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var count: Int](anyrandomaccesscollection/count.md)
  The number of elements.
- [var first: Self.Element?](anyrandomaccesscollection/first.md)
  The first element of the collection.
- [var indices: DefaultIndices<Self>](anyrandomaccesscollection/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](anyrandomaccesscollection/isempty.md)
  A Boolean value indicating whether the collection is empty.
### Instance Methods
- [func firstIndex(of: Self.Element) -> Self.Index?](anyrandomaccesscollection/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](anyrandomaccesscollection/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func index(of: Self.Element) -> Self.Index?](anyrandomaccesscollection/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](anyrandomaccesscollection/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](anyrandomaccesscollection/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func makeIterator() -> AnyRandomAccessCollection<Element>.Iterator](anyrandomaccesscollection/makeiterator.md)
  Returns an iterator over the elements of this collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](anyrandomaccesscollection/map(_:)-1emdw.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func popFirst() -> Self.Element?](anyrandomaccesscollection/popfirst.md)
  Removes and returns the first element of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](anyrandomaccesscollection/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](anyrandomaccesscollection/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func randomElement() -> Self.Element?](anyrandomaccesscollection/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](anyrandomaccesscollection/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removeFirst() -> Self.Element](anyrandomaccesscollection/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](anyrandomaccesscollection/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](anyrandomaccesscollection/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](anyrandomaccesscollection/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](anyrandomaccesscollection/split(separator:maxsplits:omittingemptysubsequences:)-2m0ih.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(from: Self.Index) -> Self.SubSequence](anyrandomaccesscollection/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](anyrandomaccesscollection/subscript(_:)-1ezt3.md)
  Accesses a view of this collection with the elements at the given indices.
- [subscript<R>(R) -> Self.SubSequence](anyrandomaccesscollection/subscript(_:)-9umyp.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](anyrandomaccesscollection/subscript(_:)-ui2k.md)
### Type Aliases
- [AnyRandomAccessCollection.Index](anyrandomaccesscollection/index.md)
  A type that represents a position in the collection.
- [AnyRandomAccessCollection.Indices](anyrandomaccesscollection/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [AnyRandomAccessCollection.Iterator](anyrandomaccesscollection/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [AnyRandomAccessCollection.SubSequence](anyrandomaccesscollection/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anyrandomaccesscollection/collection-implementations)*