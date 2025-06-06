# Collection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var count: Int](lazymapsequence/count.md)
  The number of elements in the collection.
- [var count: Int](lazymapsequence/count-5qqod.md)
  The number of elements in the collection.
- [var endIndex: Base.Index](lazymapsequence/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: LazyMapSequence<Base, Element>.Indices](lazymapsequence/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](lazymapsequence/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var isEmpty: Bool](lazymapsequence/isempty-75pes.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: Base.Index](lazymapsequence/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func distance(from: LazyMapSequence<Base, Element>.Index, to: LazyMapSequence<Base, Element>.Index) -> Int](lazymapsequence/distance(from:to:).md)
  Returns the distance between two indices.
- [func distance(from: Self.Index, to: Self.Index) -> Int](lazymapsequence/distance(from:to:)-3i820.md)
  Returns the distance between two indices.
- [func firstIndex(of: Self.Element) -> Self.Index?](lazymapsequence/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](lazymapsequence/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](lazymapsequence/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](lazymapsequence/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout LazyMapSequence<Base, Element>.Index)](lazymapsequence/formindex(after:).md)
  Replaces the given index with its successor.
- [func formIndex(after: inout Self.Index)](lazymapsequence/formindex(after:)-6932e.md)
  Replaces the given index with its successor.
- [func index(LazyMapSequence<Base, Element>.Index, offsetBy: Int) -> LazyMapSequence<Base, Element>.Index](lazymapsequence/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](lazymapsequence/index(_:offsetby:)-78pdz.md)
  Returns an index that is the specified distance from the given index.
- [func index(LazyMapSequence<Base, Element>.Index, offsetBy: Int, limitedBy: LazyMapSequence<Base, Element>.Index) -> LazyMapSequence<Base, Element>.Index?](lazymapsequence/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](lazymapsequence/index(_:offsetby:limitedby:)-5uiel.md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: LazyMapSequence<Base, Element>.Index) -> LazyMapSequence<Base, Element>.Index](lazymapsequence/index(after:).md)
  Returns the position immediately after the given index.
- [func index(of: Self.Element) -> Self.Index?](lazymapsequence/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](lazymapsequence/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](lazymapsequence/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](lazymapsequence/map(_:)-8qb3x.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(through: Self.Index) -> Self.SubSequence](lazymapsequence/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](lazymapsequence/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func randomElement() -> Self.Element?](lazymapsequence/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](lazymapsequence/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](lazymapsequence/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](lazymapsequence/split(separator:maxsplits:omittingemptysubsequences:)-5eafc.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(from: Self.Index) -> Self.SubSequence](lazymapsequence/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript(Base.Index) -> Element](lazymapsequence/subscript(_:)-36b2w.md)
  Accesses the element at `position`.
- [subscript<R>(R) -> Self.SubSequence](lazymapsequence/subscript(_:)-3hxz5.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(Range<Base.Index>) -> LazyMapSequence<Base, Element>.SubSequence](lazymapsequence/subscript(_:)-4qmx0.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](lazymapsequence/subscript(_:)-4tv8v.md)
  Accesses a view of this collection with the elements at the given indices.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](lazymapsequence/subscript(_:)-88114.md)
### Type Aliases
- [LazyMapSequence.Index](lazymapsequence/index.md)
  A type that represents a position in the collection.
- [LazyMapSequence.Indices](lazymapsequence/indices-swift.typealias.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [LazyMapSequence.SubSequence](lazymapsequence/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazymapsequence/collection-implementations)*