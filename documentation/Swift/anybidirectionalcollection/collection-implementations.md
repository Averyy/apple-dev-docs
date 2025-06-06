# Collection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var count: Int](anybidirectionalcollection/count.md)
  The number of elements.
- [var first: Self.Element?](anybidirectionalcollection/first.md)
  The first element of the collection.
- [var indices: DefaultIndices<Self>](anybidirectionalcollection/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](anybidirectionalcollection/isempty.md)
  A Boolean value indicating whether the collection is empty.
### Instance Methods
- [func firstIndex(of: Self.Element) -> Self.Index?](anybidirectionalcollection/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](anybidirectionalcollection/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func index(of: Self.Element) -> Self.Index?](anybidirectionalcollection/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](anybidirectionalcollection/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](anybidirectionalcollection/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func makeIterator() -> AnyBidirectionalCollection<Element>.Iterator](anybidirectionalcollection/makeiterator.md)
  Returns an iterator over the elements of this collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](anybidirectionalcollection/map(_:)-4xfvs.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func popFirst() -> Self.Element?](anybidirectionalcollection/popfirst.md)
  Removes and returns the first element of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](anybidirectionalcollection/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](anybidirectionalcollection/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func randomElement() -> Self.Element?](anybidirectionalcollection/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](anybidirectionalcollection/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removeFirst() -> Self.Element](anybidirectionalcollection/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](anybidirectionalcollection/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](anybidirectionalcollection/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](anybidirectionalcollection/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](anybidirectionalcollection/split(separator:maxsplits:omittingemptysubsequences:)-5dxmc.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(from: Self.Index) -> Self.SubSequence](anybidirectionalcollection/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](anybidirectionalcollection/subscript(_:)-34ify.md)
- [subscript<R>(R) -> Self.SubSequence](anybidirectionalcollection/subscript(_:)-8f134.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](anybidirectionalcollection/subscript(_:)-93ijp.md)
  Accesses a view of this collection with the elements at the given indices.
### Type Aliases
- [AnyBidirectionalCollection.Index](anybidirectionalcollection/index.md)
  A type that represents a position in the collection.
- [AnyBidirectionalCollection.Indices](anybidirectionalcollection/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [AnyBidirectionalCollection.Iterator](anybidirectionalcollection/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [AnyBidirectionalCollection.SubSequence](anybidirectionalcollection/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anybidirectionalcollection/collection-implementations)*