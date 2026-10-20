# Order Dependent Operations on Set

**Framework**: Swift  
**Role**: API Collection

Perform order-dependent operations common to all collections, as implemented for `Set`.

## Topics

### Manipulating Indices
- [var startIndex: Set<Element>.Index](./set/startindex.md)
  The starting position for iterating members of the set.
- [var endIndex: Set<Element>.Index](./set/endindex.md)
  The “past the end” position for the set—that is, the position one greater than the last valid subscript argument.
- [func index(after: Set<Element>.Index) -> Set<Element>.Index](./set/index%28after%29.md)
  Returns the position immediately after the given index.
- [func formIndex(after: inout Set<Element>.Index)](./set/formindex%28after%29.md)
  Replaces the given index with its successor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](./set/index%28_,offsetby%29.md)
  Returns an index that is the specified distance from the given index.
- [func formIndex(inout Self.Index, offsetBy: Int)](./set/formindex%28_,offsetby%29.md)
  Offsets the given index by the specified distance.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](./set/index%28_,offsetby,limitedby%29.md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](./set/formindex%28_,offsetby,limitedby%29.md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func distance(from: Self.Index, to: Self.Index) -> Int](./set/distance%28from,to%29.md)
  Returns the distance between two indices.
- [var indices: DefaultIndices<Self>](./set/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
### Comparing Sets
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](./set/elementsequal%28_%29.md)
  Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](./set/elementsequal%28_,by%29.md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence) -> Bool](./set/lexicographicallyprecedes%28_%29.md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](./set/lexicographicallyprecedes%28_,by%29.md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](./set/starts%28with%29.md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](./set/starts%28with,by%29.md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
### Selecting Elements
- [subscript(Set<Element>.Index) -> Element](./set/subscript%28_%29.md)
  Accesses the member at the given position.
- [func prefix(Int) -> Self.SubSequence](./set/prefix%28_%29.md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](./set/prefix%28upto%29.md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(through: Self.Index) -> Self.SubSequence](./set/prefix%28through%29.md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](./set/prefix%28while%29.md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func suffix(Int) -> Self.SubSequence](./set/suffix%28_%29.md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](./set/suffix%28from%29.md)
  Returns a subsequence from the specified position to the end of the collection.
### Excluding Elements
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](./set/drop%28while%29.md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](./set/dropfirst%28_%29.md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](./set/droplast%28_%29.md)
  Returns a subsequence containing all but the specified number of final elements.
- [func popFirst() -> Element?](./set/popfirst%28%29.md)
  Removes and returns the first element of the set.
### Reversing a Set’s Elements
- [func reversed() -> [Self.Element]](./set/reversed%28%29.md)
  Returns an array containing the elements of this sequence in reverse order.
### Splitting and Joining Elements
- [func joined() -> FlattenSequence<Self>](./set/joined%28%29.md)
  Returns the elements of this sequence of sequences, concatenated.
- [func joined<Separator>(separator: Separator) -> JoinedSequence<Self>](./set/joined%28separator%29-7ubey.md)
  Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
- [func joined(separator: String) -> String](./set/joined%28separator%29-1cko4.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](./set/split%28separator,maxsplits,omittingemptysubsequences%29.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](./set/split%28maxsplits,omittingemptysubsequences,whereseparator%29.md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/order-dependent-operations-on-set)*