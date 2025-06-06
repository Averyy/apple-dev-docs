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

Always call this function instead of `Publisher/receive(subscriber:)`. Adopters of `Publisher` must implement `Publisher/receive(subscriber:)`. The implementation of `Publisher/subscribe(_:)-4u8kn` provided by `Publisher` calls through to `Publisher/receive(subscriber:)`.

## Parameters

- `subscriber`: The subscriber to attach to this publisher. After attaching, the subscriber can start to receive values.

## See Also

- [func receive<S>(subscriber: S)](loadrequest/receive(subscriber:).md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S)](loadrequest/subscribe(_:).md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S) -> AnyCancellable](loadrequest/subscribe(_:)-86taw.md)
  Attaches the specified subject to this publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/loadrequest/subscribe(_:)-zoee)*