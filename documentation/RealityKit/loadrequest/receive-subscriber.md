# receive(subscriber:)

**Framework**: RealityKit  
**Kind**: method

Attaches the specified subscriber to this publisher.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func receive<S>(subscriber: S) where Output == S.Input, S : Subscriber, S.Failure == any Error
```

#### Discussion

Implementations of `Publisher` must implement this method.

The provided implementation of `Publisher/subscribe(_:)-4u8kn`calls this method.

## Parameters

- `subscriber`: The subscriber to attach to this  , after which it can receive values.

## See Also

- [func subscribe<S>(S)](loadrequest/subscribe(_:).md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S)](loadrequest/subscribe(_:)-zoee.md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S) -> AnyCancellable](loadrequest/subscribe(_:)-86taw.md)
  Attaches the specified subject to this publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/loadrequest/receive(subscriber:))*