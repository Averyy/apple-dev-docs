# max()

**Framework**: Combine  
**Kind**: method

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

#### Return Value

A publisher that publishes the maximum value received from the upstream publisher, after the upstream publisher finishes.

#### Discussion

Use [`max()`](publisher/max().md) to determine the maximum value in the stream of elements from an upstream publisher.

In the example below, the [`max()`](publisher/max().md) operator emits a value when the publisher finishes, that value is the maximum of the values received from upstream, which is `10`.

```swift
let numbers = [0, 10, 5]
cancellable = numbers.publisher
    .max()
    .sink { print("\($0)") }

// Prints: "10"
```

After this publisher receives a request for more than 0 items, it requests unlimited items from its upstream publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/max()-49bgv)*