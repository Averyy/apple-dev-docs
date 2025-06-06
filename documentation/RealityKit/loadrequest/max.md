# max()

**Framework**: RealityKit  
**Kind**: method

Publishes the maximum value received from the upstream publisher, after it finishes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
func max() -> Publishers.Comparison<Self>
```

#### Return Value

A publisher that publishes the maximum value received from the upstream publisher, after the upstream publisher finishes.

#### Discussion

Use `Publisher/max()` to determine the maximum value in the stream of elements from an upstream publisher.

In the example below, the `Publisher/max()` operator emits a value when the publisher finishes, that value is the maximum of the values received from upstream, which is `10`.

```None
let numbers = [0, 10, 5]
cancellable = numbers.publisher
    .max()
    .sink { print("\($0)") }

// Prints: "10"
```

After this publisher receives a request for more than 0 items, it requests unlimited items from its upstream publisher.

## See Also

- [func count() -> Publishers.Count<Self>](loadrequest/count.md)
  Publishes the number of elements received from the upstream publisher.
- [func max(by: (Self.Output, Self.Output) -> Bool) -> Publishers.Comparison<Self>](loadrequest/max(by:).md)
  Publishes the maximum value received from the upstream publisher, using the provided ordering closure.
- [func tryMax(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](loadrequest/trymax(by:).md)
  Publishes the maximum value received from the upstream publisher, using the provided error-throwing closure to order the items.
- [func min() -> Publishers.Comparison<Self>](loadrequest/min.md)
  Publishes the minimum value received from the upstream publisher, after it finishes.
- [func min(by: (Self.Output, Self.Output) -> Bool) -> Publishers.Comparison<Self>](loadrequest/min(by:).md)
  Publishes the minimum value received from the upstream publisher, after it finishes.
- [func tryMin(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](loadrequest/trymin(by:).md)
  Publishes the minimum value received from the upstream publisher, using the provided error-throwing closure to order the items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/loadrequest/max())*