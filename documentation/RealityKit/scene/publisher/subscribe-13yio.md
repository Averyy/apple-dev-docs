# subscribe(_:)

**Framework**: RealityKit  
**Kind**: method

Attaches the specified subscriber to this publisher.

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
func subscribe<S>(_ subscriber: S) where S : Subscriber, Self.Failure == S.Failure, Self.Output == S.Input
```

#### Discussion

Always call this function instead of [`receive(subscriber:)`](scene/publisher/receive(subscriber:).md). Adopters of [`Scene.Publisher`](scene/publisher.md) must implement [`receive(subscriber:)`](scene/publisher/receive(subscriber:).md). The implementation of `Publisher/subscribe(_:)-4u8kn` provided by [`Scene.Publisher`](scene/publisher.md) calls through to [`receive(subscriber:)`](scene/publisher/receive(subscriber:).md).

## Parameters

- `subscriber`: The subscriber to attach to this publisher. After attaching, the subscriber can start to receive values.

## See Also

- [func receive<S>(subscriber: S)](scene/publisher/receive(subscriber:).md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S) -> AnyCancellable](scene/publisher/subscribe(_:)-60uvt.md)
  Attaches the specified subject to this publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/publisher/subscribe(_:)-13yio)*