# Collection Implementations

**Framework**: Swift

## Topics

### Structures
- [FlattenSequence.Index](flattensequence/index.md)
  A position in a FlattenCollection
### Instance Properties
- [var count: Int](flattensequence/count.md)
  The number of elements in the collection.
- [var endIndex: FlattenSequence<Base>.Index](flattensequence/endindex.md)
  The collection’s “past the end” position.
- [var indices: DefaultIndices<Self>](flattensequence/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](flattensequence/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: FlattenSequence<Base>.Index](flattensequence/startindex.md)
  The position of the first element in a non-empty collection.
### Instance Methods
- [func distance(from: FlattenSequence<Base>.Index, to: FlattenSequence<Base>.Index) -> Int](flattensequence/distance(from:to:).md)
  Returns the distance between two indices.
- [func distance(from: Self.Index, to: Self.Index) -> Int](flattensequence/distance(from:to:)-1neyu.md)
  Returns the distance between two indices.
- [func firstIndex(of: Self.Element) -> Self.Index?](flattensequence/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](flattensequence/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](flattensequence/formindex(_:offsetby:)-9h4a8.md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](flattensequence/formindex(_:offsetby:limitedby:)-5809f.md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout FlattenSequence<Base>.Index)](flattensequence/formindex(after:).md)
  Replaces the given index with its successor.
- [func formIndex(after: inout Self.Index)](flattensequence/formindex(after:)-7v0c1.md)
  Replaces the given index with its successor.
- [func index(FlattenSequence<Base>.Index, offsetBy: Int) -> FlattenSequence<Base>.Index](flattensequence/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](flattensequence/index(_:offsetby:)-20r2m.md)
  Returns an index that is the specified distance from the given index.
- [func index(FlattenSequence<Base>.Index, offsetBy: Int, limitedBy: FlattenSequence<Base>.Index) -> FlattenSequence<Base>.Index?](flattensequence/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](flattensequence/index(_:offsetby:limitedby:)-7gfpk.md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: FlattenSequence<Base>.Index) -> FlattenSequence<Base>.Index](flattensequence/index(after:).md)
  Returns the position immediately after the given index.
- [func index(of: Self.Element) -> Self.Index?](flattensequence/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](flattensequence/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](flattensequence/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](flattensequence/map(_:)-9pfsv.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(through: Self.Index) -> Self.SubSequence](flattensequence/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](flattensequence/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func randomElement() -> Self.Element?](flattensequence/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](flattensequence/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](flattensequence/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](flattensequence/split(separator:maxsplits:omittingemptysubsequences:)-9yjf5.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(from: Self.Index) -> Self.SubSequence](flattensequence/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript(Range<Self.Index>) -> Slice<Self>](flattensequence/subscript(_:)-1cq56.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(FlattenSequence<Base>.Index) -> Base.Element.Element](flattensequence/subscript(_:)-1eq7u.md)
  Accesses the element at `position`.
- [subscript(Range<FlattenSequence<Base>.Index>) -> Slice<FlattenCollection<Base>>](flattensequence/subscript(_:)-3w5sk.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](flattensequence/subscript(_:)-4nz3b.md)
  Accesses a view of this collection with the elements at the given indices.
- [subscript<R>(R) -> Self.SubSequence](flattensequence/subscript(_:)-cutv.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](flattensequence/subscript(_:)-v1s4.md)
### Type Aliases
- [FlattenSequence.Indices](flattensequence/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [FlattenSequence.SubSequence](flattensequence/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/flattensequence/collection-implementations)*