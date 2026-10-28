# filter(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.

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
func filter(_ isIncluded: @escaping @Sendable (Self.Element) async -> Bool) -> AsyncFilterSequence<Self>
```

## Return Value

An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.

## Discussion

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `filter(_:)` method returns `true` for even values and `false` for odd values, thereby filtering out the odd values:

```swift
let stream = Counter(howHigh: 10)
    .filter { $0 % 2 == 0 }
for await number in stream {
    print(number, terminator: " ")
}
// Prints "2 4 6 8 10 "
```

## Parameters

- `isIncluded`: A closure that takes an element of the asynchronous sequence as its argument and returns a Boolean value that indicates whether to include the element in the filtered sequence.

## See Also

### Accessing an Asynchronous Sequence of Results
- [func makeAsyncIterator() -> TaskGroup<ChildTaskResult>.Iterator](./makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [func allSatisfy((Self.Element) async throws -> Bool) async rethrows -> Bool](./allsatisfy%28_%29.md)
  Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.
- [func compactMap<ElementOfResult>((Self.Element) async throws -> ElementOfResult?) -> AsyncThrowingCompactMapSequence<Self, ElementOfResult>](./compactmap%28_%29-944od.md)
  Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [func compactMap<ElementOfResult>((Self.Element) async -> ElementOfResult?) -> AsyncCompactMapSequence<Self, ElementOfResult>](./compactmap%28_%29-7mgj1.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [func contains(Self.Element) async rethrows -> Bool](./contains%28_%29.md)
  Returns a Boolean value that indicates whether the asynchronous sequence contains the given element.
- [func contains(where: (Self.Element) async throws -> Bool) async rethrows -> Bool](./contains%28where%29.md)
  Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.
- [func drop(while: (Self.Element) async -> Bool) -> AsyncDropWhileSequence<Self>](./drop%28while%29.md)
  Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [func dropFirst(Int) -> AsyncDropFirstSequence<Self>](./dropfirst%28_%29.md)
  Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [func first(where: (Self.Element) async throws -> Bool) async rethrows -> Self.Element?](./first%28where%29.md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func flatMap<SegmentOfResult>((Self.Element) async throws -> SegmentOfResult) -> AsyncThrowingFlatMapSequence<Self, SegmentOfResult>](./flatmap%28_%29-vhi3.md)
  Creates an asynchronous sequence that concatenates the results of calling the given error-throwing transformation with each element of this sequence.
- [func map<Transformed>((Self.Element) async throws -> Transformed) -> AsyncThrowingMapSequence<Self, Transformed>](./map%28_%29-58nsr.md)
  Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [func map<Transformed>((Self.Element) async -> Transformed) -> AsyncMapSequence<Self, Transformed>](./map%28_%29-4a4kq.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [func max() async rethrows -> Self.Element?](./max%28%29.md)
  Returns the maximum element in an asynchronous sequence of comparable elements.
- [func max(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](./max%28by%29.md)
  Returns the maximum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [func min() async rethrows -> Self.Element?](./min%28%29.md)
  Returns the minimum element in an asynchronous sequence of comparable elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/taskgroup/filter(_:))*