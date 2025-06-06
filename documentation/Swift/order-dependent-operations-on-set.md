# Order Dependent Operations on Set

**Framework**: Swift

Perform order-dependent operations common to all collections, as implemented for `Set`.

## Topics

### Manipulating Indices
- [var startIndex: Set<Element>.Index](set/startindex.md)
  The starting position for iterating members of the set.
- [var endIndex: Set<Element>.Index](set/endindex.md)
  The “past the end” position for the set—that is, the position one greater than the last valid subscript argument.
- [func index(after: Set<Element>.Index) -> Set<Element>.Index](set/index(after:).md)
  Returns the position immediately after the given index.
- [func formIndex(after: inout Set<Element>.Index)](set/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](set/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func formIndex(inout Self.Index, offsetBy: Int)](set/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](set/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](set/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func distance(from: Self.Index, to: Self.Index) -> Int](set/distance(from:to:).md)
  Returns the distance between two indices.
- [var indices: DefaultIndices<Self>](set/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
### Comparing Sets
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](set/elementsequal(_:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](set/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence) -> Bool](set/lexicographicallyprecedes(_:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](set/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](set/starts(with:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](set/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
### Selecting Elements
- [subscript(Set<Element>.Index) -> Element](set/subscript(_:).md)
  Accesses the member at the given position.
- [func prefix(Int) -> Self.SubSequence](set/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](set/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(through: Self.Index) -> Self.SubSequence](set/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](set/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func suffix(Int) -> Self.SubSequence](set/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](set/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Excluding Elements
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](set/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](set/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](set/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func popFirst() -> Element?](set/popfirst.md)
  Removes and returns the first element of the set.
### Reversing a Set’s Elements
- [func reversed() -> [Self.Element]](set/reversed.md)
  Returns an array containing the elements of this sequence in reverse order.
### Splitting and Joining Elements
- [func joined() -> FlattenSequence<Self>](set/joined.md)
  Returns the elements of this sequence of sequences, concatenated.
- [func joined<Separator>(separator: Separator) -> JoinedSequence<Self>](set/joined(separator:)-7ubey.md)
  Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
- [func joined(separator: String) -> String](set/joined(separator:)-1cko4.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](set/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](set/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/order-dependent-operations-on-set)*