# Collection Implementations

**Framework**: RealityKit

## Topics

### Instance Properties
- [var first: Self.Element?](ikrig/jointcollection/first.md)
  The first element of the collection.
- [var indices: DefaultIndices<Self>](ikrig/jointcollection/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var underestimatedCount: Int](ikrig/jointcollection/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func distance(from: Self.Index, to: Self.Index) -> Int](ikrig/jointcollection/distance(from:to:).md)
  Returns the distance between two indices.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](ikrig/jointcollection/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](ikrig/jointcollection/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](ikrig/jointcollection/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](ikrig/jointcollection/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](ikrig/jointcollection/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](ikrig/jointcollection/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](ikrig/jointcollection/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](ikrig/jointcollection/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](ikrig/jointcollection/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](ikrig/jointcollection/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](ikrig/jointcollection/map(_:)-67dx2.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(Int) -> Self.SubSequence](ikrig/jointcollection/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](ikrig/jointcollection/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](ikrig/jointcollection/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](ikrig/jointcollection/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](ikrig/jointcollection/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](ikrig/jointcollection/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](ikrig/jointcollection/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](ikrig/jointcollection/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func suffix(Int) -> Self.SubSequence](ikrig/jointcollection/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](ikrig/jointcollection/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
- [func trimmingPrefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](ikrig/jointcollection/trimmingprefix(while:).md)
### Subscripts
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](ikrig/jointcollection/subscript(_:)-1vxyw.md)
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](ikrig/jointcollection/subscript(_:)-2y26u.md)
  Accesses a view of this collection with the elements at the given indices.
- [subscript<R>(R) -> Self.SubSequence](ikrig/jointcollection/subscript(_:)-7rzh4.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(Range<Self.Index>) -> Slice<Self>](ikrig/jointcollection/subscript(_:)-8aa58.md)
  Accesses a contiguous subrange of the collection’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/jointcollection/collection-implementations)*