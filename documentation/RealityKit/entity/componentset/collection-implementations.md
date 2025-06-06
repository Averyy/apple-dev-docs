# Collection Implementations

**Framework**: RealityKit

## Topics

### Structures
- [Entity.ComponentSet.Index](entity/componentset/index.md)
  A type that represents a position in the collection.
- [Entity.ComponentSet.Indices](entity/componentset/indices-swift.struct.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
### Instance Properties
- [var endIndex: Entity.ComponentSet.Index](entity/componentset/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var first: Self.Element?](entity/componentset/first.md)
  The first element of the collection.
- [var indices: Entity.ComponentSet.Indices](entity/componentset/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](entity/componentset/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var isEmpty: Bool](entity/componentset/isempty-4425d.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: Entity.ComponentSet.Index](entity/componentset/startindex.md)
  The position of the first element in a nonempty collection.
- [var underestimatedCount: Int](entity/componentset/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func distance(from: Entity.ComponentSet.Index, to: Entity.ComponentSet.Index) -> Int](entity/componentset/distance(from:to:).md)
  Returns the distance between two indices.
- [func distance(from: Self.Index, to: Self.Index) -> Int](entity/componentset/distance(from:to:)-2zrgy.md)
  Returns the distance between two indices.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](entity/componentset/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](entity/componentset/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](entity/componentset/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](entity/componentset/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](entity/componentset/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](entity/componentset/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Entity.ComponentSet.Index)](entity/componentset/formindex(after:).md)
  Replaces the given index with its successor.
- [func formIndex(after: inout Self.Index)](entity/componentset/formindex(after:)-3jr5w.md)
  Replaces the given index with its successor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](entity/componentset/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](entity/componentset/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Entity.ComponentSet.Index) -> Entity.ComponentSet.Index](entity/componentset/index(after:).md)
  Returns the position immediately after the given index.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](entity/componentset/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](entity/componentset/map(_:)-46qp5.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(Int) -> Self.SubSequence](entity/componentset/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](entity/componentset/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](entity/componentset/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](entity/componentset/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](entity/componentset/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](entity/componentset/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](entity/componentset/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](entity/componentset/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func suffix(Int) -> Self.SubSequence](entity/componentset/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](entity/componentset/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
- [func trimmingPrefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](entity/componentset/trimmingprefix(while:).md)
### Subscripts
- [subscript(Entity.ComponentSet.Index) -> any Component](entity/componentset/subscript(_:)-5bllq.md)
  Accesses the element at the specified position.
### Type Aliases
- [Entity.ComponentSet.SubSequence](entity/componentset/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/collection-implementations)*