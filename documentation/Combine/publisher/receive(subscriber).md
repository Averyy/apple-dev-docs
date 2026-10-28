# receive(subscriber:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

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
func receive<S>(subscriber: S) where S : Subscriber, Self.Failure == S.Failure, Self.Output == S.Input
```

## Discussion

Implementations of [`Publisher`](../publisher.md) must implement this method.

The provided implementation of [`subscribe(_:)`](./subscribe%28_%29-4u8kn.md)calls this method.

## Parameters

- `subscriber`: The subscriber to attach to this [`Publisher`](../publisher.md), after which it can receive values.

## See Also

### Working with subscribers
- [func subscribe<S>(S)](./subscribe%28_%29-4u8kn.md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S) -> AnyCancellable](./subscribe%28_%29-3fk20.md)
  Attaches the specified subject to this publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher/receive(subscriber:))*