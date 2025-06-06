# receive(subscriber:)

**Framework**: Combine  
**Kind**: method

Attaches the specified subscriber to this publisher.

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
func receive<S>(subscriber: S) where Value == S.Input, S : Subscriber, S.Failure == Never
```

#### Discussion

Implementations of [`Published.Publisher`](published/publisher.md) must implement this method.

The provided implementation of [`subscribe(_:)`](publisher/subscribe(_:)-4u8kn.md)calls this method.

## Parameters

- `subscriber`: The subscriber to attach to this  , after which it can receive values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/published/publisher/receive(subscriber:))*