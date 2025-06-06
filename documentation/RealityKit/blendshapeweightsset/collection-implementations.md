# Collection Implementations

**Framework**: RealityKit

## Topics

### Instance Properties
- [var endIndex: BlendShapeWeightsSet.Index](blendshapeweightsset/endindex.md)
  The index of the last entry in a non-empty set.
- [var first: Self.Element?](blendshapeweightsset/first.md)
  The first element of the collection.
- [var indices: DefaultIndices<Self>](blendshapeweightsset/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var startIndex: BlendShapeWeightsSet.Index](blendshapeweightsset/startindex.md)
  The index of the first entry in a non-empty set.
- [var underestimatedCount: Int](blendshapeweightsset/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func distance(from: Self.Index, to: Self.Index) -> Int](blendshapeweightsset/distance(from:to:).md)
  Returns the distance between two indices.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](blendshapeweightsset/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](blendshapeweightsset/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](blendshapeweightsset/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](blendshapeweightsset/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](blendshapeweightsset/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](blendshapeweightsset/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](blendshapeweightsset/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](blendshapeweightsset/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](blendshapeweightsset/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: BlendShapeWeightsSet.Index) -> BlendShapeWeightsSet.Index](blendshapeweightsset/index(after:).md)
  Returns the index after the given index.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](blendshapeweightsset/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](blendshapeweightsset/map(_:)-8jjb3.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(Int) -> Self.SubSequence](blendshapeweightsset/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](blendshapeweightsset/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](blendshapeweightsset/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](blendshapeweightsset/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](blendshapeweightsset/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](blendshapeweightsset/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](blendshapeweightsset/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](blendshapeweightsset/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func suffix(Int) -> Self.SubSequence](blendshapeweightsset/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](blendshapeweightsset/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
- [func trimmingPrefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](blendshapeweightsset/trimmingprefix(while:).md)
### Subscripts
- [subscript(BlendShapeWeightsSet.Index) -> BlendShapeWeightsSet.Element](blendshapeweightsset/subscript(_:)-9wfe8.md)
  Accesses the blend shape weights data at the specified index.
### Type Aliases
- [BlendShapeWeightsSet.Index](blendshapeweightsset/index.md)
  A type that represents a position in the collection.
- [BlendShapeWeightsSet.Indices](blendshapeweightsset/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [BlendShapeWeightsSet.SubSequence](blendshapeweightsset/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendshapeweightsset/collection-implementations)*