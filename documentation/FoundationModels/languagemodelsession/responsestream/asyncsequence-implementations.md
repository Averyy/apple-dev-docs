# AsyncSequence Implementations

**Framework**: Foundation Models

## Topics

### Structures
- [LanguageModelSession.ResponseStream.AsyncIterator](languagemodelsession/responsestream/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
### Instance Properties
- [var characters: AsyncCharacterSequence<Self>](languagemodelsession/responsestream/characters.md)
  A non-blocking sequence of `Characters` created by decoding the elements of `self` as UTF8.
- [var lines: AsyncLineSequence<Self>](languagemodelsession/responsestream/lines.md)
  A non-blocking sequence of newline-separated `Strings` created by decoding the elements of `self` as UTF8.
- [var unicodeScalars: AsyncUnicodeScalarSequence<Self>](languagemodelsession/responsestream/unicodescalars.md)
  A non-blocking sequence of `UnicodeScalars` created by decoding the elements of `self` as UTF8.
### Instance Methods
- [func allSatisfy((Self.Element) async throws -> Bool) async rethrows -> Bool](languagemodelsession/responsestream/allsatisfy(_:).md)
  Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.
- [func compactMap(_:)](languagemodelsession/responsestream/compactmap(_:).md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [func compactMap<ElementOfResult>((Self.Element) async throws -> ElementOfResult?) -> AsyncThrowingCompactMapSequence<Self, ElementOfResult>](languagemodelsession/responsestream/compactmap(_:)-3xs9w.md)
  Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [func compactMap<ElementOfResult>((Self.Element) async -> ElementOfResult?) -> AsyncCompactMapSequence<Self, ElementOfResult>](languagemodelsession/responsestream/compactmap(_:)-4zlli.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [func contains(Self.Element) async rethrows -> Bool](languagemodelsession/responsestream/contains(_:).md)
  Returns a Boolean value that indicates whether the asynchronous sequence contains the given element.
- [func contains(where: (Self.Element) async throws -> Bool) async rethrows -> Bool](languagemodelsession/responsestream/contains(where:).md)
  Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.
- [func drop(while: (Self.Element) async -> Bool) -> AsyncDropWhileSequence<Self>](languagemodelsession/responsestream/drop(while:).md)
  Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [func dropFirst(Int) -> AsyncDropFirstSequence<Self>](languagemodelsession/responsestream/dropfirst(_:).md)
  Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [func filter((Self.Element) async -> Bool) -> AsyncFilterSequence<Self>](languagemodelsession/responsestream/filter(_:).md)
  Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
- [func first(where: (Self.Element) async throws -> Bool) async rethrows -> Self.Element?](languagemodelsession/responsestream/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func flatMap(_:)](languagemodelsession/responsestream/flatmap(_:).md)
  Creates an asynchronous sequence that concatenates the results of calling the given transformation with each element of this sequence.
- [func flatMap<SegmentOfResult>((Self.Element) async throws -> SegmentOfResult) -> AsyncThrowingFlatMapSequence<Self, SegmentOfResult>](languagemodelsession/responsestream/flatmap(_:)-2ty8.md)
  Creates an asynchronous sequence that concatenates the results of calling the given error-throwing transformation with each element of this sequence.
- [func flatMap<SegmentOfResult>((Self.Element) async -> SegmentOfResult) -> AsyncFlatMapSequence<Self, SegmentOfResult>](languagemodelsession/responsestream/flatmap(_:)-52b2j.md)
  Creates an asynchronous sequence that concatenates the results of calling the given transformation with each element of this sequence.
- [func flatMap<SegmentOfResult>((Self.Element) async -> SegmentOfResult) -> AsyncFlatMapSequence<Self, SegmentOfResult>](languagemodelsession/responsestream/flatmap(_:)-6on5g.md)
  Creates an asynchronous sequence that concatenates the results of calling the given transformation with each element of this sequence.
- [func flatMap<SegmentOfResult>((Self.Element) async -> SegmentOfResult) -> AsyncFlatMapSequence<Self, SegmentOfResult>](languagemodelsession/responsestream/flatmap(_:)-9npun.md)
  Creates an asynchronous sequence that concatenates the results of calling the given transformation with each element of this sequence.
- [func makeAsyncIterator() -> LanguageModelSession.ResponseStream<Content>.AsyncIterator](languagemodelsession/responsestream/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [func map(_:)](languagemodelsession/responsestream/map(_:).md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [func map<Transformed>((Self.Element) async -> Transformed) -> AsyncMapSequence<Self, Transformed>](languagemodelsession/responsestream/map(_:)-78boz.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [func map<Transformed>((Self.Element) async throws -> Transformed) -> AsyncThrowingMapSequence<Self, Transformed>](languagemodelsession/responsestream/map(_:)-7xgzd.md)
  Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [func max() async rethrows -> Self.Element?](languagemodelsession/responsestream/max.md)
  Returns the maximum element in an asynchronous sequence of comparable elements.
- [func max(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](languagemodelsession/responsestream/max(by:).md)
  Returns the maximum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [func min() async rethrows -> Self.Element?](languagemodelsession/responsestream/min.md)
  Returns the minimum element in an asynchronous sequence of comparable elements.
- [func min(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](languagemodelsession/responsestream/min(by:).md)
  Returns the minimum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [func prefix(Int) -> AsyncPrefixSequence<Self>](languagemodelsession/responsestream/prefix(_:).md)
  Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.
- [func prefix(while: (Self.Element) async -> Bool) rethrows -> AsyncPrefixWhileSequence<Self>](languagemodelsession/responsestream/prefix(while:).md)
  Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given predicate.
- [func reduce<Result>(Result, (Result, Self.Element) async throws -> Result) async rethrows -> Result](languagemodelsession/responsestream/reduce(_:_:).md)
  Returns the result of combining the elements of the asynchronous sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) async throws -> Void) async rethrows -> Result](languagemodelsession/responsestream/reduce(into:_:).md)
  Returns the result of combining the elements of the asynchronous sequence using the given closure, given a mutable initial value.
### Type Aliases
- [LanguageModelSession.ResponseStream.Element](languagemodelsession/responsestream/element.md)
  The type of element produced by this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/responsestream/asyncsequence-implementations)*