# min()

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
func min() -> Publishers.Comparison<Self>
```

#### Return Value

A publisher that publishes the minimum value received from the upstream publisher, after the upstream publisher finishes.

#### Discussion

Use [`min(by:)`](publisher/min(by:).md) to find the minimum value in a stream of elements from an upstream publisher.

In the example below, the [`min(by:)`](publisher/min(by:).md) operator emits a value when the publisher finishes, that value is the minimum of the values received from upstream, which is `-1`.

```swift
let numbers = [-1, 0, 10, 5]
numbers.publisher
    .min()
    .sink { print("\($0)") }

// Prints: "-1"
```

After this publisher receives a request for more than 0 items, it requests unlimited items from its upstream publisher.

## See Also

- [func count() -> Publishers.Count<Self>](publishers/merge3/count.md)
  Publishes the number of elements received from the upstream publisher.
- [func max() -> Publishers.Comparison<Self>](publishers/merge3/max.md)
  Publishes the maximum value received from the upstream publisher, after it finishes.
- [func max(by: (Self.Output, Self.Output) -> Bool) -> Publishers.Comparison<Self>](publishers/merge3/max(by:).md)
  Publishes the maximum value received from the upstream publisher, using the provided ordering closure.
- [func tryMax(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](publishers/merge3/trymax(by:).md)
  Publishes the maximum value received from the upstream publisher, using the provided error-throwing closure to order the items.
- [func min(by: (Self.Output, Self.Output) -> Bool) -> Publishers.Comparison<Self>](publishers/merge3/min(by:).md)
  Publishes the minimum value received from the upstream publisher, after it finishes.
- [func tryMin(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](publishers/merge3/trymin(by:).md)
  Publishes the minimum value received from the upstream publisher, using the provided error-throwing closure to order the items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge3/min())*