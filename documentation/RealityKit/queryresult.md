# QueryResult

**Framework**: RealityKit  
**Kind**: struct

An object that returns the results of an entity query.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct QueryResult<Element>
```

#### Overview

You can’t create query result objects. Instead, call [`performQuery(_:)`](scene/performquery(_:).md), which returns a [`QueryResult`](queryresult.md) containing the entities that meet your specified query criteria.

```swift
// Ask the scene to perform the query and iterate over the returned entities.
scene.performQuery(query).forEach { entity in
    print("Returned entity: \(entity)")
}
```

## Topics

### Creating an iterator
- [QueryResult.Iterator](queryresult/iterator.md)
  The type of iterator used for entity query results.
- [func makeIterator() -> QueryResult<Element>.Iterator](queryresult/makeiterator.md)
  Returns an iterator for the contained entities.
### Finding elements
- [func contains(Self.Element) -> Bool](queryresult/contains(_:).md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](queryresult/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](queryresult/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](queryresult/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
### Selecting elements
- [func prefix(Int) -> PrefixSequence<Self>](queryresult/prefix(_:).md)
  Returns a sequence, up to the specified maximum length, containing the initial elements of the sequence.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> [Self.Element]](queryresult/prefix(while:).md)
  Returns a sequence containing the initial, consecutive elements that satisfy the given predicate.
- [func suffix(Int) -> [Self.Element]](queryresult/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the sequence.
### Excluding elements
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> DropWhileSequence<Self>](queryresult/drop(while:).md)
  Returns a sequence by skipping the initial, consecutive elements that satisfy the given predicate.
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](queryresult/filter(_:).md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [func filter<T>(matchingCategory: CMTypedTag<T>.Category) -> [CMTypedTag<T>]](queryresult/filter(matchingcategory:).md)
  Filters a sequence of tags based on matching the specified category.  Returns the tags that match the specified category.
### Transforming a sequence
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](queryresult/map(_:).md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](queryresult/flatmap(_:)-6wvi7.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](queryresult/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](queryresult/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](queryresult/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [var lazy: LazySequence<Self>](queryresult/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](queryresult/flatmap(_:)-icze.md)
### Iterating over a sequence’s elements
- [func forEach((Self.Element) throws -> Void) rethrows](queryresult/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func enumerated() -> EnumeratedSequence<Self>](queryresult/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [var underestimatedCount: Int](queryresult/underestimatedcount.md)
  A value less than or equal to the number of elements in the sequence, calculated nondestructively.
### Reordering elements
- [func shuffled() -> [Self.Element]](queryresult/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](queryresult/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
### Splitting and joining elements
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [ArraySlice<Self.Element>]](queryresult/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the sequence, in order, that don’t contain elements satisfying the given predicate. Elements that are used to split the sequence are not returned as part of any subsequence.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [ArraySlice<Self.Element>]](queryresult/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the sequence, in order, around elements equal to the given element.
- [func joined() -> FlattenSequence<Self>](queryresult/joined.md)
  Returns the elements of this sequence of sequences, concatenated.
- [func joined<Separator>(separator: Separator) -> JoinedSequence<Self>](queryresult/joined(separator:)-632mh.md)
  Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
- [func joined(separator: String) -> String](queryresult/joined(separator:)-58ktm.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
### Comparing sequences
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](queryresult/elementsequal(_:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](queryresult/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](queryresult/starts(with:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](queryresult/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
### Accessing underlying storage
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](queryresult/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.
### Publishing a sequence
- [var publisher: Publishers.Sequence<Self, Never>](queryresult/publisher.md)
### Default Implementations
- [Sequence Implementations](queryresult/sequence-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct EntityQuery](entityquery.md)
  An object that retrieves entities from a scene.
- [struct QueryPredicate](querypredicate.md)
  An object that defines the criteria for an entity query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/queryresult)*