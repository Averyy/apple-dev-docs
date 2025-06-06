# allSatisfy(_:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.

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
func allSatisfy(_ predicate: (Self.Element) async throws -> Bool) async rethrows -> Bool
```

#### Return Value

`true` if the sequence contains only elements that satisfy `predicate`; otherwise, `false`.

#### Discussion

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `allSatisfy(_:)` method checks to see whether all elements produced by the sequence are less than `10`.

```swift
let allLessThanTen = await Counter(howHigh: 10)
    .allSatisfy { $0 < 10 }
print(allLessThanTen)
// Prints "false"
```

The predicate executes each time the asynchronous sequence produces an element, until either the predicate returns `false` or the sequence ends.

If the asynchronous sequence is empty, this method returns `true`.

## Parameters

- `predicate`: A closure that takes an element of the asynchronous   sequence as its argument and returns a Boolean value that indicates   whether the passed element satisfies a condition.

## See Also

- [func makeAsyncIterator() -> TaskGroup<ChildTaskResult>.Iterator](taskgroup/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [func compactMap<ElementOfResult>((Self.Element) async throws -> ElementOfResult?) -> AsyncThrowingCompactMapSequence<Self, ElementOfResult>](taskgroup/compactmap(_:)-944od.md)
  Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [func compactMap<ElementOfResult>((Self.Element) async -> ElementOfResult?) -> AsyncCompactMapSequence<Self, ElementOfResult>](taskgroup/compactmap(_:)-7mgj1.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [func contains(Self.Element) async rethrows -> Bool](taskgroup/contains(_:).md)
  Returns a Boolean value that indicates whether the asynchronous sequence contains the given element.
- [func contains(where: (Self.Element) async throws -> Bool) async rethrows -> Bool](taskgroup/contains(where:).md)
  Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.
- [func drop(while: (Self.Element) async -> Bool) -> AsyncDropWhileSequence<Self>](taskgroup/drop(while:).md)
  Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [func dropFirst(Int) -> AsyncDropFirstSequence<Self>](taskgroup/dropfirst(_:).md)
  Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [func filter((Self.Element) async -> Bool) -> AsyncFilterSequence<Self>](taskgroup/filter(_:).md)
  Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
- [func first(where: (Self.Element) async throws -> Bool) async rethrows -> Self.Element?](taskgroup/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func flatMap<SegmentOfResult>((Self.Element) async throws -> SegmentOfResult) -> AsyncThrowingFlatMapSequence<Self, SegmentOfResult>](taskgroup/flatmap(_:)-vhi3.md)
  Creates an asynchronous sequence that concatenates the results of calling the given error-throwing transformation with each element of this sequence.
- [func map<Transformed>((Self.Element) async throws -> Transformed) -> AsyncThrowingMapSequence<Self, Transformed>](taskgroup/map(_:)-58nsr.md)
  Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [func map<Transformed>((Self.Element) async -> Transformed) -> AsyncMapSequence<Self, Transformed>](taskgroup/map(_:)-4a4kq.md)
  Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [func max() async rethrows -> Self.Element?](taskgroup/max.md)
  Returns the maximum element in an asynchronous sequence of comparable elements.
- [func max(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](taskgroup/max(by:).md)
  Returns the maximum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [func min() async rethrows -> Self.Element?](taskgroup/min.md)
  Returns the minimum element in an asynchronous sequence of comparable elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/taskgroup/allsatisfy(_:))*