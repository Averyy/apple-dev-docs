# Sequence Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var lazy: LazySequence<Self>](unsafemutablebufferpointer/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [var underestimatedCount: Int](unsafemutablebufferpointer/underestimatedcount-4t0hk.md)
  A value less than or equal to the number of elements in the sequence, calculated nondestructively.
### Instance Methods
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](unsafemutablebufferpointer/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](unsafemutablebufferpointer/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func contains(Self.Element) -> Bool](unsafemutablebufferpointer/contains(_:).md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](unsafemutablebufferpointer/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func count<E>(where: (Self.Element) throws(E) -> Bool) throws(E) -> Int](unsafemutablebufferpointer/count(where:).md)
  Returns the number of elements in the sequence that satisfy the given predicate.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> DropWhileSequence<Self>](unsafemutablebufferpointer/drop(while:)-7a7k8.md)
  Returns a sequence by skipping the initial, consecutive elements that satisfy the given predicate.
- [func dropFirst(Int) -> DropFirstSequence<Self>](unsafemutablebufferpointer/dropfirst(_:)-9f3di.md)
  Returns a sequence containing all but the given number of initial elements.
- [func dropLast(Int) -> [Self.Element]](unsafemutablebufferpointer/droplast(_:)-8b3lf.md)
  Returns a sequence containing all but the given number of final elements.
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](unsafemutablebufferpointer/elementsequal(_:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](unsafemutablebufferpointer/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func enumerated() -> EnumeratedSequence<Self>](unsafemutablebufferpointer/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](unsafemutablebufferpointer/filter(_:).md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](unsafemutablebufferpointer/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](unsafemutablebufferpointer/flatmap(_:)-6chtv.md)
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](unsafemutablebufferpointer/flatmap(_:)-i3n4.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func forEach((Self.Element) throws -> Void) rethrows](unsafemutablebufferpointer/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func joined() -> FlattenSequence<Self>](unsafemutablebufferpointer/joined.md)
  Returns the elements of this sequence of sequences, concatenated.
- [func joined(separator: String) -> String](unsafemutablebufferpointer/joined(separator:)-1ckou.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func joined<Separator>(separator: Separator) -> JoinedSequence<Self>](unsafemutablebufferpointer/joined(separator:)-7ubf4.md)
  Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence) -> Bool](unsafemutablebufferpointer/lexicographicallyprecedes(_:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](unsafemutablebufferpointer/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
- [func makeIterator() -> UnsafeMutableBufferPointer<Element>.Iterator](unsafemutablebufferpointer/makeiterator.md)
  Returns an iterator over the elements of this buffer.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](unsafemutablebufferpointer/map(_:)-9jnoq.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func max() -> Self.Element?](unsafemutablebufferpointer/max.md)
  Returns the maximum element in the sequence.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](unsafemutablebufferpointer/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func min() -> Self.Element?](unsafemutablebufferpointer/min.md)
  Returns the minimum element in the sequence.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](unsafemutablebufferpointer/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func prefix(Int) -> PrefixSequence<Self>](unsafemutablebufferpointer/prefix(_:)-9jcs0.md)
  Returns a sequence, up to the specified maximum length, containing the initial elements of the sequence.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> [Self.Element]](unsafemutablebufferpointer/prefix(while:)-3il6q.md)
  Returns a sequence containing the initial, consecutive elements that satisfy the given predicate.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](unsafemutablebufferpointer/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](unsafemutablebufferpointer/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reversed() -> [Self.Element]](unsafemutablebufferpointer/reversed-24fmo.md)
  Returns an array containing the elements of this sequence in reverse order.
- [func shuffled() -> [Self.Element]](unsafemutablebufferpointer/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](unsafemutablebufferpointer/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [func sorted() -> [Self.Element]](unsafemutablebufferpointer/sorted.md)
  Returns the elements of the sequence, sorted.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](unsafemutablebufferpointer/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [ArraySlice<Self.Element>]](unsafemutablebufferpointer/split(maxsplits:omittingemptysubsequences:whereseparator:)-5m0ky.md)
  Returns the longest possible subsequences of the sequence, in order, that don’t contain elements satisfying the given predicate. Elements that are used to split the sequence are not returned as part of any subsequence.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [ArraySlice<Self.Element>]](unsafemutablebufferpointer/split(separator:maxsplits:omittingemptysubsequences:)-9bdx3.md)
  Returns the longest possible subsequences of the sequence, in order, around elements equal to the given element.
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](unsafemutablebufferpointer/starts(with:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](unsafemutablebufferpointer/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [func suffix(Int) -> [Self.Element]](unsafemutablebufferpointer/suffix(_:)-1rpyd.md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the sequence.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Element>) throws -> R) rethrows -> R?](unsafemutablebufferpointer/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](unsafemutablebufferpointer/withcontiguousstorageifavailable(_:)-1ynsv.md)
  Executes a closure on the sequence’s contiguous storage.
### Type Aliases
- [UnsafeMutableBufferPointer.Iterator](unsafemutablebufferpointer/iterator.md)
  A type that provides the sequence’s iteration interface and encapsulates its iteration state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/sequence-implementations)*