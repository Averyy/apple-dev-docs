# Sequence Implementations

**Framework**: RealityKit

## Topics

### Structures
- [MeshSkeletonCollection.Iterator](meshskeletoncollection/iterator.md)
  A type that provides the sequence’s iteration interface and encapsulates its iteration state.
### Instance Properties
- [var lazy: LazySequence<Self>](meshskeletoncollection/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [var publisher: Publishers.Sequence<Self, Never>](meshskeletoncollection/publisher.md)
### Instance Methods
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](meshskeletoncollection/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](meshskeletoncollection/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func compare<Comparator>(Comparator.Compared, Comparator.Compared) -> ComparisonResult](meshskeletoncollection/compare(_:_:).md)
  If `lhs` is ordered before `rhs` in the ordering described by the given sequence of `SortComparator`s
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](meshskeletoncollection/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func count<E>(where: (Self.Element) throws(E) -> Bool) throws(E) -> Int](meshskeletoncollection/count(where:).md)
  Returns the number of elements in the sequence that satisfy the given predicate.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](meshskeletoncollection/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func enumerated() -> EnumeratedSequence<Self>](meshskeletoncollection/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](meshskeletoncollection/filter(_:).md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](meshskeletoncollection/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](meshskeletoncollection/flatmap(_:)-5odxk.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](meshskeletoncollection/flatmap(_:)-8mwha.md)
- [func forEach((Self.Element) throws -> Void) rethrows](meshskeletoncollection/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func formatted<S>(S) -> S.FormatOutput](meshskeletoncollection/formatted(_:).md)
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](meshskeletoncollection/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
- [func makeIterator() -> MeshSkeletonCollection.Iterator](meshskeletoncollection/makeiterator.md)
  Returns an iterator over the elements of this sequence.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](meshskeletoncollection/map(_:)-fkw3.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](meshskeletoncollection/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](meshskeletoncollection/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](meshskeletoncollection/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](meshskeletoncollection/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reversed() -> [Self.Element]](meshskeletoncollection/reversed.md)
  Returns an array containing the elements of this sequence in reverse order.
- [func shuffled() -> [Self.Element]](meshskeletoncollection/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](meshskeletoncollection/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](meshskeletoncollection/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func sorted<Comparator>(using: Comparator) -> [Self.Element]](meshskeletoncollection/sorted(using:)-7i8u8.md)
  Returns the elements of the sequence, sorted using the given comparator to compare elements.
- [func sorted<S, Comparator>(using: S) -> [Self.Element]](meshskeletoncollection/sorted(using:)-8dl3h.md)
  Returns the elements of the sequence, sorted using the given array of `SortComparator`s to compare elements.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](meshskeletoncollection/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](meshskeletoncollection/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.
### Type Aliases
- [MeshSkeletonCollection.Element](meshskeletoncollection/element.md)
  A type representing the sequence’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshskeletoncollection/sequence-implementations)*