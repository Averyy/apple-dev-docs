# Scene.AnchorCollection

**Framework**: RealityKit  
**Kind**: struct

A collection of anchor entities.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency struct AnchorCollection
```

## Topics

### Comparing collections
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](scene/anchorcollection/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](scene/anchorcollection/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](scene/anchorcollection/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
### Iterating over the collection
- [func makeIterator() -> Scene.AnchorCollection.Iterator](scene/anchorcollection/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [Scene.AnchorCollection.Iterator](scene/anchorcollection/iterator.md)
  An iterator that presents the elements of the collection.
- [Scene.AnchorCollection.Element](scene/anchorcollection/element.md)
  The type of element traversed by the iterator.
- [func forEach((Self.Element) throws -> Void) rethrows](scene/anchorcollection/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func enumerated() -> EnumeratedSequence<Self>](scene/anchorcollection/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [var underestimatedCount: Int](scene/anchorcollection/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Counting anchors
- [var count: Int](scene/anchorcollection/count.md)
  The number of elements in the collection.
- [var isEmpty: Bool](scene/anchorcollection/isempty.md)
  A Boolean value indicating whether the collection is empty.
### Accessing anchors
- [subscript(Int) -> any HasAnchoring](scene/anchorcollection/subscript(_:).md)
  Accesses the element at the specified position.
- [Scene.AnchorCollection.SubSequence](scene/anchorcollection/subsequence.md)
  A sequence that represents a contiguous subrange of the collection’s elements.
### Adding anchors
- [func append(any HasAnchoring)](scene/anchorcollection/append(_:).md)
  Adds a new anchor at the end of the collection.
- [func append(contentsOf: [any HasAnchoring])](scene/anchorcollection/append(contentsof:)-3bjib.md)
  Adds anchors from an array to the end of this collection.
- [func append<S>(contentsOf: S)](scene/anchorcollection/append(contentsof:)-4sf55.md)
  Adds anchors from a sequence to the end of this collection.
### Removing anchors
- [func remove(any HasAnchoring)](scene/anchorcollection/remove(_:).md)
  Removes the anchor at the specified position.
- [func remove(at: Int)](scene/anchorcollection/remove(at:).md)
  Removes and returns the anchor at the specified position.
- [func removeAll()](scene/anchorcollection/removeall.md)
  Removes all anchors from the collection.
- [func removeAll(keepCapacity: Bool)](scene/anchorcollection/removeall(keepcapacity:).md)
  Removes all anchors from the collection.
### Replacing anchors
- [func replaceAll([any HasAnchoring])](scene/anchorcollection/replaceall(_:)-tris.md)
  Replaces the existing anchor collection with a provided collection.
- [func replaceAll<S>(S)](scene/anchorcollection/replaceall(_:)-5t195.md)
  Replaces the existing anchor collection with a provided sequence.
### Finding anchors
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](scene/anchorcollection/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](scene/anchorcollection/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [var first: Self.Element?](scene/anchorcollection/first.md)
  The first element of the collection.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](scene/anchorcollection/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](scene/anchorcollection/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](scene/anchorcollection/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
### Selecting anchors
- [func filter(Predicate<Self.Element>) throws -> [Self.Element]](scene/anchorcollection/filter(_:)-4j9lz.md)
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](scene/anchorcollection/filter(_:)-9loo9.md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [func prefix(Int) -> Self.SubSequence](scene/anchorcollection/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](scene/anchorcollection/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](scene/anchorcollection/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](scene/anchorcollection/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func suffix(Int) -> Self.SubSequence](scene/anchorcollection/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](scene/anchorcollection/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
- [func randomElement() -> Self.Element?](scene/anchorcollection/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](scene/anchorcollection/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
### Transforming anchors
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](scene/anchorcollection/map(_:)-707cs.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](scene/anchorcollection/flatmap(_:)-8rfad.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](scene/anchorcollection/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](scene/anchorcollection/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](scene/anchorcollection/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [var lazy: LazySequence<Self>](scene/anchorcollection/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](scene/anchorcollection/flatmap(_:)-73qft.md)
### Reordering anchors
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](scene/anchorcollection/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func reversed() -> [Self.Element]](scene/anchorcollection/reversed.md)
  Returns an array containing the elements of this sequence in reverse order.
- [func shuffled() -> [Self.Element]](scene/anchorcollection/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](scene/anchorcollection/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
### Excluding anchors
- [func dropFirst(Int) -> Self.SubSequence](scene/anchorcollection/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](scene/anchorcollection/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](scene/anchorcollection/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
### Splitting the collection
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](scene/anchorcollection/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
### Manipulating indices
- [Scene.AnchorCollection.Index](scene/anchorcollection/index.md)
  A type that represents a position in the collection.
- [Scene.AnchorCollection.Indices](scene/anchorcollection/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [var startIndex: Int](scene/anchorcollection/startindex.md)
  The position of the first element in a nonempty collection.
- [var endIndex: Int](scene/anchorcollection/endindex.md)
  The position one greater than the last valid subscript argument.
- [var indices: DefaultIndices<Self>](scene/anchorcollection/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](scene/anchorcollection/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](scene/anchorcollection/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Int) -> Int](scene/anchorcollection/index(after:).md)
  Returns the position immediately after the given index.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](scene/anchorcollection/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](scene/anchorcollection/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](scene/anchorcollection/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](scene/anchorcollection/formindex(after:).md)
  Replaces the given index with its successor.
- [func distance(from: Self.Index, to: Self.Index) -> Int](scene/anchorcollection/distance(from:to:).md)
  Returns the distance between two indices.
### Accessing underlying storage
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](scene/anchorcollection/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.
### Publishing changes
- [var publisher: Publishers.Sequence<Self, Never>](scene/anchorcollection/publisher.md)
### Describing the collection
- [var description: String](scene/anchorcollection/description.md)
  A textual representation of this instance.
### Default Implementations
- [Collection Implementations](scene/anchorcollection/collection-implementations.md)
- [CustomStringConvertible Implementations](scene/anchorcollection/customstringconvertible-implementations.md)
- [Sequence Implementations](scene/anchorcollection/sequence-implementations.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [class Scene](scene.md)
  A container that holds the collection of entities that an AR view renders.
- [typealias ID](scene/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection)*