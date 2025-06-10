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

## Parameters

- `subject`: The subject to attach to this publisher.

## See Also

- [func receive<S>(subscriber: S)](publishers/share/receive(subscriber:).md)
  Attaches the specified subscriber to this publisher.
- [func subscribe<S>(S)](publishers/share/subscribe(_:)-85csy.md)
  Attaches the specified subscriber to this publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/share/subscribe(_:)-8qqf6)*