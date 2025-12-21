# AsyncSequence

**Framework**: Swift  
**Kind**: protocol

A type that provides asynchronous, sequential, iterated access to its elements.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
protocol AsyncSequence<Element, Failure>
```

#### Overview

An `AsyncSequence` resembles the `Sequence` type — offering a list of values you can step through one at a time — and adds asynchronicity. An `AsyncSequence` may have all, some, or none of its values available when you first use it. Instead, you use `await` to receive values as they become available.

As with `Sequence`, you typically iterate through an `AsyncSequence` with a `for await`-`in` loop. However, because the caller must potentially wait for values, you use the `await` keyword. The following example shows how to iterate over `Counter`, a custom `AsyncSequence` that produces `Int` values from `1` up to a `howHigh` value:

```swift
for await number in Counter(howHigh: 10) {
    print(number, terminator: " ")
}
// Prints "1 2 3 4 5 6 7 8 9 10 "
```

An `AsyncSequence` doesn’t generate or contain the values; it just defines how you access them. Along with defining the type of values as an associated type called `Element`, the `AsyncSequence` defines a `makeAsyncIterator()` method. This returns an instance of type `AsyncIterator`. Like the standard `IteratorProtocol`, the `AsyncIteratorProtocol` defines a single `next()` method to produce elements. The difference is that the `AsyncIterator` defines its `next()` method as `async`, which requires a caller to wait for the next value with the `await` keyword.

`AsyncSequence` also defines methods for processing the elements you receive, modeled on the operations provided by the basic `Sequence` in the standard library. There are two categories of methods: those that return a single value, and those that return another `AsyncSequence`.

Single-value methods eliminate the need for a `for await`-`in` loop, and instead let you make a single `await` call. For example, the `contains(_:)` method returns a Boolean value that indicates if a given value exists in the `AsyncSequence`. Given the `Counter` sequence from the previous example, you can test for the existence of a sequence member with a one-line call:

```swift
let found = await Counter(howHigh: 10).contains(5) // true
```

Methods that return another `AsyncSequence` return a type specific to the method’s semantics. For example, the `.map(_:)` method returns a `AsyncMapSequence` (or a `AsyncThrowingMapSequence`, if the closure you provide to the `map(_:)` method can throw an error). These returned sequences don’t eagerly await the next member of the sequence, which allows the caller to decide when to start work. Typically, you’ll iterate over these sequences with `for await`-`in`, like the base `AsyncSequence` you started with. In the following example, the `map(_:)` method transforms each `Int` received from a `Counter` sequence into a `String`:

```swift
let stream = Counter(howHigh: 10)
    .map { $0 % 2 == 0 ? "Even" : "Odd" }
