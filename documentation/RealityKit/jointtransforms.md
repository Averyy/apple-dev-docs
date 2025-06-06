# JointTransforms

**Framework**: RealityKit  
**Kind**: struct

A set of animatable transform values for joints that collectively represent a single skeletal pose.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct JointTransforms
```

#### Overview

This structure provides a template that informs an animation on how to animate a character. The resulting movement bases on the  ([`fromValue`](fromtobyanimation/fromvalue-6msd.md)) ,  ([`toValue`](fromtobyanimation/tovalue-813jk.md)) , or  values ([`byValue`](fromtobyanimation/byvalue-3bp3q.md)) you supply for a [`FromToByAnimation`](fromtobyanimation.md). The animation determines which joints take on the movement through its [`jointNames`](fromtobyanimation/jointnames.md) property.

#### Animate an Entitys Skeleton

The following code moves the joints of a 3D asset by specifying the joint, `joint1`, beginning, and ending values.

```swift
// Define the joint's pose at the start of the animation.
let fromTransforms: [Transform] = [Transform(scale: SIMD3<Float>(1, 2, 3), rotation: simd_quatf(ix: 5.0, iy: 6.0, iz: 7.0, r: 8.0), translation: SIMD3<Float>(10, 20, 30))]
let fromPose = JointTransforms(fromTransforms)

// Define the joint's pose at the end of the animation.
let toTransforms: [Transform] = [Transform(scale: SIMD3<Float>(10, 20, 30), rotation:
simd_quatf(ix: 50.0, iy: 60.0, iz: 70.0, r: 80.0), translation:
SIMD3<Float>(100, 200, 300)) ]
let toPose = JointTransforms(toTransforms)

// Indicate that the animation applies to the joint named 'joint1'.
let jointNames = ["joint1"]

// Configure the animation specifics.
var fromToBy = FromToByAnimation<JointTransforms>()
fromToBy.name = "anim"
fromToBy.blendLayer = 100
fromToBy.duration = 10.0
fromToBy.fillMode = .forwards
fromToBy.jointNames = jointNames
fromToBy.fromValue = fromPose
fromToBy.toValue = toPose
fromToBy.bindTarget = .transform

// Generate a resource from the animation.
let animationResource = fromToBy.create()
```

To run the animation on an entity and animate the joints, call `playAnimation(_:transitionDuration:startsPaused:)`. Optionally, you can control the animation’s playback by storing the returned controller object.

```swift
// Play the animation on an entity.
let entity = AnchorEntity(...)
let controller = entity.playAnimation(animationResource)

