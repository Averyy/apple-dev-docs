# Sequence Implementations

**Framework**: Swift

## Topics

### Structures
- [LazyPrefixWhileSequence.Iterator](lazyprefixwhilesequence/iterator.md)
  An iterator over the initial elements traversed by a base iterator that satisfy a given predicate.
### Instance Properties
- [var underestimatedCount: Int](lazyprefixwhilesequence/underestimatedcount.md)
  A value less than or equal to the number of elements in the sequence, calculated nondestructively.
### Instance Methods
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](lazyprefixwhilesequence/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](lazyprefixwhilesequence/compactmap(_:)-29nfp.md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func contains(Self.Element) -> Bool](lazyprefixwhilesequence/contains(_:).md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](lazyprefixwhilesequence/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func count<E>(where: (Self.Element) throws(E) -> Bool) throws(E) -> Int](lazyprefixwhilesequence/count(where:).md)
  Returns the number of elements in the sequence that satisfy the given predicate.
- [func dropFirst(Int) -> DropFirstSequence<Self>](lazyprefixwhilesequence/dropfirst(_:).md)
  Returns a sequence containing all but the given number of initial elements.
- [func dropLast(Int) -> [Self.Element]](lazyprefixwhilesequence/droplast(_:).md)
  Returns a sequence containing all but the given number of final elements.
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](lazyprefixwhilesequence/elementsequal(_:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](lazyprefixwhilesequence/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func enumerated() -> EnumeratedSequence<Self>](lazyprefixwhilesequence/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](lazyprefixwhilesequence/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](lazyprefixwhilesequence/flatmap(_:)-62fa.md)
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](lazyprefixwhilesequence/flatmap(_:)-9fckz.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func forEach((Self.Element) throws -> Void) rethrows](lazyprefixwhilesequence/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func joined() -> FlattenSequence<Self>](lazyprefixwhilesequence/joined-1ob4c.md)
  Returns the elements of this sequence of sequences, concatenated.
- [func joined<Separator>(separator: Separator) -> JoinedSequence<Self>](lazyprefixwhilesequence/joined(separator:)-1n2gn.md)
  Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
- [func joined(separator: String) -> String](lazyprefixwhilesequence/joined(separator:)-26tel.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence) -> Bool](lazyprefixwhilesequence/lexicographicallyprecedes(_:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](lazyprefixwhilesequence/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
- [func makeIterator() -> LazyPrefixWhileSequence<Base>.Iterator](lazyprefixwhilesequence/makeiterator.md)
  Returns an iterator over the elements of this sequence.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](lazyprefixwhilesequence/map(_:)-4uxrw.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func max() -> Self.Element?](lazyprefixwhilesequence/max.md)
  Returns the maximum element in the sequence.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](lazyprefixwhilesequence/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func min() -> Self.Element?](lazyprefixwhilesequence/min.md)
  Returns the minimum element in the sequence.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](lazyprefixwhilesequence/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func prefix(Int) -> PrefixSequence<Self>](lazyprefixwhilesequence/prefix(_:).md)
  Returns a sequence, up to the specified maximum length, containing the initial elements of the sequence.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](lazyprefixwhilesequence/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](lazyprefixwhilesequence/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reversed() -> [Self.Element]](lazyprefixwhilesequence/reversed.md)
  Returns an array containing the elements of this sequence in reverse order.
- [func shuffled() -> [Self.Element]](lazyprefixwhilesequence/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](lazyprefixwhilesequence/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [func sorted() -> [Self.Element]](lazyprefixwhilesequence/sorted.md)
  Returns the elements of the sequence, sorted.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](lazyprefixwhilesequence/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [ArraySlice<Self.Element>]](lazyprefixwhilesequence/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the sequence, in order, that don’t contain elements satisfying the given predicate. Elements that are used to split the sequence are not returned as part of any subsequence.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [ArraySlice<Self.Element>]](lazyprefixwhilesequence/split(separator:maxsplits:omittingemptysubsequences:)-rqw4.md)
  Returns the longest possible subsequences of the sequence, in order, around elements equal to the given element.
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](lazyprefixwhilesequence/starts(with:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](lazyprefixwhilesequence/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [func suffix(Int) -> [Self.Element]](lazyprefixwhilesequence/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the sequence.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](lazyprefixwhilesequence/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazyprefixwhilesequence/sequence-implementations)*