for await s in stream {
    print(s, terminator: " ")
}
// Prints "Odd Even Odd Even Odd Even Odd Even Odd Even "
```

## Topics

### Creating an Iterator
- [func makeAsyncIterator() -> Self.AsyncIterator](asyncsequence/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [associatedtype AsyncIterator : AsyncIteratorProtocol](asyncsequence/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [protocol AsyncIteratorProtocol](asynciteratorprotocol.md)
  A type that asynchronously supplies the values of a sequence one at a time.
- [associatedtype Element](asyncsequence/element.md)
  The type of element produced by this asynchronous sequence.
### Finding Elements
- [func contains(Self.Element) async rethrows -> Bool](asyncsequence/contains(_:).md)
  Returns a Boolean value that indicates whether the asynchronous sequence contains the given element.
- [func contains(where: (Self.Element) async throws -> Bool) async rethrows -> Bool](asyncsequence/contains(where:).md)
  Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.
- [func allSatisfy((Self.Element) async throws -> Bool) async rethrows -> Bool](asyncsequence/allsatisfy(_:).md)
  Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.
- [func first(where: (Self.Element) async throws -> Bool) async rethrows -> Self.Element?](asyncsequence/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func min() async rethrows -> Self.Element?](asyncsequence/min.md)
  Returns the minimum element in an asynchronous sequence of comparable elements.
- [func min(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](asyncsequence/min(by:).md)
  Returns the minimum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [func max() async rethrows -> Self.Element?](asyncsequence/max.md)
  Returns the maximum element in an asynchronous sequence of comparable elements.
- [func max(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](asyncsequence/max(by:).md)
  Returns the maximum element in the asynchronous sequence, using the given predicate as the comparison between elements.
### Selecting Elements
- [func prefix(Int) -> AsyncPrefixSequence<Self>](asyncsequence/prefix(_:).md)
  Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.
- [struct AsyncPrefixSequence](asyncprefixsequence.md)
  An asynchronous sequence, up to a specified maximum length, containing the initial elements of a base asynchronous sequence.
- [func prefix(while: (Self.Element) async -> Bool) rethrows -> AsyncPrefixWhileSequence<Self>](asyncsequence/prefix(while:)-2xy95.md)
  Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given predicate.
- [struct AsyncPrefixWhileSequence](asyncprefixwhilesequence.md)
  An asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy a given predicate.
- [func prefix(while: (Self.Element) async throws -> Bool) rethrows -> AsyncThrowingPrefixWhileSequence<Self>](asyncsequence/prefix(while:)-6yp5n.md)
  Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given error-throwing predicate.
- [struct AsyncThrowingPrefixWhileSequence](asyncthrowingprefixwhilesequence.md)
  An asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given error-throwing predicate.
### Excluding Elements
- [func dropFirst(Int) -> AsyncDropFirstSequence<Self>](asyncsequence/dropfirst(_:).md)
  Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [struct AsyncDropFirstSequence](asyncdropfirstsequence.md)
  An asynchronous sequence which omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [func drop(while: (Self.Element) async -> Bool) -> AsyncDropWhileSequence<Self>](asyncsequence/drop(while:)-9sp3b.md)
  Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [struct AsyncDropWhileSequence](asyncdropwhilesequence.md)
  An asynchronous sequence which omits elements from the base sequence until a given closure returns false, after which it passes through all remaining elements.
- [func drop(while: (Self.Element) async throws -> Bool) -> AsyncThrowingDropWhileSequence<Self>](asyncsequence/drop(while:)-67kgo.md)
  Omits elements from the base sequence until a given error-throwing closure returns false, after which it passes through all remaining elements.
- [struct AsyncThrowingDropWhileSequence](asyncthrowingdropwhilesequence.md)
  An asynchronous sequence which omits elements from the base sequence until a given error-throwing closure returns false, after which it passes through all remaining elements.
- [func filter((Self.Element) async -> Bool) -> AsyncFilterSequence<Self>](asyncsequence/filter(_:)-435af.md)
  Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
- [struct AsyncFilterSequence](asyncfiltersequence.md)
  An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy a given predicate.
- [func filter((Self.Element) async throws -> Bool) -> AsyncThrowingFilterSequence<Self>](asyncsequence/filter(_:)-2cc0l.md)
  Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given error-throwing predicate.
- [struct AsyncThrowingFilterSequence](asyncthrowingfiltersequence.md)
  An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given error-throwing predicate.
### Transforming a Sequence
- [func map<Transformed>((Self.Element) async -> Transformed) -> AsyncMapSequence<Self, Transformed>](asyncsequence/map(_:)-1q1k3.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [struct AsyncMapSequence](asyncmapsequence.md)
  An asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [func map<Transformed>((Self.Element) async throws -> Transformed) -> AsyncThrowingMapSequence<Self, Transformed>](asyncsequence/map(_:)-70wgb.md)
  Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [struct AsyncThrowingMapSequence](asyncthrowingmapsequence.md)
  An asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [func compactMap<ElementOfResult>((Self.Element) async -> ElementOfResult?) -> AsyncCompactMapSequence<Self, ElementOfResult>](asyncsequence/compactmap(_:)-gfdq.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [struct AsyncCompactMapSequence](asynccompactmapsequence.md)
  An asynchronous sequence that maps a given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [func compactMap<ElementOfResult>((Self.Element) async throws -> ElementOfResult?) -> AsyncThrowingCompactMapSequence<Self, ElementOfResult>](asyncsequence/compactmap(_:)-1f8zn.md)
  Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [struct AsyncThrowingCompactMapSequence](asyncthrowingcompactmapsequence.md)
  An asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [struct AsyncFlatMapSequence](asyncflatmapsequence.md)
  An asynchronous sequence that concatenates the results of calling a given transformation with each element of this sequence.
- [struct AsyncThrowingFlatMapSequence](asyncthrowingflatmapsequence.md)
  An asynchronous sequence that concatenates the results of calling a given error-throwing transformation with each element of this sequence.
- [func reduce<Result>(Result, (Result, Self.Element) async throws -> Result) async rethrows -> Result](asyncsequence/reduce(_:_:).md)
  Returns the result of combining the elements of the asynchronous sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) async throws -> Void) async rethrows -> Result](asyncsequence/reduce(into:_:).md)
  Returns the result of combining the elements of the asynchronous sequence using the given closure, given a mutable initial value.
### Adapting Textual Sequences
- [var characters: AsyncCharacterSequence<Self>](asyncsequence/characters.md)
  A non-blocking sequence of `Characters` created by decoding the elements of `self` as UTF8.
- [struct AsyncCharacterSequence](../Foundation/AsyncCharacterSequence.md)
  An asynchronous sequence of characters.
- [var unicodeScalars: AsyncUnicodeScalarSequence<Self>](asyncsequence/unicodescalars.md)
  A non-blocking sequence of `UnicodeScalars` created by decoding the elements of `self` as UTF8.
- [struct AsyncUnicodeScalarSequence](../Foundation/AsyncUnicodeScalarSequence.md)
  An asychronous sequence of Unicode scalar values.
- [var lines: AsyncLineSequence<Self>](asyncsequence/lines.md)
  A non-blocking sequence of newline-separated `Strings` created by decoding the elements of `self` as UTF8.
- [struct AsyncLineSequence](../Foundation/AsyncLineSequence.md)
  An asynchronous sequence of lines of text.
### Associated Types
- [associatedtype Failure = any Error](asyncsequence/failure.md)
  The type of errors produced when iteration over the sequence fails.
### Instance Methods
- [func flatMap<SegmentOfResult>((Self.Element) async -> SegmentOfResult) -> AsyncFlatMapSequence<Self, SegmentOfResult>](asyncsequence/flatmap(_:)-4bl9a.md)
  Creates an asynchronous sequence that concatenates the results of calling the given transformation with each element of this sequence.
- [func flatMap<SegmentOfResult>((Self.Element) async -> SegmentOfResult) -> AsyncFlatMapSequence<Self, SegmentOfResult>](asyncsequence/flatmap(_:)-54rrt.md)
  Creates an asynchronous sequence that concatenates the results of calling the given transformation with each element of this sequence.
- [func flatMap<SegmentOfResult>((Self.Element) async throws -> SegmentOfResult) -> AsyncThrowingFlatMapSequence<Self, SegmentOfResult>](asyncsequence/flatmap(_:)-5j8ra.md)
  Creates an asynchronous sequence that concatenates the results of calling the given error-throwing transformation with each element of this sequence.
- [func flatMap<SegmentOfResult>((Self.Element) async -> SegmentOfResult) -> AsyncFlatMapSequence<Self, SegmentOfResult>](asyncsequence/flatmap(_:)-5rn1j.md)
  Creates an asynchronous sequence that concatenates the results of calling the given transformation with each element of this sequence.

## Relationships

### Conforming Types
- [AsyncCompactMapSequence](asynccompactmapsequence.md)
- [AsyncDropFirstSequence](asyncdropfirstsequence.md)
- [AsyncDropWhileSequence](asyncdropwhilesequence.md)
- [AsyncFilterSequence](asyncfiltersequence.md)
- [AsyncFlatMapSequence](asyncflatmapsequence.md)
- [AsyncMapSequence](asyncmapsequence.md)
- [AsyncPrefixSequence](asyncprefixsequence.md)
- [AsyncPrefixWhileSequence](asyncprefixwhilesequence.md)
- [AsyncStream](asyncstream.md)
- [AsyncThrowingCompactMapSequence](asyncthrowingcompactmapsequence.md)
- [AsyncThrowingDropWhileSequence](asyncthrowingdropwhilesequence.md)
- [AsyncThrowingFilterSequence](asyncthrowingfiltersequence.md)
- [AsyncThrowingFlatMapSequence](asyncthrowingflatmapsequence.md)
- [AsyncThrowingMapSequence](asyncthrowingmapsequence.md)
- [AsyncThrowingPrefixWhileSequence](asyncthrowingprefixwhilesequence.md)
- [AsyncThrowingStream](asyncthrowingstream.md)
- [Observations](../observation/observations.md)
- [TaskGroup](taskgroup.md)
- [ThrowingTaskGroup](throwingtaskgroup.md)

## See Also

- [struct AsyncStream](asyncstream.md)
  An asynchronous sequence generated from a closure that calls a continuation to produce new elements.
- [struct AsyncThrowingStream](asyncthrowingstream.md)
  An asynchronous sequence generated from an error-throwing closure that calls a continuation to produce new elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncsequence)*