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
func receive<S>(subscriber: S) where S : Subscriber, P.Output == S.Input, Upstream.Failure == S.Failure
```

#### Discussion

Implementations of [`Publisher`](publisher.md) must implement this method.

The provided implementation of [`subscribe(_:)`](publisher/subscribe(_:)-4u8kn.md)calls this method.

## Parameters

- `subscriber`: The subscriber to attach to this  , after which it can receive values.

## See Also

- [func subscribe<S>(S)](publishers/switchtolatest/subscribe(_:)-7dkfw.md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S) -> AnyCancellable](publishers/switchtolatest/subscribe(_:)-91fpq.md)
  Attaches the specified subject to this publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/switchtolatest/receive(subscriber:))*