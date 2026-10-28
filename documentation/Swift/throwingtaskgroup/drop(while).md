# drop(while:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.

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
func drop(while predicate: @escaping @Sendable (Self.Element) async -> Bool) -> AsyncDropWhileSequence<Self>
```

## Return Value

An asynchronous sequence that skips over values from the base sequence until the provided closure returns `false`.

## Discussion

Use `drop(while:)` to omit elements from an asynchronous sequence until the element received meets a condition you specify.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `drop(while:)` method causes the modified sequence to ignore received values until it encounters one that is divisible by `3`:

```swift
let stream = Counter(howHigh: 10)
    .drop { $0 % 3 != 0 }
for await number in stream {
    print(number, terminator: " ")
}
// Prints "3 4 5 6 7 8 9 10 "
```

After the predicate returns `false`, the sequence never executes it again, and from then on the sequence passes through elements from its underlying sequence as-is.

## Parameters

- `predicate`: A closure that takes an element as a parameter and returns a Boolean value indicating whether to drop the element from the modified sequence.

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
- [func min(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](./min%28by%29.md)
  Returns the minimum element in the asynchronous sequence, using the given predicate as the comparison between elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/drop(while:))*