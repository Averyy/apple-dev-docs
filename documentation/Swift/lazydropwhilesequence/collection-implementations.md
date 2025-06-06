# Collection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var count: Int](lazydropwhilesequence/count.md)
  The number of elements in the collection.
- [var endIndex: LazyDropWhileSequence<Base>.Index](lazydropwhilesequence/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: DefaultIndices<Self>](lazydropwhilesequence/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](lazydropwhilesequence/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: LazyDropWhileSequence<Base>.Index](lazydropwhilesequence/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func distance(from: Self.Index, to: Self.Index) -> Int](lazydropwhilesequence/distance(from:to:)-9uku.md)
  Returns the distance between two indices.
- [func firstIndex(of: Self.Element) -> Self.Index?](lazydropwhilesequence/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](lazydropwhilesequence/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](lazydropwhilesequence/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](lazydropwhilesequence/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](lazydropwhilesequence/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](lazydropwhilesequence/index(_:offsetby:)-17asz.md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](lazydropwhilesequence/index(_:offsetby:limitedby:)-k9zq.md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: LazyDropWhileSequence<Base>.Index) -> LazyDropWhileSequence<Base>.Index](lazydropwhilesequence/index(after:).md)
  Returns the position immediately after the given index.
- [func index(of: Self.Element) -> Self.Index?](lazydropwhilesequence/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](lazydropwhilesequence/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](lazydropwhilesequence/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](lazydropwhilesequence/map(_:)-7ovhy.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(through: Self.Index) -> Self.SubSequence](lazydropwhilesequence/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](lazydropwhilesequence/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func randomElement() -> Self.Element?](lazydropwhilesequence/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](lazydropwhilesequence/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](lazydropwhilesequence/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](lazydropwhilesequence/split(separator:maxsplits:omittingemptysubsequences:)-16h0n.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(from: Self.Index) -> Self.SubSequence](lazydropwhilesequence/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript(LazyDropWhileSequence<Base>.Index) -> LazyDropWhileSequence<Base>.Element](lazydropwhilesequence/subscript(_:).md)
  Accesses the element at the specified position.
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](lazydropwhilesequence/subscript(_:)-5atki.md)
  Accesses a view of this collection with the elements at the given indices.
- [subscript(Range<Self.Index>) -> Slice<Self>](lazydropwhilesequence/subscript(_:)-7qiik.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](lazydropwhilesequence/subscript(_:)-8ifgj.md)
- [subscript<R>(R) -> Self.SubSequence](lazydropwhilesequence/subscript(_:)-jkb6.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
### Type Aliases
- [LazyDropWhileSequence.Index](lazydropwhilesequence/index.md)
  A type that represents a position in the collection.
- [LazyDropWhileSequence.Indices](lazydropwhilesequence/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [LazyDropWhileSequence.SubSequence](lazydropwhilesequence/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazydropwhilesequence/collection-implementations)*