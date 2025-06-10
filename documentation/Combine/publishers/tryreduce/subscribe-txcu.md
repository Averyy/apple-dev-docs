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

Always call this function instead of [`receive(subscriber:)`](publisher/receive(subscriber:).md). Adopters of [`Publisher`](publisher.md) must implement [`receive(subscriber:)`](publisher/receive(subscriber:).md). The implementation of [`subscribe(_:)`](publisher/subscribe(_:)-4u8kn.md) provided by [`Publisher`](publisher.md) calls through to [`receive(subscriber:)`](publisher/receive(subscriber:).md).

## Parameters

- `subscriber`: The subscriber to attach to this publisher. After attaching, the subscriber can start to receive values.

## See Also

- [func receive<S>(subscriber: S)](publishers/tryreduce/receive(subscriber:).md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S) -> AnyCancellable](publishers/tryreduce/subscribe(_:)-9o35l.md)
  Attaches the specified subject to this publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/tryreduce/subscribe(_:)-txcu)*