# Collection Implementations

**Framework**: RealityKit

## Topics

### Instance Properties
- [var endIndex: Int](meshinstancecollection/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var first: Self.Element?](meshinstancecollection/first.md)
  The first element of the collection.
- [var indices: DefaultIndices<Self>](meshinstancecollection/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var startIndex: Int](meshinstancecollection/startindex.md)
  The position of the first element in a nonempty collection.
- [var underestimatedCount: Int](meshinstancecollection/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func distance(from: Self.Index, to: Self.Index) -> Int](meshinstancecollection/distance(from:to:).md)
  Returns the distance between two indices.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](meshinstancecollection/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](meshinstancecollection/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](meshinstancecollection/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](meshinstancecollection/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](meshinstancecollection/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](meshinstancecollection/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Int)](meshinstancecollection/formindex(after:).md)
  Replaces the given index with its successor.
- [func formIndex(after: inout Self.Index)](meshinstancecollection/formindex(after:)-5r8zu.md)
  Replaces the given index with its successor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](meshinstancecollection/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](meshinstancecollection/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Int) -> Int](meshinstancecollection/index(after:).md)
  Returns the position immediately after the given index.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](meshinstancecollection/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](meshinstancecollection/map(_:)-696m7.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(Int) -> Self.SubSequence](meshinstancecollection/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](meshinstancecollection/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](meshinstancecollection/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](meshinstancecollection/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](meshinstancecollection/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](meshinstancecollection/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](meshinstancecollection/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](meshinstancecollection/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func suffix(Int) -> Self.SubSequence](meshinstancecollection/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](meshinstancecollection/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
- [func trimmingPrefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](meshinstancecollection/trimmingprefix(while:).md)
### Subscripts
- [subscript(Int) -> MeshResource.Instance](meshinstancecollection/subscript(_:)-40ren.md)
  Accesses the element at the specified position.
### Type Aliases
- [MeshInstanceCollection.Index](meshinstancecollection/index.md)
  A type that represents a position in the collection.
- [MeshInstanceCollection.Indices](meshinstancecollection/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [MeshInstanceCollection.SubSequence](meshinstancecollection/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshinstancecollection/collection-implementations)*