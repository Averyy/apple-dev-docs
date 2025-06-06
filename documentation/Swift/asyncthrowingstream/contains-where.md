# contains(where:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.

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
func contains(where predicate: (Self.Element) async throws -> Bool) async rethrows -> Bool
```

#### Return Value

`true` if the sequence contains an element that satisfies predicate; otherwise, `false`.

#### Discussion

You can use the predicate to check for an element of a type that doesn’t conform to the `Equatable` protocol, or to find an element that satisfies a general condition.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `contains(where:)` method checks to see whether the sequence produces a value divisible by `3`:

```swift
let containsDivisibleByThree = await Counter(howHigh: 10)
    .contains { $0 % 3 == 0 }
print(containsDivisibleByThree)
// Prints "true"
```

The predicate executes each time the asynchronous sequence produces an element, until either the predicate finds a match or the sequence ends.

## Parameters

- `predicate`: A closure that takes an element of the asynchronous   sequence as its argument and returns a Boolean value that indicates   whether the passed element represents a match.

## See Also

- [func contains(Self.Element) async rethrows -> Bool](asyncthrowingstream/contains(_:).md)
  Returns a Boolean value that indicates whether the asynchronous sequence contains the given element.
- [func allSatisfy((Self.Element) async throws -> Bool) async rethrows -> Bool](asyncthrowingstream/allsatisfy(_:).md)
  Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.
- [func first(where: (Self.Element) async throws -> Bool) async rethrows -> Self.Element?](asyncthrowingstream/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func min() async rethrows -> Self.Element?](asyncthrowingstream/min.md)
  Returns the minimum element in an asynchronous sequence of comparable elements.
- [func min(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](asyncthrowingstream/min(by:).md)
  Returns the minimum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [func max() async rethrows -> Self.Element?](asyncthrowingstream/max.md)
  Returns the maximum element in an asynchronous sequence of comparable elements.
- [func max(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](asyncthrowingstream/max(by:).md)
  Returns the maximum element in the asynchronous sequence, using the given predicate as the comparison between elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingstream/contains(where:))*