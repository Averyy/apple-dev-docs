# count()

**Framework**: Combine  
**Kind**: method

Publishes the number of elements received from the upstream publisher.

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
func count() -> Publishers.Count<Self>
```

#### Return Value

A publisher that consumes all elements until the upstream publisher finishes, then emits a single value with the total number of elements received.

#### Discussion

Use [`count()`](publisher/count().md) to determine the number of elements received from the upstream publisher before it completes:

```swift
let numbers = (0...10)
cancellable = numbers.publisher
    .count()
    .sink { print("\($0)") }

// Prints: "11"
```

## See Also

- [func max() -> Publishers.Comparison<Self>](publishers/replaceerror/max.md)
  Publishes the maximum value received from the upstream publisher, after it finishes.
- [func max(by: (Self.Output, Self.Output) -> Bool) -> Publishers.Comparison<Self>](publishers/replaceerror/max(by:).md)
  Publishes the maximum value received from the upstream publisher, using the provided ordering closure.
- [func tryMax(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](publishers/replaceerror/trymax(by:).md)
  Publishes the maximum value received from the upstream publisher, using the provided error-throwing closure to order the items.
- [func min() -> Publishers.Comparison<Self>](publishers/replaceerror/min.md)
  Publishes the minimum value received from the upstream publisher, after it finishes.
- [func min(by: (Self.Output, Self.Output) -> Bool) -> Publishers.Comparison<Self>](publishers/replaceerror/min(by:).md)
  Publishes the minimum value received from the upstream publisher, after it finishes.
- [func tryMin(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](publishers/replaceerror/trymin(by:).md)
  Publishes the minimum value received from the upstream publisher, using the provided error-throwing closure to order the items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/replaceerror/count())*