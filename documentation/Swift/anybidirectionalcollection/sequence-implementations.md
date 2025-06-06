# Sequence Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var lazy: LazySequence<Self>](anybidirectionalcollection/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [var underestimatedCount: Int](anybidirectionalcollection/underestimatedcount.md)
  A value less than or equal to the number of elements in the sequence, calculated nondestructively.
### Instance Methods
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](anybidirectionalcollection/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](anybidirectionalcollection/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func contains(Self.Element) -> Bool](anybidirectionalcollection/contains(_:).md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](anybidirectionalcollection/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func count<E>(where: (Self.Element) throws(E) -> Bool) throws(E) -> Int](anybidirectionalcollection/count(where:).md)
  Returns the number of elements in the sequence that satisfy the given predicate.
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](anybidirectionalcollection/elementsequal(_:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](anybidirectionalcollection/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func enumerated() -> EnumeratedSequence<Self>](anybidirectionalcollection/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](anybidirectionalcollection/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](anybidirectionalcollection/flatmap(_:)-400so.md)
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](anybidirectionalcollection/flatmap(_:)-78q3j.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func joined() -> FlattenSequence<Self>](anybidirectionalcollection/joined.md)
  Returns the elements of this sequence of sequences, concatenated.
- [func joined<Separator>(separator: Separator) -> JoinedSequence<Self>](anybidirectionalcollection/joined(separator:)-75msx.md)
  Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
- [func joined(separator: String) -> String](anybidirectionalcollection/joined(separator:)-8i1yu.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence) -> Bool](anybidirectionalcollection/lexicographicallyprecedes(_:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](anybidirectionalcollection/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](anybidirectionalcollection/map(_:)-769c3.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func max() -> Self.Element?](anybidirectionalcollection/max.md)
  Returns the maximum element in the sequence.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](anybidirectionalcollection/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func min() -> Self.Element?](anybidirectionalcollection/min.md)
  Returns the minimum element in the sequence.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](anybidirectionalcollection/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](anybidirectionalcollection/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](anybidirectionalcollection/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func shuffled() -> [Self.Element]](anybidirectionalcollection/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](anybidirectionalcollection/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [func sorted() -> [Self.Element]](anybidirectionalcollection/sorted.md)
  Returns the elements of the sequence, sorted.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](anybidirectionalcollection/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [ArraySlice<Self.Element>]](anybidirectionalcollection/split(separator:maxsplits:omittingemptysubsequences:)-4y1gu.md)
  Returns the longest possible subsequences of the sequence, in order, around elements equal to the given element.
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](anybidirectionalcollection/starts(with:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](anybidirectionalcollection/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](anybidirectionalcollection/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anybidirectionalcollection/sequence-implementations)*