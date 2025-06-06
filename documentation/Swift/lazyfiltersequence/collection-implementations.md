# Collection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var count: Int](lazyfiltersequence/count.md)
  The number of elements in the collection.
- [var endIndex: LazyFilterSequence<Base>.Index](lazyfiltersequence/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: DefaultIndices<Self>](lazyfiltersequence/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](lazyfiltersequence/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: LazyFilterSequence<Base>.Index](lazyfiltersequence/startindex.md)
  The position of the first element in a non-empty collection.
### Instance Methods
- [func distance(from: LazyFilterSequence<Base>.Index, to: LazyFilterSequence<Base>.Index) -> Int](lazyfiltersequence/distance(from:to:).md)
  Returns the distance between two indices.
- [func distance(from: Self.Index, to: Self.Index) -> Int](lazyfiltersequence/distance(from:to:)-64w60.md)
  Returns the distance between two indices.
- [func firstIndex(of: Self.Element) -> Self.Index?](lazyfiltersequence/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](lazyfiltersequence/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](lazyfiltersequence/formindex(_:offsetby:)-4fulw.md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](lazyfiltersequence/formindex(_:offsetby:limitedby:)-94oyz.md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout LazyFilterSequence<Base>.Index)](lazyfiltersequence/formindex(after:).md)
  Replaces the given index with its successor.
- [func formIndex(after: inout Self.Index)](lazyfiltersequence/formindex(after:)-8eya1.md)
  Replaces the given index with its successor.
- [func index(LazyFilterSequence<Base>.Index, offsetBy: Int) -> LazyFilterSequence<Base>.Index](lazyfiltersequence/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](lazyfiltersequence/index(_:offsetby:)-ghrd.md)
  Returns an index that is the specified distance from the given index.
- [func index(LazyFilterSequence<Base>.Index, offsetBy: Int, limitedBy: LazyFilterSequence<Base>.Index) -> LazyFilterSequence<Base>.Index?](lazyfiltersequence/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](lazyfiltersequence/index(_:offsetby:limitedby:)-6rs60.md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: LazyFilterSequence<Base>.Index) -> LazyFilterSequence<Base>.Index](lazyfiltersequence/index(after:).md)
  Returns the position immediately after the given index.
- [func index(of: Self.Element) -> Self.Index?](lazyfiltersequence/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](lazyfiltersequence/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](lazyfiltersequence/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](lazyfiltersequence/map(_:)-8n620.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(through: Self.Index) -> Self.SubSequence](lazyfiltersequence/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](lazyfiltersequence/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func randomElement() -> Self.Element?](lazyfiltersequence/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](lazyfiltersequence/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](lazyfiltersequence/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](lazyfiltersequence/split(separator:maxsplits:omittingemptysubsequences:)-f04l.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(from: Self.Index) -> Self.SubSequence](lazyfiltersequence/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript(Range<LazyFilterSequence<Base>.Index>) -> LazyFilterSequence<Base>.SubSequence](lazyfiltersequence/subscript(_:)-4caas.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(LazyFilterSequence<Base>.Index) -> LazyFilterSequence<Base>.Element](lazyfiltersequence/subscript(_:)-4syjt.md)
  Accesses the element at `position`.
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](lazyfiltersequence/subscript(_:)-6uzbx.md)
  Accesses a view of this collection with the elements at the given indices.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](lazyfiltersequence/subscript(_:)-7ge85.md)
- [subscript<R>(R) -> Self.SubSequence](lazyfiltersequence/subscript(_:)-lelz.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
### Type Aliases
- [LazyFilterSequence.Index](lazyfiltersequence/index.md)
  A type that represents a valid position in the collection.
- [LazyFilterSequence.Indices](lazyfiltersequence/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [LazyFilterSequence.SubSequence](lazyfiltersequence/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazyfiltersequence/collection-implementations)*