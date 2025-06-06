# Collection Implementations

**Framework**: Swift

## Topics

### Structures
- [Dictionary.Keys.Iterator](dictionary/keys-swift.struct/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
### Instance Properties
- [var first: Self.Element?](dictionary/keys-swift.struct/first.md)
  The first element of the collection.
- [var indices: DefaultIndices<Self>](dictionary/keys-swift.struct/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var underestimatedCount: Int](dictionary/keys-swift.struct/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Instance Methods
- [func distance(from: Self.Index, to: Self.Index) -> Int](dictionary/keys-swift.struct/distance(from:to:).md)
  Returns the distance between two indices.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](dictionary/keys-swift.struct/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](dictionary/keys-swift.struct/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](dictionary/keys-swift.struct/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func firstIndex(of: Self.Element) -> Self.Index?](dictionary/keys-swift.struct/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](dictionary/keys-swift.struct/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](dictionary/keys-swift.struct/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](dictionary/keys-swift.struct/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](dictionary/keys-swift.struct/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](dictionary/keys-swift.struct/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(of: Self.Element) -> Self.Index?](dictionary/keys-swift.struct/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func indices(of: Self.Element) -> RangeSet<Self.Index>](dictionary/keys-swift.struct/indices(of:).md)
  Returns the indices of all the elements that are equal to the given element.
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](dictionary/keys-swift.struct/indices(where:).md)
  Returns the indices of all the elements that match the given predicate.
- [func makeIterator() -> Dictionary<Key, Value>.Keys.Iterator](dictionary/keys-swift.struct/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](dictionary/keys-swift.struct/map(_:)-6ax5v.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func prefix(Int) -> Self.SubSequence](dictionary/keys-swift.struct/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](dictionary/keys-swift.struct/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](dictionary/keys-swift.struct/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](dictionary/keys-swift.struct/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](dictionary/keys-swift.struct/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](dictionary/keys-swift.struct/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](dictionary/keys-swift.struct/removingsubranges(_:).md)
  Returns a collection of the elements in this collection that are not represented by the given range set.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](dictionary/keys-swift.struct/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](dictionary/keys-swift.struct/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func suffix(Int) -> Self.SubSequence](dictionary/keys-swift.struct/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](dictionary/keys-swift.struct/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/keys-swift.struct/collection-implementations)*