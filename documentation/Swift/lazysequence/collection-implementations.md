# Collection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var count: Int](lazysequence/count.md)
  Returns the number of elements.
- [var count: Int](lazysequence/count-1cggd.md)
  The number of elements in the collection.
- [var endIndex: LazySequence<Base>.Index](lazysequence/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: LazySequence<Base>.Indices](lazysequence/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](lazysequence/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var isEmpty: Bool](lazysequence/isempty-1upms.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: LazySequence<Base>.Index](lazysequence/startindex.md)
  The position of the first element in a non-empty collection.
### Instance Methods
- [func distance(from: LazySequence<Base>.Index, to: LazySequence<Base>.Index) -> Int](lazysequence/distance(from:to:).md)
  Returns the distance between two indices.
- [func distance(from: Self.Index, to: Self.Index) -> Int](lazysequence/distance(from:to:)-396sb.md)
  Returns the distance between two indices.
- [func firstIndex(of: Self.Element) -> Self.Index?](lazysequence/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](lazysequence/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](lazysequence/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](lazysequence/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](lazysequence/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(LazySequence<Base>.Index, offsetBy: Int) -> LazySequence<Base>.Index](lazysequence/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](lazysequence/index(_:offsetby:)-t8sl.md)
  Returns an index that is the specified distance from the given index.
- [func index(LazySequence<Base>.Index, offsetBy: Int, limitedBy: LazySequence<Base>.Index) -> LazySequence<Base>.Index?](lazysequence/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](lazysequence/index(_:offsetby:limitedby:)-62vws.md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: LazySequence<Base>.Index) -> LazySequence<Base>.Index](lazysequence/index(after:).md)
  Returns the position immediately after the given index.
- [func index(of: Self.Element) -> Self.Index?](lazysequence/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](lazysequence/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](lazysequence/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func makeIterator() -> LazySequence<Base>.Iterator](lazysequence/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](lazysequence/map(_:)-7wx5z.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(through: Self.Index) -> Self.SubSequence](lazysequence/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](lazysequence/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func randomElement() -> Self.Element?](lazysequence/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](lazysequence/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](lazysequence/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](lazysequence/split(separator:maxsplits:omittingemptysubsequences:)-ki1c.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(from: Self.Index) -> Self.SubSequence](lazysequence/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript(LazySequence<Base>.Index) -> LazySequence<Base>.Element](lazysequence/subscript(_:).md)
  Accesses the element at `position`.
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](lazysequence/subscript(_:)-1iwxl.md)
  Accesses a view of this collection with the elements at the given indices.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](lazysequence/subscript(_:)-1rlj.md)
- [subscript(Range<Self.Index>) -> Slice<Self>](lazysequence/subscript(_:)-8iflg.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript<R>(R) -> Self.SubSequence](lazysequence/subscript(_:)-9kt1v.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
### Type Aliases
- [LazySequence.Index](lazysequence/index.md)
  A type that represents a valid position in the collection.
- [LazySequence.Indices](lazysequence/indices-swift.typealias.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [LazySequence.Iterator](lazysequence/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [LazySequence.SubSequence](lazysequence/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazysequence/collection-implementations)*