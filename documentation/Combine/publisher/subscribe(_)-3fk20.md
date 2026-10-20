# subscribe(_:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

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

- [Controlling Publishing with Connectable Publishers](../controlling-publishing-with-connectable-publishers.md)

## Parameters

- `subject`: The subject to attach to this publisher.

## See Also

### Working with subscribers
- [func receive<S>(subscriber: S)](./receive%28subscriber%29.md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S)](./subscribe%28_%29-4u8kn.md)
  Attaches the specified subscriber to this publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher/subscribe(_:)-3fk20)*