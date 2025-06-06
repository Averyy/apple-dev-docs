# Sequence Implementations

**Framework**: MusicKit

## Topics

### Instance Properties
- [var lazy: LazySequence<Self>](musicitemcollection/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [var publisher: Publishers.Sequence<Self, Never>](musicitemcollection/publisher.md)
### Instance Methods
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](musicitemcollection/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](musicitemcollection/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func compare<Comparator>(Comparator.Compared, Comparator.Compared) -> ComparisonResult](musicitemcollection/compare(_:_:).md)
  If `lhs` is ordered before `rhs` in the ordering described by the given sequence of `SortComparator`s
- [func contains(Self.Element) -> Bool](musicitemcollection/contains(_:)-512nn.md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](musicitemcollection/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func count<E>(where: (Self.Element) throws(E) -> Bool) throws(E) -> Int](musicitemcollection/count(where:).md)
  Returns the number of elements in the sequence that satisfy the given predicate.
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](musicitemcollection/elementsequal(_:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](musicitemcollection/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func enumerated() -> EnumeratedSequence<Self>](musicitemcollection/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](musicitemcollection/filter(_:).md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](musicitemcollection/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](musicitemcollection/flatmap(_:)-21yez.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](musicitemcollection/flatmap(_:)-58ib8.md)
- [func forEach((Self.Element) throws -> Void) rethrows](musicitemcollection/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func formatted() -> String](musicitemcollection/formatted.md)
- [func formatted<S>(S) -> S.FormatOutput](musicitemcollection/formatted(_:).md)
- [func joined() -> FlattenSequence<Self>](musicitemcollection/joined.md)
  Returns the elements of this sequence of sequences, concatenated.
- [func joined(separator: String) -> String](musicitemcollection/joined(separator:)-39nu7.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func joined<Separator>(separator: Separator) -> JoinedSequence<Self>](musicitemcollection/joined(separator:)-6uzne.md)
  Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence) -> Bool](musicitemcollection/lexicographicallyprecedes(_:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](musicitemcollection/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](musicitemcollection/map(_:)-7jzyg.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func max() -> Self.Element?](musicitemcollection/max.md)
  Returns the maximum element in the sequence.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](musicitemcollection/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func min() -> Self.Element?](musicitemcollection/min.md)
  Returns the minimum element in the sequence.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](musicitemcollection/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](musicitemcollection/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](musicitemcollection/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func shuffled() -> [Self.Element]](musicitemcollection/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](musicitemcollection/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [func sorted() -> [Self.Element]](musicitemcollection/sorted.md)
  Returns the elements of the sequence, sorted.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](musicitemcollection/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func sorted<Comparator>(using: Comparator) -> [Self.Element]](musicitemcollection/sorted(using:)-8uvpa.md)
  Returns the elements of the sequence, sorted using the given comparator to compare elements.
- [func sorted<S, Comparator>(using: S) -> [Self.Element]](musicitemcollection/sorted(using:)-9hucf.md)
  Returns the elements of the sequence, sorted using the given array of `SortComparator`s to compare elements.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [ArraySlice<Self.Element>]](musicitemcollection/split(separator:maxsplits:omittingemptysubsequences:)-2vhx7.md)
  Returns the longest possible subsequences of the sequence, in order, around elements equal to the given element.
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](musicitemcollection/starts(with:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](musicitemcollection/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](musicitemcollection/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.
### Type Aliases
- [MusicItemCollection.Element](musicitemcollection/element.md)
  A type representing the sequence’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicitemcollection/sequence-implementations)*