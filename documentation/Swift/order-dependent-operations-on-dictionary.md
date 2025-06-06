# Order Dependent Operations on Dictionary

**Framework**: Swift

Perform order-dependent operations common to all collections, as implemented for `Dictionary`.

## Topics

### Comparing Dictionaries
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](dictionary/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](dictionary/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](dictionary/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
### Manipulating Indices
- [var startIndex: Dictionary<Key, Value>.Index](dictionary/startindex.md)
  The position of the first element in a nonempty dictionary.
- [var endIndex: Dictionary<Key, Value>.Index](dictionary/endindex.md)
  The dictionary’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [func index(after: Dictionary<Key, Value>.Index) -> Dictionary<Key, Value>.Index](dictionary/index(after:).md)
  Returns the position immediately after the given index.
- [func formIndex(after: inout Dictionary<Key, Value>.Index)](dictionary/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](dictionary/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func formIndex(inout Self.Index, offsetBy: Int)](dictionary/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](dictionary/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](dictionary/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func distance(from: Self.Index, to: Self.Index) -> Int](dictionary/distance(from:to:).md)
  Returns the distance between two indices.
- [var indices: DefaultIndices<Self>](dictionary/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
### Selecting Elements
- [subscript(Range<Self.Index>) -> Slice<Self>](dictionary/subscript(_:)-2ny9y.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript<R>(R) -> Self.SubSequence](dictionary/subscript(_:)-4h7sk.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](dictionary/subscript(_:)-4al9z.md)
- [func prefix(Int) -> Self.SubSequence](dictionary/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](dictionary/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](dictionary/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](dictionary/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func suffix(Int) -> Self.SubSequence](dictionary/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](dictionary/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Excluding Elements
- [func dropFirst(Int) -> Self.SubSequence](dictionary/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](dictionary/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropLast(Int) -> Self.SubSequence](dictionary/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func popFirst() -> Dictionary<Key, Value>.Element?](dictionary/popfirst.md)
  Removes and returns the first key-value pair of the dictionary if the dictionary isn’t empty.
### Transforming a Dictionary’s Elements
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](dictionary/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func reversed() -> [Self.Element]](dictionary/reversed.md)
  Returns an array containing the elements of this sequence in reverse order.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](dictionary/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/order-dependent-operations-on-dictionary)*