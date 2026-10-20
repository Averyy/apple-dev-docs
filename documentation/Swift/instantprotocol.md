# InstantProtocol

**Framework**: Swift  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol InstantProtocol<Duration> : Comparable, Hashable, Sendable
```

## Topics

### Associated Types
- [associatedtype Duration : DurationProtocol](./instantprotocol/duration.md)
### Instance Methods
- [func advanced(by: Self.Duration) -> Self](./instantprotocol/advanced%28by%29.md)
- [func duration(to: Self) -> Self.Duration](./instantprotocol/duration%28to%29.md)

## Relationships

### Inherits From
- [Comparable](./comparable.md)
- [Equatable](./equatable.md)
- [Hashable](./hashable.md)
- [Sendable](./sendable.md)
- [SendableMetatype](./sendablemetatype.md)
### Conforming Types
- [ContinuousClock.Instant](./continuousclock/instant.md)
- [SuspendingClock.Instant](./suspendingclock/instant.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/instantprotocol)*