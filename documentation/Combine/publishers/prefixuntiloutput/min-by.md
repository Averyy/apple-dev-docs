# min(by:)

**Framework**: Combine  
**Kind**: method

Publishes the minimum value received from the upstream publisher, after it finishes.

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
func min(by areInIncreasingOrder: @escaping (Self.Output, Self.Output) -> Bool) -> Publishers.Comparison<Self>
```

#### Return Value

A publisher that publishes the minimum value received from the upstream publisher, after the upstream publisher finishes.

#### Discussion

Use [`min(by:)`](publisher/min(by:).md) to determine the minimum value in the stream of elements from an upstream publisher using a comparison operation you specify.

This operator is useful when the value received from the upstream publisher isn’t [`Comparable`](https://developer.apple.com/documentation/Swift/Comparable).

In the example below an array publishes enumeration elements representing playing card ranks. The [`min(by:)`](publisher/min(by:).md) operator compares the current and next elements using the `rawValue` property of each enumeration value in the user supplied closure and prints the minimum value found after publishing all of the elements.

```swift
enum Rank: Int {
    case ace = 1, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king
}

let cards: [Rank] = [.five, .queen, .ace, .eight, .king]
cancellable = cards.publisher
    .min {
        return  $0.rawValue < $1.rawValue
    }
    .sink { print("\($0)") }

// Prints: "ace"
```

After this publisher receives a request for more than 0 items, it requests unlimited items from its upstream publisher.

## Parameters

- `areInIncreasingOrder`: A closure that receives two elements and returns true if they’re in increasing order.

## See Also

- [func count() -> Publishers.Count<Self>](publishers/prefixuntiloutput/count.md)
  Publishes the number of elements received from the upstream publisher.
- [func max() -> Publishers.Comparison<Self>](publishers/prefixuntiloutput/max.md)
  Publishes the maximum value received from the upstream publisher, after it finishes.
- [func max(by: (Self.Output, Self.Output) -> Bool) -> Publishers.Comparison<Self>](publishers/prefixuntiloutput/max(by:).md)
  Publishes the maximum value received from the upstream publisher, using the provided ordering closure.
- [func tryMax(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](publishers/prefixuntiloutput/trymax(by:).md)
  Publishes the maximum value received from the upstream publisher, using the provided error-throwing closure to order the items.
- [func min() -> Publishers.Comparison<Self>](publishers/prefixuntiloutput/min.md)
  Publishes the minimum value received from the upstream publisher, after it finishes.
- [func tryMin(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](publishers/prefixuntiloutput/trymin(by:).md)
  Publishes the minimum value received from the upstream publisher, using the provided error-throwing closure to order the items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/prefixuntiloutput/min(by:))*