# max()

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

Publishes the maximum value received from the upstream publisher, after it finishes.

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
func max() -> Publishers.Comparison<Self>
```

Available when `Output` conforms to `Comparable`.

## Return Value

A publisher that publishes the maximum value received from the upstream publisher, after the upstream publisher finishes.

## Discussion

Use [`max()`](./max%28%29.md) to determine the maximum value in the stream of elements from an upstream publisher.

In the example below, the [`max()`](./max%28%29.md) operator emits a value when the publisher finishes, that value is the maximum of the values received from upstream, which is `10`.

```swift
let numbers = [0, 10, 5]
cancellable = numbers.publisher
    .max()
    .sink { print("\($0)") }

// Prints: "10"
```

After this publisher receives a request for more than 0 items, it requests unlimited items from its upstream publisher.

## See Also

### Applying mathematical operations on elements
- [func count() -> Publishers.Count<Self>](./count%28%29.md)
  Publishes the number of elements received from the upstream publisher.
- [func max(by: (Self.Output, Self.Output) -> Bool) -> Publishers.Comparison<Self>](./max%28by%29.md)
  Publishes the maximum value received from the upstream publisher, using the provided ordering closure.
- [func tryMax(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](./trymax%28by%29.md)
  Publishes the maximum value received from the upstream publisher, using the provided error-throwing closure to order the items.
- [func min() -> Publishers.Comparison<Self>](./min%28%29.md)
  Publishes the minimum value received from the upstream publisher, after it finishes.
- [func min(by: (Self.Output, Self.Output) -> Bool) -> Publishers.Comparison<Self>](./min%28by%29.md)
  Publishes the minimum value received from the upstream publisher, after it finishes.
- [func tryMin(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](./trymin%28by%29.md)
  Publishes the minimum value received from the upstream publisher, using the provided error-throwing closure to order the items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher/max())*