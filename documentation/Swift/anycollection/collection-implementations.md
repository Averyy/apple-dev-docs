# Collection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var count: Int](anycollection/count.md)
  The number of elements.
- [var endIndex: AnyCollection<Element>.Index](anycollection/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var first: Self.Element?](anycollection/first.md)
  The first element of the collection.
- [var indices: DefaultIndices<Self>](anycollection/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](anycollection/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: AnyCollection<Element>.Index](anycollection/startindex.md)
  The position of the first element in a non-empty collection.
### Instance Methods
- [func distance(from: AnyCollection<Element>.Index, to: AnyCollection<Element>.Index) -> Int](anycollection/distance(from:to:).md)
  Returns the distance between two indices.
- [func firstIndex(of: Self.Element) -> Self.Index?](anycollection/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](anycollection/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(after: inout AnyCollection<Element>.Index)](anycollection/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(AnyCollection<Element>.Index, offsetBy: Int) -> AnyCollection<Element>.Index](anycollection/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(AnyCollection<Element>.Index, offsetBy: Int, limitedBy: AnyCollection<Element>.Index) -> AnyCollection<Element>.Index?](anycollection/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: AnyCollection<Element>.Index) -> AnyCollection<Element>.Index](anycollection/index(after:).md)
  Returns the position immediately after the given index.
- [func index(of: Self.Element) -> Self.Index?](anycollection/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](anycollection/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](anycollection/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func makeIterator() -> AnyCollection<Element>.Iterator](anycollection/makeiterator.md)
  Returns an iterator over the elements of this collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](anycollection/map(_:)-2u3hq.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func popFirst() -> Self.Element?](anycollection/popfirst.md)
  Removes and returns the first element of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](anycollection/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](anycollection/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func randomElement() -> Self.Element?](anycollection/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](anycollection/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removeFirst() -> Self.Element](anycollection/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](anycollection/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](anycollection/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](anycollection/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](anycollection/split(separator:maxsplits:omittingemptysubsequences:)-52osm.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(from: Self.Index) -> Self.SubSequence](anycollection/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](anycollection/subscript(_:)-47haf.md)
  Accesses a view of this collection with the elements at the given indices.
- [subscript(AnyCollection<Element>.Index) -> Element](anycollection/subscript(_:)-87z1l.md)
  Accesses the element indicated by `position`.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](anycollection/subscript(_:)-9guhy.md)
- [subscript<R>(R) -> Self.SubSequence](anycollection/subscript(_:)-t0ed.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(Range<AnyCollection<Element>.Index>) -> AnyCollection<Element>.SubSequence](anycollection/subscript(_:)-vb3o.md)
  Accesses a contiguous subrange of the collection’s elements.
### Type Aliases
- [AnyCollection.Index](anycollection/index.md)
  A type that represents a position in the collection.
- [AnyCollection.Indices](anycollection/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [AnyCollection.Iterator](anycollection/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [AnyCollection.SubSequence](anycollection/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anycollection/collection-implementations)*