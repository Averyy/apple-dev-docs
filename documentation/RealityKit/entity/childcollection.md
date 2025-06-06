# Entity.ChildCollection

**Framework**: RealityKit  
**Kind**: struct

A collection of child entities.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency struct ChildCollection
```

## Topics

### Accessing collection members
- [subscript(Int) -> Entity](entity/childcollection/subscript(_:).md)
  Accesses the element at the specified position. (See `Collection.subscript`.)
### Adding entities
- [func append<S>(contentsOf: S, preservingWorldTransforms: Bool)](entity/childcollection/append(contentsof:preservingworldtransforms:)-7g61.md)
  Adds the specified list of entity as children to this entity.
- [func append(Entity, preservingWorldTransform: Bool)](entity/childcollection/append(_:preservingworldtransform:).md)
  Adds the specified entity as a child to this entity.
- [func append(contentsOf: [Entity], preservingWorldTransforms: Bool)](entity/childcollection/append(contentsof:preservingworldtransforms:)-7p4hd.md)
  Adds the specified list of entity as children to this entity.
### Removing entities
- [func remove(Entity, preservingWorldTransform: Bool)](entity/childcollection/remove(_:preservingworldtransform:).md)
  Removes the specified child from this entity.
- [func remove(at: Int, preservingWorldTransform: Bool)](entity/childcollection/remove(at:preservingworldtransform:).md)
  Removes the specified child from this entity.
- [func removeAll(preservingWorldTransforms: Bool)](entity/childcollection/removeall(preservingworldtransforms:).md)
- [func removeAll(keepCapacity: Bool, preservingWorldTransforms: Bool)](entity/childcollection/removeall(keepcapacity:preservingworldtransforms:).md)
  Removes all children from this entity.
### Replacing entities
- [func replaceAll([Entity], preservingWorldTransforms: Bool)](entity/childcollection/replaceall(_:preservingworldtransforms:)-4mgff.md)
  Removes all children from this entity and adds the specified list of entities as the new children.
- [func replaceAll<S>(S, preservingWorldTransforms: Bool)](entity/childcollection/replaceall(_:preservingworldtransforms:)-1vwk4.md)
  Removes all children from this entity and adds the specified list of entities as the new children.
### Comparing collections
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](entity/childcollection/elementsequal(_:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](entity/childcollection/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](entity/childcollection/starts(with:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](entity/childcollection/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](entity/childcollection/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
### Iterating over collection of entities
- [Entity.ChildCollection.IndexingIterator](entity/childcollection/indexingiterator.md)
- [func forEach((Self.Element) throws -> Void) rethrows](entity/childcollection/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func enumerated() -> EnumeratedSequence<Self>](entity/childcollection/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [var underestimatedCount: Int](entity/childcollection/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Finding entities
- [func contains(Self.Element) -> Bool](entity/childcollection/contains(_:).md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](entity/childcollection/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](entity/childcollection/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [var first: Self.Element?](entity/childcollection/first.md)
  The first element of the collection.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](entity/childcollection/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](entity/childcollection/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](entity/childcollection/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func randomElement() -> Self.Element?](entity/childcollection/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](entity/childcollection/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
### Selecting entities
- [subscript(Int) -> Entity](entity/childcollection/subscript(_:).md)
  Accesses the element at the specified position. (See `Collection.subscript`.)
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](entity/childcollection/filter(_:)-4vjmu.md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [func prefix(Int) -> Self.SubSequence](entity/childcollection/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](entity/childcollection/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](entity/childcollection/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](entity/childcollection/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func suffix(Int) -> Self.SubSequence](entity/childcollection/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](entity/childcollection/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Transforming entities
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](entity/childcollection/map(_:)-78ywb.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](entity/childcollection/flatmap(_:)-5ijyo.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](entity/childcollection/flatmap(_:)-9ovg6.md)
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](entity/childcollection/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](entity/childcollection/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](entity/childcollection/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [var lazy: LazySequence<Self>](entity/childcollection/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
### Reordering entities
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](entity/childcollection/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func reversed() -> [Self.Element]](entity/childcollection/reversed.md)
  Returns an array containing the elements of this sequence in reverse order.
- [func shuffled() -> [Self.Element]](entity/childcollection/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](entity/childcollection/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
### Splitting the collection
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](entity/childcollection/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](entity/childcollection/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
### Describing a collection
- [var description: String](entity/childcollection/description.md)
  A textual representation of this instance. (See `CustomStringConvertible`.)
### Counting entities
- [var count: Int](entity/childcollection/count.md)
  The number of elements in the collection.
- [var isEmpty: Bool](entity/childcollection/isempty.md)
  A Boolean value indicating whether the collection is empty.
### Excluding entities
- [func dropFirst(Int) -> Self.SubSequence](entity/childcollection/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](entity/childcollection/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](entity/childcollection/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
### Accessing underlying storage
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](entity/childcollection/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.
### Manipulating indices
- [func distance(from: Self.Index, to: Self.Index) -> Int](entity/childcollection/distance(from:to:).md)
  Returns the distance between two indices.
- [var indices: DefaultIndices<Self>](entity/childcollection/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var startIndex: Int](entity/childcollection/startindex.md)
  The position of the first element in a nonempty collection. (See `Collection.startIndex`.)
- [var endIndex: Int](entity/childcollection/endindex.md)
  TThe collection’s “past the end” position—that is, the position one greater than the last valid subscript argument. (See `Collection.endIndex`.)
- [func firstIndex(of: Self.Element) -> Self.Index?](entity/childcollection/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](entity/childcollection/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func formIndex(inout Self.Index, offsetBy: Int)](entity/childcollection/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](entity/childcollection/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](entity/childcollection/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](entity/childcollection/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](entity/childcollection/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Int) -> Int](entity/childcollection/index(after:).md)
  Returns the position immediately after the given index. (See `Collection.index`.)
- [func index(of: Self.Element) -> Self.Index?](entity/childcollection/index(of:).md)
  Returns the first index where the specified value appears in the collection.
### Publishing changes
- [var publisher: Publishers.Sequence<Self, Never>](entity/childcollection/publisher.md)
### Instance Methods
- [func append(contentsOf: Entity.ChildCollection, preservingWorldTransforms: Bool)](entity/childcollection/append(contentsof:preservingworldtransforms:)-4cjpz.md)
  Moves all `children` to be children of this entity.
- [func makeIterator() -> Entity.ChildCollection.Iterator](entity/childcollection/makeiterator.md)
  Returns an iterator over the elements of the collection.
### Type Aliases
- [Entity.ChildCollection.Element](entity/childcollection/element.md)
  A type representing the sequence’s elements.
- [Entity.ChildCollection.Index](entity/childcollection/index.md)
  A type that represents a position in the collection.
- [Entity.ChildCollection.Indices](entity/childcollection/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Entity.ChildCollection.Iterator](entity/childcollection/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [Entity.ChildCollection.SubSequence](entity/childcollection/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [Collection Implementations](entity/childcollection/collection-implementations.md)
- [CustomStringConvertible Implementations](entity/childcollection/customstringconvertible-implementations.md)
- [EntityCollection Implementations](entity/childcollection/entitycollection-implementations.md)
- [Sequence Implementations](entity/childcollection/sequence-implementations.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [EntityCollection](entitycollection.md)
- [Sendable](../Swift/Sendable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [var parent: Entity?](entity/parent.md)
  The parent entity.
- [func setParent(Entity?, preservingWorldTransform: Bool)](entity/setparent(_:preservingworldtransform:).md)
  Attaches the entity as a child to the specified entity.
- [func removeFromParent(preservingWorldTransform: Bool)](entity/removefromparent(preservingworldtransform:).md)
  Removes the entity from its current parent or from the scene if it is a root entity.
- [var children: Entity.ChildCollection](entity/children.md)
  The child entities that the entity manages.
- [func addChild(Entity, preservingWorldTransform: Bool)](entity/addchild(_:preservingworldtransform:).md)
  Adds the given entity to the collection of child entities.
- [func removeChild(Entity, preservingWorldTransform: Bool)](entity/removechild(_:preservingworldtransform:).md)
  Removes the given child from the entity.
- [protocol HasHierarchy](hashierarchy.md)
  An interface that provides access to a parent entity and child entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection)*