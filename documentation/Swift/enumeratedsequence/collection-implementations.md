# Collection Implementations

**Framework**: Swift

## Topics

### Structures
- [EnumeratedSequence.Index](enumeratedsequence/index.md)
  A type that represents a position in the collection.
### Instance Properties
- [var count: Int](enumeratedsequence/count.md)
  The number of elements in the collection.
- [var count: Int](enumeratedsequence/count-3o2fx.md)
  The number of elements in the collection.
- [var endIndex: EnumeratedSequence<Base>.Index](enumeratedsequence/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: DefaultIndices<Self>](enumeratedsequence/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](enumeratedsequence/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var isEmpty: Bool](enumeratedsequence/isempty-1yllc.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: EnumeratedSequence<Base>.Index](enumeratedsequence/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func distance(from: EnumeratedSequence<Base>.Index, to: EnumeratedSequence<Base>.Index) -> Int](enumeratedsequence/distance(from:to:).md)
  Returns the distance between two indices.
- [func distance(from: Self.Index, to: Self.Index) -> Int](enumeratedsequence/distance(from:to:)-6kmqj.md)
  Returns the distance between two indices.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](enumeratedsequence/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](enumeratedsequence/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](enumeratedsequence/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](enumeratedsequence/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(EnumeratedSequence<Base>.Index, offsetBy: Int) -> EnumeratedSequence<Base>.Index](enumeratedsequence/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](enumeratedsequence/index(_:offsetby:)-4bcg9.md)
  Returns an index that is the specified distance from the given index.
- [func index(EnumeratedSequence<Base>.Index, offsetBy: Int, limitedBy: EnumeratedSequence<Base>.Index) -> EnumeratedSequence<Base>.Index?](enumeratedsequence/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](enumeratedsequence/index(_:offsetby:limitedby:)-4rme3.md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: EnumeratedSequence<Base>.Index) -> EnumeratedSequence<Base>.Index](enumeratedsequence/index(after:).md)
  Returns the position immediately after the given index.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](enumeratedsequence/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](enumeratedsequence/map(_:)-9le0.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(through: Self.Index) -> Self.SubSequence](enumeratedsequence/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](enumeratedsequence/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func randomElement() -> Self.Element?](enumeratedsequence/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](enumeratedsequence/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](enumeratedsequence/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func suffix(from: Self.Index) -> Self.SubSequence](enumeratedsequence/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript(EnumeratedSequence<Base>.Index) -> EnumeratedSequence<Base>.Element](enumeratedsequence/subscript(_:).md)
  Accesses the element at the specified position.
- [subscript(Range<Self.Index>) -> Slice<Self>](enumeratedsequence/subscript(_:)-5gng6.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](enumeratedsequence/subscript(_:)-7y5my.md)
- [subscript<R>(R) -> Self.SubSequence](enumeratedsequence/subscript(_:)-8ubal.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](enumeratedsequence/subscript(_:)-91gqg.md)
  Accesses a view of this collection with the elements at the given indices.
### Type Aliases
- [EnumeratedSequence.Indices](enumeratedsequence/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [EnumeratedSequence.SubSequence](enumeratedsequence/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/enumeratedsequence/collection-implementations)*