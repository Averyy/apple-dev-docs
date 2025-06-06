# subscribe(_:)

**Framework**: Combine  
**Kind**: method

Attaches the specified subject to this publisher.

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
func subscribe<S>(_ subject: S) -> AnyCancellable where S : Subject, Self.Failure == S.Failure, Self.Output == S.Output
```

## Mentions

- [Controlling Publishing with Connectable Publishers](controlling-publishing-with-connectable-publishers.md)

## Parameters

- `subject`: The subject to attach to this publisher.

## See Also

- [func receive<S>(subscriber: S)](publisher/receive(subscriber:).md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S)](publisher/subscribe(_:)-4u8kn.md)
  Attaches the specified subscriber to this publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher/subscribe(_:)-3fk20)*