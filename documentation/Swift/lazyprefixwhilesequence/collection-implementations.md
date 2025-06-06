# Collection Implementations

**Framework**: Swift

## Topics

### Structures
- [LazyPrefixWhileSequence.Index](lazyprefixwhilesequence/index.md)
  A position in a `LazyPrefixWhileCollection` or `LazyPrefixWhileBidirectionalCollection` instance.
### Instance Properties
- [var count: Int](lazyprefixwhilesequence/count.md)
  The number of elements in the collection.
- [var endIndex: LazyPrefixWhileSequence<Base>.Index](lazyprefixwhilesequence/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: DefaultIndices<Self>](lazyprefixwhilesequence/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](lazyprefixwhilesequence/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: LazyPrefixWhileSequence<Base>.Index](lazyprefixwhilesequence/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func distance(from: Self.Index, to: Self.Index) -> Int](lazyprefixwhilesequence/distance(from:to:)-5ytzv.md)
  Returns the distance between two indices.
- [func firstIndex(of: Self.Element) -> Self.Index?](lazyprefixwhilesequence/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](lazyprefixwhilesequence/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](lazyprefixwhilesequence/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](lazyprefixwhilesequence/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](lazyprefixwhilesequence/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](lazyprefixwhilesequence/index(_:offsetby:)-2y8r8.md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](lazyprefixwhilesequence/index(_:offsetby:limitedby:)-279cj.md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: LazyPrefixWhileSequence<Base>.Index) -> LazyPrefixWhileSequence<Base>.Index](lazyprefixwhilesequence/index(after:).md)
  Returns the position immediately after the given index.
- [func index(of: Self.Element) -> Self.Index?](lazyprefixwhilesequence/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](lazyprefixwhilesequence/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](lazyprefixwhilesequence/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](lazyprefixwhilesequence/map(_:)-69szl.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(through: Self.Index) -> Self.SubSequence](lazyprefixwhilesequence/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](lazyprefixwhilesequence/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func randomElement() -> Self.Element?](lazyprefixwhilesequence/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](lazyprefixwhilesequence/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](lazyprefixwhilesequence/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](lazyprefixwhilesequence/split(separator:maxsplits:omittingemptysubsequences:)-1na6p.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(from: Self.Index) -> Self.SubSequence](lazyprefixwhilesequence/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript(LazyPrefixWhileSequence<Base>.Index) -> LazyPrefixWhileSequence<Base>.Element](lazyprefixwhilesequence/subscript(_:).md)
  Accesses the element at the specified position.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](lazyprefixwhilesequence/subscript(_:)-1oo1v.md)
- [subscript(Range<Self.Index>) -> Slice<Self>](lazyprefixwhilesequence/subscript(_:)-59k49.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](lazyprefixwhilesequence/subscript(_:)-75yeo.md)
  Accesses a view of this collection with the elements at the given indices.
- [subscript<R>(R) -> Self.SubSequence](lazyprefixwhilesequence/subscript(_:)-9tkrc.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
### Type Aliases
- [LazyPrefixWhileSequence.Indices](lazyprefixwhilesequence/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [LazyPrefixWhileSequence.SubSequence](lazyprefixwhilesequence/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazyprefixwhilesequence/collection-implementations)*