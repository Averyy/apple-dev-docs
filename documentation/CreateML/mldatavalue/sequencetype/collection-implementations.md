# Collection Implementations

**Framework**: Create ML

## Topics

### Instance Properties
- [var count: Int](mldatavalue/sequencetype/count.md)
  The number of elements in the collection.
- [var endIndex: MLDataValue.SequenceType.Index](mldatavalue/sequencetype/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var first: Self.Element?](mldatavalue/sequencetype/first.md)
  The first element of the collection.
- [var isEmpty: Bool](mldatavalue/sequencetype/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var startIndex: MLDataValue.SequenceType.Index](mldatavalue/sequencetype/startindex.md)
  The position of the first element in a nonempty collection.
- [var underestimatedCount: Int](mldatavalue/sequencetype/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](mldatavalue/sequencetype/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](mldatavalue/sequencetype/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func firstIndex(of: Self.Element) -> Self.Index?](mldatavalue/sequencetype/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](mldatavalue/sequencetype/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func firstRange<C>(of: C) -> Range<Self.Index>?](mldatavalue/sequencetype/firstrange(of:).md)
  Finds and returns the range of the first occurrence of a given collection within this collection.
- [func formIndex(inout Self.Index, offsetBy: Int)](mldatavalue/sequencetype/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](mldatavalue/sequencetype/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](mldatavalue/sequencetype/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(of: Self.Element) -> Self.Index?](mldatavalue/sequencetype/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](mldatavalue/sequencetype/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](mldatavalue/sequencetype/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func makeIterator() -> IndexingIterator<Self>](mldatavalue/sequencetype/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](mldatavalue/sequencetype/map(_:)-3l8fk.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(Int) -> Self.SubSequence](mldatavalue/sequencetype/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](mldatavalue/sequencetype/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](mldatavalue/sequencetype/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](mldatavalue/sequencetype/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](mldatavalue/sequencetype/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](mldatavalue/sequencetype/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func ranges<C>(of: C) -> [Range<Self.Index>]](mldatavalue/sequencetype/ranges(of:).md)
  Finds and returns the ranges of the all occurrences of a given sequence within the collection.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](mldatavalue/sequencetype/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](mldatavalue/sequencetype/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](mldatavalue/sequencetype/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(from: Self.Index) -> Self.SubSequence](mldatavalue/sequencetype/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
- [func trimmingPrefix<Prefix>(Prefix) -> Self.SubSequence](mldatavalue/sequencetype/trimmingprefix(_:).md)
  Returns a new collection of the same type by removing `prefix` from the start of the collection.
- [func trimmingPrefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](mldatavalue/sequencetype/trimmingprefix(while:).md)
### Subscripts
- [subscript(MLDataValue.SequenceType.Index) -> MLDataValue.SequenceType.Element](mldatavalue/sequencetype/subscript(_:).md)
  Accesses the element at the specified position.
### Type Aliases
- [MLDataValue.SequenceType.Index](mldatavalue/sequencetype/index.md)
  A type that represents a position in the collection.
- [MLDataValue.SequenceType.Indices](mldatavalue/sequencetype/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [MLDataValue.SequenceType.Iterator](mldatavalue/sequencetype/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [MLDataValue.SequenceType.SubSequence](mldatavalue/sequencetype/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalue/sequencetype/collection-implementations)*