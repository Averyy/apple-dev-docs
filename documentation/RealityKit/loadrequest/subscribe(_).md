# subscribe(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Attaches the specified subscriber to this publisher.

**Availability**:
- iOS 13.0+ - Deprecated in 18.0
- iPadOS 13.0+ - Deprecated in 18.0
- Mac Catalyst 13.0+ - Deprecated in 18.0
- macOS 10.15+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
func subscribe<S>(_ subscriber: S) where Output == S.Input, S : Subscriber, S.Failure == any Error
```

## Discussion

Always call this function instead of `Publisher/receive(subscriber:)`. Adopters of `Publisher` must implement `Publisher/receive(subscriber:)`. The implementation of `Publisher/subscribe(_:)-4u8kn` provided by `Publisher` calls through to `Publisher/receive(subscriber:)`.

## Parameters

- `subscriber`: The subscriber to attach to this publisher. After attaching, the subscriber can start to receive values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/loadrequest/subscribe(_:))*