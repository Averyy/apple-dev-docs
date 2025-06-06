# MPNowPlayingSessionDelegate

**Framework**: Media Player  
**Kind**: protocol

A protocol that defines the delegate interface for a Now Playing session.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol MPNowPlayingSessionDelegate : NSObjectProtocol
```

## Topics

### Responding to state changes
- [func nowPlayingSessionDidChangeActive(MPNowPlayingSession)](mpnowplayingsessiondelegate/nowplayingsessiondidchangeactive(_:).md)
  Tells the delegate that the session changed its active status.
- [func nowPlayingSessionDidChangeCanBecomeActive(MPNowPlayingSession)](mpnowplayingsessiondelegate/nowplayingsessiondidchangecanbecomeactive(_:).md)
  Tells the delegate that the session is eligible to become active.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any MPNowPlayingSessionDelegate)?](mpnowplayingsession/delegate.md)
  The Now Playing session’s delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayingsessiondelegate)*