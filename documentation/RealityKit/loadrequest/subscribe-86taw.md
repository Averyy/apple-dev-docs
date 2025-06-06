# subscribe(_:)

**Framework**: RealityKit  
**Kind**: method

Attaches the specified subject to this publisher.

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
func subscribe<S>(_ subject: S) -> AnyCancellable where S : Subject, Self.Failure == S.Failure, Self.Output == S.Output
```

## Parameters

- `subject`: The subject to attach to this publisher.

## See Also

- [func receive<S>(subscriber: S)](loadrequest/receive(subscriber:).md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S)](loadrequest/subscribe(_:).md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S)](loadrequest/subscribe(_:)-zoee.md)
  Attaches the specified subscriber to this publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/loadrequest/subscribe(_:)-86taw)*