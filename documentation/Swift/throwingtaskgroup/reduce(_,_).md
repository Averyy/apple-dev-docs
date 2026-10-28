# reduce(_:_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns the result of combining the elements of the asynchronous sequence using the given closure.

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
func reduce<Result>(_ initialResult: Result, _ nextPartialResult: (Result, Self.Element) async throws -> Result) async rethrows -> Result
```

## Return Value

The final accumulated value. If the sequence has no elements, the result is `initialResult`.

## Discussion

Use the `reduce(_:_:)` method to produce a single value from the elements of an entire sequence. For example, you can use this method on an sequence of numbers to find their sum or product.

The `nextPartialResult` closure executes sequentially with an accumulating value initialized to `initialResult` and each element of the sequence.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `4`. The `reduce(_:_:)` method sums the values received from the asynchronous sequence.

```swift
let sum = await Counter(howHigh: 4)
    .reduce(0) {
        $0 + $1
    }
print(sum)
// Prints "10"
```

## Parameters

- `initialResult`: The value to use as the initial accumulating value. The `nextPartialResult` closure receives `initialResult` the first time the closure runs.
- `nextPartialResult`: A closure that combines an accumulating value and an element of the asynchronous sequence into a new accumulating value, for use in the next call of the `nextPartialResult` closure or returned to the caller.

## See Also

### Accessing an Asynchronous Sequence of Results
- [func makeAsyncIterator() -> ThrowingTaskGroup<ChildTaskResult, Failure>.Iterator](./makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [func allSatisfy((Self.Element) async throws -> Bool) async rethrows -> Bool](./allsatisfy%28_%29.md)
  Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.
- [func compactMap<ElementOfResult>((Self.Element) async throws -> ElementOfResult?) -> AsyncThrowingCompactMapSequence<Self, ElementOfResult>](./compactmap%28_%29-944nh.md)
  Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [func compactMap<ElementOfResult>((Self.Element) async -> ElementOfResult?) -> AsyncCompactMapSequence<Self, ElementOfResult>](./compactmap%28_%29-7mgi5.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [func contains(Self.Element) async rethrows -> Bool](./contains%28_%29.md)
  Returns a Boolean value that indicates whether the asynchronous sequence contains the given element.
- [func contains(where: (Self.Element) async throws -> Bool) async rethrows -> Bool](./contains%28where%29.md)
  Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.
- [func drop(while: (Self.Element) async -> Bool) -> AsyncDropWhileSequence<Self>](./drop%28while%29.md)
  Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [func dropFirst(Int) -> AsyncDropFirstSequence<Self>](./dropfirst%28_%29.md)
  Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [func filter((Self.Element) async -> Bool) -> AsyncFilterSequence<Self>](./filter%28_%29.md)
  Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
- [func first(where: (Self.Element) async throws -> Bool) async rethrows -> Self.Element?](./first%28where%29.md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func map<Transformed>((Self.Element) async throws -> Transformed) -> AsyncThrowingMapSequence<Self, Transformed>](./map%28_%29-58nrv.md)
  Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [func map<Transformed>((Self.Element) async -> Transformed) -> AsyncMapSequence<Self, Transformed>](./map%28_%29-4a4ju.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [func max() async rethrows -> Self.Element?](./max%28%29.md)
  Returns the maximum element in an asynchronous sequence of comparable elements.
- [func max(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](./max%28by%29.md)
  Returns the maximum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [func min() async rethrows -> Self.Element?](./min%28%29.md)
  Returns the minimum element in an asynchronous sequence of comparable elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/reduce(_:_:))*