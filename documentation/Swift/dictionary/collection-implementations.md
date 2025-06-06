# Collection Implementations

**Framework**: Swift

## Topics

### Structures
- [Dictionary.Index](dictionary/index.md)
  The position of a key-value pair in a dictionary.
### Instance Properties
- [var count: Int](dictionary/count.md)
  The number of key-value pairs in the dictionary.
- [var endIndex: Dictionary<Key, Value>.Index](dictionary/endindex.md)
  The dictionary’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var first: Self.Element?](dictionary/first.md)
  The first element of the collection.
- [var indices: DefaultIndices<Self>](dictionary/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isEmpty: Bool](dictionary/isempty.md)
  A Boolean value that indicates whether the dictionary is empty.
- [var startIndex: Dictionary<Key, Value>.Index](dictionary/startindex.md)
  The position of the first element in a nonempty dictionary.
- [var underestimatedCount: Int](dictionary/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func distance(from: Self.Index, to: Self.Index) -> Int](dictionary/distance(from:to:).md)
  Returns the distance between two indices.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](dictionary/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](dictionary/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](dictionary/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](dictionary/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](dictionary/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](dictionary/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Dictionary<Key, Value>.Index)](dictionary/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](dictionary/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](dictionary/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Dictionary<Key, Value>.Index) -> Dictionary<Key, Value>.Index](dictionary/index(after:).md)
  Returns the position immediately after the given index.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](dictionary/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](dictionary/map(_:)-5p6p2.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(Int) -> Self.SubSequence](dictionary/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](dictionary/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](dictionary/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](dictionary/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](dictionary/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](dictionary/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](dictionary/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](dictionary/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func suffix(Int) -> Self.SubSequence](dictionary/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](dictionary/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Subscripts
- [subscript(Range<Self.Index>) -> Slice<Self>](dictionary/subscript(_:)-2ny9y.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](dictionary/subscript(_:)-392o0.md)
  Accesses a view of this collection with the elements at the given indices.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](dictionary/subscript(_:)-4al9z.md)
- [subscript(Dictionary<Key, Value>.Index) -> Dictionary<Key, Value>.Element](dictionary/subscript(_:)-4bhoo.md)
  Accesses the key-value pair at the specified position.
- [subscript<R>(R) -> Self.SubSequence](dictionary/subscript(_:)-4h7sk.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
### Type Aliases
- [Dictionary.Indices](dictionary/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Dictionary.SubSequence](dictionary/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/collection-implementations)*