// Optionally control playback using the returned controller.
controller.pause()
```

## Topics

### Creating joint transforms
- [init()](jointtransforms/init.md)
  Initializes a collection of animatable transforms for a single skeletal pose.
- [init<S>(S)](jointtransforms/init(_:).md)
  Initializes a collection of transforms of a specific type for a single skeletal pose.
- [init(arrayLiteral: Transform...)](jointtransforms/init(arrayliteral:).md)
  Initializes a collection of animatable transforms using the argument elements for a single skeletal pose.
### Identifying joint transforms
- [JointTransforms.ArrayLiteralElement](jointtransforms/arrayliteralelement.md)
  The type of the elements of an array literal.
- [JointTransforms.Element](jointtransforms/element.md)
  An individual joint transform in the collection.
- [JointTransforms.Index](jointtransforms/index.md)
  A position of an individual joint transform in the collection.
- [JointTransforms.Indices](jointtransforms/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [JointTransforms.Iterator](jointtransforms/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [JointTransforms.SubSequence](jointtransforms/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Inspecting joint transform details
- [var count: Int](jointtransforms/count.md)
  The number of elements in the collection.
- [var first: Self.Element?](jointtransforms/first.md)
  The first element of the collection.
- [var indices: DefaultIndices<Self>](jointtransforms/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var startIndex: JointTransforms.Index](jointtransforms/startindex.md)
  An index to the first joint transform in the collection.
- [var endIndex: JointTransforms.Index](jointtransforms/endindex.md)
  An index to the last joint transform in the collection.
- [var isEmpty: Bool](jointtransforms/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var last: Self.Element?](jointtransforms/last.md)
  The last element of the collection.
- [var lazy: LazySequence<Self>](jointtransforms/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [var publisher: Publishers.Sequence<Self, Never>](jointtransforms/publisher.md)
- [var underestimatedCount: Int](jointtransforms/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Accessing joint transforms
- [subscript(JointTransforms.Index) -> Transform](jointtransforms/subscript(_:).md)
  Accesses a single joint transform in the collection at the given index.
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](jointtransforms/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](jointtransforms/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func contains(Self.Element) -> Bool](jointtransforms/contains(_:).md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](jointtransforms/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](jointtransforms/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](jointtransforms/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func distance(from: Self.Index, to: Self.Index) -> Int](jointtransforms/distance(from:to:).md)
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](jointtransforms/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](jointtransforms/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](jointtransforms/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](jointtransforms/elementsequal(_:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](jointtransforms/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func enumerated() -> EnumeratedSequence<Self>](jointtransforms/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](jointtransforms/filter(_:).md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](jointtransforms/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func firstIndex(of: Self.Element) -> Self.Index?](jointtransforms/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](jointtransforms/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](jointtransforms/flatmap(_:)-1as7d.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func forEach((Self.Element) throws -> Void) rethrows](jointtransforms/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func formIndex(inout Self.Index, offsetBy: Int)](jointtransforms/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](jointtransforms/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func formIndex(after: inout Self.Index)](jointtransforms/formindex(after:).md)
  Replaces the given index with its successor.
- [func formIndex(before: inout Self.Index)](jointtransforms/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func formatted<S>(S) -> S.FormatOutput](jointtransforms/formatted(_:).md)
- [func index(Self.Index, offsetBy: Int) -> Self.Index](jointtransforms/index(_:offsetby:).md)
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](jointtransforms/index(_:offsetby:limitedby:).md)
- [func index(after: JointTransforms.Index) -> JointTransforms.Index](jointtransforms/index(after:).md)
  Returns the position in the sequence of the joint that follows the given position.
- [func index(before: JointTransforms.Index) -> JointTransforms.Index](jointtransforms/index(before:).md)
  Returns the position in the sequence of the joint that preceeds the given position.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](jointtransforms/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](jointtransforms/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](jointtransforms/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](jointtransforms/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
- [func makeIterator() -> IndexingIterator<Self>](jointtransforms/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](jointtransforms/map(_:)-8zpgc.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](jointtransforms/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](jointtransforms/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func partition(by: (Self.Element) throws -> Bool) rethrows -> Self.Index](jointtransforms/partition(by:)-pjjr.md)
  Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [func prefix(Int) -> Self.SubSequence](jointtransforms/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](jointtransforms/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](jointtransforms/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](jointtransforms/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func randomElement() -> Self.Element?](jointtransforms/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](jointtransforms/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](jointtransforms/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](jointtransforms/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reverse()](jointtransforms/reverse.md)
  Reverses the elements of the collection in place.
- [func reversed() -> ReversedCollection<Self>](jointtransforms/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func shuffled() -> [Self.Element]](jointtransforms/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](jointtransforms/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](jointtransforms/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func sorted<Comparator>(using: Comparator) -> [Self.Element]](jointtransforms/sorted(using:)-5o7zi.md)
  Returns the elements of the sequence, sorted using the given comparator to compare elements.
- [func sorted<S, Comparator>(using: S) -> [Self.Element]](jointtransforms/sorted(using:)-3wbdj.md)
  Returns the elements of the sequence, sorted using the given array of `SortComparator`s to compare elements.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](jointtransforms/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](jointtransforms/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](jointtransforms/starts(with:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](jointtransforms/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [func suffix(Int) -> Self.SubSequence](jointtransforms/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](jointtransforms/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
- [func swapAt(Self.Index, Self.Index)](jointtransforms/swapat(_:_:).md)
  Exchanges the values at the specified indices of the collection.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R?](jointtransforms/withcontiguousmutablestorageifavailable(_:).md)
  Executes a closure on the collection’s contiguous storage.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](jointtransforms/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.
### Comparing joint transforms
- [static func == (JointTransforms, JointTransforms) -> Bool](jointtransforms/==(_:_:).md)
  Returns a Boolean value that indicates whether two collections of joints are equal.
- [static func != (Self, Self) -> Bool](jointtransforms/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func compare<Comparator>(Comparator.Compared, Comparator.Compared) -> ComparisonResult](jointtransforms/compare(_:_:).md)
  If `lhs` is ordered before `rhs` in the ordering described by the given sequence of `SortComparator`s
### Deprecated
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](jointtransforms/flatmap(_:)-4w5mr.md)
- [func index(of: Self.Element) -> Self.Index?](jointtransforms/index(of:).md)
  Returns the first index where the specified value appears in the collection.
### Default Implementations
- [BidirectionalCollection Implementations](jointtransforms/bidirectionalcollection-implementations.md)
- [Collection Implementations](jointtransforms/collection-implementations.md)
- [Decodable Implementations](jointtransforms/decodable-implementations.md)
- [Encodable Implementations](jointtransforms/encodable-implementations.md)
- [Equatable Implementations](jointtransforms/equatable-implementations.md)
- [MutableCollection Implementations](jointtransforms/mutablecollection-implementations.md)
- [Sequence Implementations](jointtransforms/sequence-implementations.md)

## Relationships

### Conforms To
- [AnimatableData](animatabledata.md)
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [MutableCollection](../Swift/MutableCollection.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/jointtransforms)*