# Sequence Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var lazy: LazySequence<Self>](dropfirstsequence/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [var underestimatedCount: Int](dropfirstsequence/underestimatedcount.md)
  A value less than or equal to the number of elements in the sequence, calculated nondestructively.
### Instance Methods
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](dropfirstsequence/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](dropfirstsequence/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func contains(Self.Element) -> Bool](dropfirstsequence/contains(_:).md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](dropfirstsequence/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func count<E>(where: (Self.Element) throws(E) -> Bool) throws(E) -> Int](dropfirstsequence/count(where:).md)
  Returns the number of elements in the sequence that satisfy the given predicate.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> DropWhileSequence<Self>](dropfirstsequence/drop(while:).md)
  Returns a sequence by skipping the initial, consecutive elements that satisfy the given predicate.
- [func dropLast(Int) -> [Self.Element]](dropfirstsequence/droplast(_:).md)
  Returns a sequence containing all but the given number of final elements.
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](dropfirstsequence/elementsequal(_:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](dropfirstsequence/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func enumerated() -> EnumeratedSequence<Self>](dropfirstsequence/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](dropfirstsequence/filter(_:).md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](dropfirstsequence/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](dropfirstsequence/flatmap(_:)-66w5i.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](dropfirstsequence/flatmap(_:)-9hnmb.md)
- [func forEach((Self.Element) throws -> Void) rethrows](dropfirstsequence/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func joined() -> FlattenSequence<Self>](dropfirstsequence/joined.md)
  Returns the elements of this sequence of sequences, concatenated.
- [func joined(separator: String) -> String](dropfirstsequence/joined(separator:)-1lfg6.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func joined<Separator>(separator: Separator) -> JoinedSequence<Self>](dropfirstsequence/joined(separator:)-vj4v.md)
  Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence) -> Bool](dropfirstsequence/lexicographicallyprecedes(_:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](dropfirstsequence/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
- [func makeIterator() -> DropFirstSequence<Base>.Iterator](dropfirstsequence/makeiterator.md)
  Returns an iterator over the elements of this sequence.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](dropfirstsequence/map(_:).md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func max() -> Self.Element?](dropfirstsequence/max.md)
  Returns the maximum element in the sequence.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](dropfirstsequence/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func min() -> Self.Element?](dropfirstsequence/min.md)
  Returns the minimum element in the sequence.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](dropfirstsequence/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func prefix(Int) -> PrefixSequence<Self>](dropfirstsequence/prefix(_:).md)
  Returns a sequence, up to the specified maximum length, containing the initial elements of the sequence.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> [Self.Element]](dropfirstsequence/prefix(while:).md)
  Returns a sequence containing the initial, consecutive elements that satisfy the given predicate.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](dropfirstsequence/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](dropfirstsequence/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reversed() -> [Self.Element]](dropfirstsequence/reversed.md)
  Returns an array containing the elements of this sequence in reverse order.
- [func shuffled() -> [Self.Element]](dropfirstsequence/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](dropfirstsequence/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [func sorted() -> [Self.Element]](dropfirstsequence/sorted.md)
  Returns the elements of the sequence, sorted.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](dropfirstsequence/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [ArraySlice<Self.Element>]](dropfirstsequence/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the sequence, in order, that don’t contain elements satisfying the given predicate. Elements that are used to split the sequence are not returned as part of any subsequence.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [ArraySlice<Self.Element>]](dropfirstsequence/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the sequence, in order, around elements equal to the given element.
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](dropfirstsequence/starts(with:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](dropfirstsequence/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [func suffix(Int) -> [Self.Element]](dropfirstsequence/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the sequence.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](dropfirstsequence/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.
### Type Aliases
- [DropFirstSequence.Element](dropfirstsequence/element.md)
  A type representing the sequence’s elements.
- [DropFirstSequence.Iterator](dropfirstsequence/iterator.md)
  A type that provides the sequence’s iteration interface and encapsulates its iteration state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dropfirstsequence/sequence-implementations)*