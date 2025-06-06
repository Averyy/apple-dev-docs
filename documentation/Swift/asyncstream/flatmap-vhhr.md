# flatMap(_:)

**Framework**: Swift  
**Kind**: method

Creates an asynchronous sequence that concatenates the results of calling the given error-throwing transformation with each element of this sequence.

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
@preconcurrency
func flatMap<SegmentOfResult>(_ transform: @escaping (Self.Element) async throws -> SegmentOfResult) -> AsyncThrowingFlatMapSequence<Self, SegmentOfResult> where SegmentOfResult : AsyncSequence
```

#### Return Value

A single, flattened asynchronous sequence that contains all elements in all the asynchronous sequences produced by `transform`. The sequence ends either when the last sequence created from the last element from base sequence ends, or when `transform` throws an error.

#### Discussion

Use this method to receive a single-level asynchronous sequence when your transformation produces an asynchronous sequence for each element.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `5`. The transforming closure takes the received `Int` and returns a new `Counter` that counts that high. For example, when the transform receives `3` from the base sequence, it creates a new `Counter` that produces the values `1`, `2`, and `3`. The `flatMap(_:)` method “flattens” the resulting sequence-of-sequences into a single `AsyncSequence`. However, when the closure receives `4`, it throws an error, terminating the sequence.

```swift
do {
    let stream = Counter(howHigh: 5)
        .flatMap { (value) -> Counter in
            if value == 4 {
                throw MyError()
            }
            return Counter(howHigh: value)
        }
    for try await number in stream {
        print(number, terminator: " ")
    }
} catch {
    print(error)
}
// Prints "1 1 2 1 2 3 MyError() "
```

## Parameters

- `transform`: An error-throwing mapping closure.    accepts an element of this sequence as its parameter and returns an   . If   throws an error, the sequence ends.

## See Also

- [func map<Transformed>((Self.Element) async throws -> Transformed) -> AsyncThrowingMapSequence<Self, Transformed>](asyncstream/map(_:)-58nsf.md)
  Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [func map<Transformed>((Self.Element) async -> Transformed) -> AsyncMapSequence<Self, Transformed>](asyncstream/map(_:)-4a4la.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [func compactMap<ElementOfResult>((Self.Element) async -> ElementOfResult?) -> AsyncCompactMapSequence<Self, ElementOfResult>](asyncstream/compactmap(_:)-7mgjd.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [func compactMap<ElementOfResult>((Self.Element) async throws -> ElementOfResult?) -> AsyncThrowingCompactMapSequence<Self, ElementOfResult>](asyncstream/compactmap(_:)-944op.md)
  Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [func reduce<Result>(Result, (Result, Self.Element) async throws -> Result) async rethrows -> Result](asyncstream/reduce(_:_:).md)
  Returns the result of combining the elements of the asynchronous sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) async throws -> Void) async rethrows -> Result](asyncstream/reduce(into:_:).md)
  Returns the result of combining the elements of the asynchronous sequence using the given closure, given a mutable initial value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncstream/flatmap(_:)-vhhr)*