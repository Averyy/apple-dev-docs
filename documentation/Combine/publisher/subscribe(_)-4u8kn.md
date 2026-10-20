# subscribe(_:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

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
func subscribe<S>(_ subscriber: S) where S : Subscriber, Self.Failure == S.Failure, Self.Output == S.Input
```

#### Discussion

Always call this function instead of [`receive(subscriber:)`](./receive%28subscriber%29.md). Adopters of [`Publisher`](../publisher.md) must implement [`receive(subscriber:)`](./receive%28subscriber%29.md). The implementation of [`subscribe(_:)`](./subscribe%28_%29-4u8kn.md) provided by [`Publisher`](../publisher.md) calls through to [`receive(subscriber:)`](./receive%28subscriber%29.md).

## Parameters

- `subscriber`: The subscriber to attach to this publisher. After attaching, the subscriber can start to receive values.

## See Also

### Working with subscribers
- [func receive<S>(subscriber: S)](./receive%28subscriber%29.md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S) -> AnyCancellable](./subscribe%28_%29-3fk20.md)
  Attaches the specified subject to this publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher/subscribe(_:)-4u8kn)*