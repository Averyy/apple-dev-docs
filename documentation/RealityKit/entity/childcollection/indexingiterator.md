# Entity.ChildCollection.IndexingIterator

**Framework**: RealityKit  
**Kind**: struct

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
struct IndexingIterator<Elements> where Elements : Collection
```

## Topics

### Iterating over the collection
- [func enumerated() -> EnumeratedSequence<Self>](entity/childcollection/indexingiterator/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func next() -> Elements.Element?](entity/childcollection/indexingiterator/next.md)
  Advances to the next element and returns it, or `nil` if no next element exists.
- [func forEach((Self.Element) throws -> Void) rethrows](entity/childcollection/indexingiterator/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func makeIterator() -> Self](entity/childcollection/indexingiterator/makeiterator.md)
  Returns an iterator over the elements of this sequence.
- [Entity.ChildCollection.IndexingIterator.Iterator](entity/childcollection/indexingiterator/iterator.md)
  A type that provides the sequence’s iteration interface and encapsulates its iteration state.
- [Entity.ChildCollection.IndexingIterator.Element](entity/childcollection/indexingiterator/element.md)
  The type of element traversed by the iterator.
- [var underestimatedCount: Int](entity/childcollection/indexingiterator/underestimatedcount.md)
  A value less than or equal to the number of elements in the sequence, calculated nondestructively.
### Finding entities
- [func contains(Self.Element) -> Bool](entity/childcollection/indexingiterator/contains(_:).md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](entity/childcollection/indexingiterator/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](entity/childcollection/indexingiterator/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](entity/childcollection/indexingiterator/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func max() -> Self.Element?](entity/childcollection/indexingiterator/max.md)
  Returns the maximum element in the sequence.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](entity/childcollection/indexingiterator/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func min() -> Self.Element?](entity/childcollection/indexingiterator/min.md)
  Returns the minimum element in the sequence.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](entity/childcollection/indexingiterator/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
### Selecting entities
- [func filter(Predicate<Self.Element>) throws -> [Self.Element]](entity/childcollection/indexingiterator/filter(_:)-17bfr.md)
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](entity/childcollection/indexingiterator/filter(_:)-3ihv7.md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [func prefix(Int) -> PrefixSequence<Self>](entity/childcollection/indexingiterator/prefix(_:).md)
  Returns a sequence, up to the specified maximum length, containing the initial elements of the sequence.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> [Self.Element]](entity/childcollection/indexingiterator/prefix(while:).md)
  Returns a sequence containing the initial, consecutive elements that satisfy the given predicate.
- [func suffix(Int) -> [Self.Element]](entity/childcollection/indexingiterator/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the sequence.
### Transforming entities
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](entity/childcollection/indexingiterator/map(_:).md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](entity/childcollection/indexingiterator/flatmap(_:)-std6.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](entity/childcollection/indexingiterator/flatmap(_:)-7ql02.md)
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](entity/childcollection/indexingiterator/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](entity/childcollection/indexingiterator/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](entity/childcollection/indexingiterator/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [var lazy: LazySequence<Self>](entity/childcollection/indexingiterator/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
### Reordering entities
- [func sorted() -> [Self.Element]](entity/childcollection/indexingiterator/sorted.md)
  Returns the elements of the sequence, sorted.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](entity/childcollection/indexingiterator/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func reversed() -> [Self.Element]](entity/childcollection/indexingiterator/reversed.md)
  Returns an array containing the elements of this sequence in reverse order.
- [func shuffled() -> [Self.Element]](entity/childcollection/indexingiterator/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](entity/childcollection/indexingiterator/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
### Splitting and joining entities
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [ArraySlice<Self.Element>]](entity/childcollection/indexingiterator/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the sequence, in order, that don’t contain elements satisfying the given predicate. Elements that are used to split the sequence are not returned as part of any subsequence.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [ArraySlice<Self.Element>]](entity/childcollection/indexingiterator/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the sequence, in order, around elements equal to the given element.
- [func joined() -> FlattenSequence<Self>](entity/childcollection/indexingiterator/joined.md)
  Returns the elements of this sequence of sequences, concatenated.
- [func joined<Separator>(separator: Separator) -> JoinedSequence<Self>](entity/childcollection/indexingiterator/joined(separator:)-8q64h.md)
  Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
- [func joined(separator: String) -> String](entity/childcollection/indexingiterator/joined(separator:)-35cxx.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [Entity.ChildCollection.IndexingIterator.SubSequence](entity/childcollection/indexingiterator/subsequence.md)
### Comparing collections
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](entity/childcollection/indexingiterator/elementsequal(_:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](entity/childcollection/indexingiterator/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](entity/childcollection/indexingiterator/starts(with:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](entity/childcollection/indexingiterator/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence) -> Bool](entity/childcollection/indexingiterator/lexicographicallyprecedes(_:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](entity/childcollection/indexingiterator/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
### Excluding entities
- [func dropFirst(Int) -> DropFirstSequence<Self>](entity/childcollection/indexingiterator/dropfirst(_:).md)
  Returns a sequence containing all but the given number of initial elements.
- [func dropLast(Int) -> [Self.Element]](entity/childcollection/indexingiterator/droplast(_:).md)
  Returns a sequence containing all but the given number of final elements.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> DropWhileSequence<Self>](entity/childcollection/indexingiterator/drop(while:).md)
  Returns a sequence by skipping the initial, consecutive elements that satisfy the given predicate.
### Accessing underlying storage
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](entity/childcollection/indexingiterator/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.
### Publishing changes
- [var publisher: Publishers.Sequence<Self, Never>](entity/childcollection/indexingiterator/publisher.md)
### Default Implementations
- [IteratorProtocol Implementations](entity/childcollection/indexingiterator/iteratorprotocol-implementations.md)
- [Sequence Implementations](entity/childcollection/indexingiterator/sequence-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [IteratorProtocol](../Swift/IteratorProtocol.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [func forEach((Self.Element) throws -> Void) rethrows](entity/childcollection/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func enumerated() -> EnumeratedSequence<Self>](entity/childcollection/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [var underestimatedCount: Int](entity/childcollection/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/indexingiterator)*