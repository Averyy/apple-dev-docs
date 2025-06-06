# receive(subscriber:)

**Framework**: RealityKit  
**Kind**: method

Attaches the specified subscriber to this publisher.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
func receive<S>(subscriber: S) where E == S.Input, S : Subscriber, S.Failure == Never
```

#### Discussion

Implementations of [`Scene.Publisher`](scene/publisher.md) must implement this method.

The provided implementation of `Publisher/subscribe(_:)-4u8kn`calls this method.

## Parameters

- `subscriber`: The subscriber to attach to this  , after which it can receive values.

## See Also

- [func subscribe<S>(S)](scene/publisher/subscribe(_:)-13yio.md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S) -> AnyCancellable](scene/publisher/subscribe(_:)-60uvt.md)
  Attaches the specified subject to this publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/publisher/receive(subscriber:))*