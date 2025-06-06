# reduce(into:_:)

**Framework**: Swift  
**Kind**: method

Returns the result of combining the elements of the asynchronous sequence using the given closure, given a mutable initial value.

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
func reduce<Result>(into initialResult: Result, _ updateAccumulatingResult: (inout Result, Self.Element) async throws -> Void) async rethrows -> Result
```

#### Return Value

The final accumulated value. If the sequence has no elements, the result is `initialResult`.

#### Discussion

Use the `reduce(into:_:)` method to produce a single value from the elements of an entire sequence. For example, you can use this method on a sequence of numbers to find their sum or product.

The `updateAccumulatingResult` closure executes sequentially with an accumulating value initialized to `initialResult` and each element of the sequence.

Prefer this method over `reduce(_:_:)` for efficiency when the result is a copy-on-write type, for example an `Array` or `Dictionary`.

## Parameters

- `initialResult`: The value to use as the initial accumulating value.   The   closure receives   the first   time the closure executes.
- `updateAccumulatingResult`: A closure that combines an accumulating   value and an element of the asynchronous sequence into a new   accumulating value, for use in the next call of the    closure or returned to the caller.

## See Also

- [func map<Transformed>((Self.Element) async throws -> Transformed) -> AsyncThrowingMapSequence<Self, Transformed>](asyncstream/map(_:)-58nsf.md)
  Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [func map<Transformed>((Self.Element) async -> Transformed) -> AsyncMapSequence<Self, Transformed>](asyncstream/map(_:)-4a4la.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [func compactMap<ElementOfResult>((Self.Element) async -> ElementOfResult?) -> AsyncCompactMapSequence<Self, ElementOfResult>](asyncstream/compactmap(_:)-7mgjd.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [func compactMap<ElementOfResult>((Self.Element) async throws -> ElementOfResult?) -> AsyncThrowingCompactMapSequence<Self, ElementOfResult>](asyncstream/compactmap(_:)-944op.md)
  Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [func flatMap<SegmentOfResult>((Self.Element) async throws -> SegmentOfResult) -> AsyncThrowingFlatMapSequence<Self, SegmentOfResult>](asyncstream/flatmap(_:)-vhhr.md)
  Creates an asynchronous sequence that concatenates the results of calling the given error-throwing transformation with each element of this sequence.
- [func reduce<Result>(Result, (Result, Self.Element) async throws -> Result) async rethrows -> Result](asyncstream/reduce(_:_:).md)
  Returns the result of combining the elements of the asynchronous sequence using the given closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncstream/reduce(into:_:))*