# PhotogrammetrySession.Outputs

**Framework**: RealityKit  
**Kind**: struct

An asynchronous sequence of session-related updates.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
struct Outputs
```

## Topics

### Iterating the collection
- [func makeAsyncIterator() -> PhotogrammetrySession.Outputs.Iterator](photogrammetrysession/outputs-swift.struct/makeasynciterator.md)
  Creates an asynchronous iterator for the collection.
- [PhotogrammetrySession.Outputs.AsyncIterator](photogrammetrysession/outputs-swift.struct/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [PhotogrammetrySession.Outputs.Element](photogrammetrysession/outputs-swift.struct/element.md)
  The type of element used for Photogrammetry Session updates.
- [PhotogrammetrySession.Outputs.Iterator](photogrammetrysession/outputs-swift.struct/iterator.md)
  An object for iterating over published output objects.
### Filtering the output
- [func allSatisfy((Self.Element) async throws -> Bool) async rethrows -> Bool](photogrammetrysession/outputs-swift.struct/allsatisfy(_:).md)
  Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.
- [func compactMap<ElementOfResult>((Self.Element) async throws -> ElementOfResult?) -> AsyncThrowingCompactMapSequence<Self, ElementOfResult>](photogrammetrysession/outputs-swift.struct/compactmap(_:)-23p7w.md)
  Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [func compactMap<ElementOfResult>((Self.Element) async -> ElementOfResult?) -> AsyncCompactMapSequence<Self, ElementOfResult>](photogrammetrysession/outputs-swift.struct/compactmap(_:)-1is99.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [func contains(where: (Self.Element) async throws -> Bool) async rethrows -> Bool](photogrammetrysession/outputs-swift.struct/contains(where:).md)
  Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.
- [func drop(while: (Self.Element) async -> Bool) -> AsyncDropWhileSequence<Self>](photogrammetrysession/outputs-swift.struct/drop(while:).md)
  Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [func dropFirst(Int) -> AsyncDropFirstSequence<Self>](photogrammetrysession/outputs-swift.struct/dropfirst(_:).md)
  Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [func filter((Self.Element) async -> Bool) -> AsyncFilterSequence<Self>](photogrammetrysession/outputs-swift.struct/filter(_:).md)
  Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
- [func first(where: (Self.Element) async throws -> Bool) async rethrows -> Self.Element?](photogrammetrysession/outputs-swift.struct/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func flatMap<SegmentOfResult>((Self.Element) async throws -> SegmentOfResult) -> AsyncThrowingFlatMapSequence<Self, SegmentOfResult>](photogrammetrysession/outputs-swift.struct/flatmap(_:)-3x2or.md)
  Creates an asynchronous sequence that concatenates the results of calling the given error-throwing transformation with each element of this sequence.
- [func map<Transformed>((Self.Element) async throws -> Transformed) -> AsyncThrowingMapSequence<Self, Transformed>](photogrammetrysession/outputs-swift.struct/map(_:)-4yzto.md)
  Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [func map<Transformed>((Self.Element) async -> Transformed) -> AsyncMapSequence<Self, Transformed>](photogrammetrysession/outputs-swift.struct/map(_:)-2b175.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [func prefix(Int) -> AsyncPrefixSequence<Self>](photogrammetrysession/outputs-swift.struct/prefix(_:).md)
  Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.
- [func prefix(while: (Self.Element) async -> Bool) rethrows -> AsyncPrefixWhileSequence<Self>](photogrammetrysession/outputs-swift.struct/prefix(while:).md)
  Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given predicate.
### Default Implementations
- [AsyncSequence Implementations](photogrammetrysession/outputs-swift.struct/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [PhotogrammetrySession.Outputs.AsyncIterator](photogrammetrysession/outputs-swift.struct/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [PhotogrammetrySession.Outputs.Element](photogrammetrysession/outputs-swift.struct/element.md)
  The type of element used for Photogrammetry Session updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/outputs-swift.struct)*