# AsyncSequence Implementations

**Framework**: Swift

## Topics

### Instance Methods
- [func allSatisfy((Self.Element) async throws -> Bool) async rethrows -> Bool](asyncflatmapsequence/allsatisfy(_:).md)
  Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.
- [func compactMap<ElementOfResult>((Self.Element) async throws -> ElementOfResult?) -> AsyncThrowingCompactMapSequence<Self, ElementOfResult>](asyncflatmapsequence/compactmap(_:)-2yntz.md)
  Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [func compactMap<ElementOfResult>((Self.Element) async -> ElementOfResult?) -> AsyncCompactMapSequence<Self, ElementOfResult>](asyncflatmapsequence/compactmap(_:)-4j12y.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [func contains(Self.Element) async rethrows -> Bool](asyncflatmapsequence/contains(_:).md)
  Returns a Boolean value that indicates whether the asynchronous sequence contains the given element.
- [func contains(where: (Self.Element) async throws -> Bool) async rethrows -> Bool](asyncflatmapsequence/contains(where:).md)
  Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.
- [func drop(while: (Self.Element) async -> Bool) -> AsyncDropWhileSequence<Self>](asyncflatmapsequence/drop(while:).md)
  Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [func dropFirst(Int) -> AsyncDropFirstSequence<Self>](asyncflatmapsequence/dropfirst(_:).md)
  Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [func filter((Self.Element) async -> Bool) -> AsyncFilterSequence<Self>](asyncflatmapsequence/filter(_:).md)
  Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
- [func first(where: (Self.Element) async throws -> Bool) async rethrows -> Self.Element?](asyncflatmapsequence/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func flatMap<SegmentOfResult>((Self.Element) async -> SegmentOfResult) -> AsyncFlatMapSequence<Self, SegmentOfResult>](asyncflatmapsequence/flatmap(_:)-2m43v.md)
  Creates an asynchronous sequence that concatenates the results of calling the given transformation with each element of this sequence.
- [func flatMap<SegmentOfResult>((Self.Element) async -> SegmentOfResult) -> AsyncFlatMapSequence<Self, SegmentOfResult>](asyncflatmapsequence/flatmap(_:)-541qn.md)
  Creates an asynchronous sequence that concatenates the results of calling the given transformation with each element of this sequence.
- [func flatMap<SegmentOfResult>((Self.Element) async throws -> SegmentOfResult) -> AsyncThrowingFlatMapSequence<Self, SegmentOfResult>](asyncflatmapsequence/flatmap(_:)-67uer.md)
  Creates an asynchronous sequence that concatenates the results of calling the given error-throwing transformation with each element of this sequence.
- [func flatMap<SegmentOfResult>((Self.Element) async -> SegmentOfResult) -> AsyncFlatMapSequence<Self, SegmentOfResult>](asyncflatmapsequence/flatmap(_:)-7wopu.md)
  Creates an asynchronous sequence that concatenates the results of calling the given transformation with each element of this sequence.
- [func makeAsyncIterator() -> AsyncFlatMapSequence<Base, SegmentOfResult>.Iterator](asyncflatmapsequence/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [func map<Transformed>((Self.Element) async throws -> Transformed) -> AsyncThrowingMapSequence<Self, Transformed>](asyncflatmapsequence/map(_:)-5ncr2.md)
  Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [func map<Transformed>((Self.Element) async -> Transformed) -> AsyncMapSequence<Self, Transformed>](asyncflatmapsequence/map(_:)-wssh.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [func max() async rethrows -> Self.Element?](asyncflatmapsequence/max.md)
  Returns the maximum element in an asynchronous sequence of comparable elements.
- [func max(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](asyncflatmapsequence/max(by:).md)
  Returns the maximum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [func min() async rethrows -> Self.Element?](asyncflatmapsequence/min.md)
  Returns the minimum element in an asynchronous sequence of comparable elements.
- [func min(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](asyncflatmapsequence/min(by:).md)
  Returns the minimum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [func prefix(Int) -> AsyncPrefixSequence<Self>](asyncflatmapsequence/prefix(_:).md)
  Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.
- [func prefix(while: (Self.Element) async -> Bool) rethrows -> AsyncPrefixWhileSequence<Self>](asyncflatmapsequence/prefix(while:).md)
  Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given predicate.
- [func reduce<Result>(Result, (Result, Self.Element) async throws -> Result) async rethrows -> Result](asyncflatmapsequence/reduce(_:_:).md)
  Returns the result of combining the elements of the asynchronous sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) async throws -> Void) async rethrows -> Result](asyncflatmapsequence/reduce(into:_:).md)
  Returns the result of combining the elements of the asynchronous sequence using the given closure, given a mutable initial value.
### Type Aliases
- [AsyncFlatMapSequence.AsyncIterator](asyncflatmapsequence/asynciterator.md)
  The type of iterator that produces elements of the sequence.
- [AsyncFlatMapSequence.Element](asyncflatmapsequence/element.md)
  The type of element produced by this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncflatmapsequence/asyncsequence-implementations)*