# max(by:)

**Framework**: Combine  
**Kind**: method

Publishes the maximum value received from the upstream publisher, using the provided ordering closure.

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
func max(by areInIncreasingOrder: @escaping (Self.Output, Self.Output) -> Bool) -> Publishers.Comparison<Self>
```

#### Return Value

A publisher that publishes the maximum value received from the upstream publisher, after the upstream publisher finishes.

#### Discussion

Use [`max(by:)`](publisher/max(by:).md) to determine the maximum value of elements received from the upstream publisher based on an ordering closure you specify.

In the example below, an array publishes enumeration elements representing playing card ranks. The [`max(by:)`](publisher/max(by:).md) operator compares the current and next elements using the `rawValue` property of each enumeration value in the user supplied closure and prints the maximum value found after publishing all of the elements.

```swift
enum Rank: Int {
    case ace = 1, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king
}

let cards: [Rank] = [.five, .queen, .ace, .eight, .jack]
cancellable = cards.publisher
    .max {
        return  $0.rawValue > $1.rawValue
    }
    .sink { print("\($0)") }

// Prints: "queen"
```

After this publisher receives a request for more than 0 items, it requests unlimited items from its upstream publisher.

## Parameters

- `areInIncreasingOrder`: A closure that receives two elements and returns true if they’re in increasing order.

## See Also

- [func count() -> Publishers.Count<Self>](publishers/compactmap/count.md)
  Publishes the number of elements received from the upstream publisher.
- [func max() -> Publishers.Comparison<Self>](publishers/compactmap/max.md)
  Publishes the maximum value received from the upstream publisher, after it finishes.
- [func tryMax(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](publishers/compactmap/trymax(by:).md)
  Publishes the maximum value received from the upstream publisher, using the provided error-throwing closure to order the items.
- [func min() -> Publishers.Comparison<Self>](publishers/compactmap/min.md)
  Publishes the minimum value received from the upstream publisher, after it finishes.
- [func min(by: (Self.Output, Self.Output) -> Bool) -> Publishers.Comparison<Self>](publishers/compactmap/min(by:).md)
  Publishes the minimum value received from the upstream publisher, after it finishes.
- [func tryMin(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](publishers/compactmap/trymin(by:).md)
  Publishes the minimum value received from the upstream publisher, using the provided error-throwing closure to order the items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/compactmap/max(by:))*