# subscribe(_:)

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
func subscribe<S>(_ subscriber: S) where S : Subscriber, Self.Failure == S.Failure, Self.Output == S.Input
```

#### Discussion

Always call this function instead of [`receive(subscriber:)`](published/publisher/receive(subscriber:).md). Adopters of [`Published.Publisher`](published/publisher.md) must implement [`receive(subscriber:)`](published/publisher/receive(subscriber:).md). The implementation of [`subscribe(_:)`](publisher/subscribe(_:)-4u8kn.md) provided by [`Published.Publisher`](published/publisher.md) calls through to [`receive(subscriber:)`](published/publisher/receive(subscriber:).md).

## Parameters

- `subscriber`: The subscriber to attach to this publisher. After attaching, the subscriber can start to receive values.

## See Also

- [func subscribe<S>(S) -> AnyCancellable](published/publisher/subscribe(_:)-3k7pn.md)
  Attaches the specified subject to this publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/published/publisher/subscribe(_:)-9smkf)*