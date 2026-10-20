# MPNowPlayingSessionDelegate

**Framework**: Media Player  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol MPNowPlayingSessionDelegate <NSObject>
```

## Topics

### Responding to state changes
- [func nowPlayingSessionDidChangeActive(MPNowPlayingSession)](./mpnowplayingsessiondelegate/nowplayingsessiondidchangeactive%28_%29.md)
  Tells the delegate that the session changed its active status.
- [func nowPlayingSessionDidChangeCanBecomeActive(MPNowPlayingSession)](./mpnowplayingsessiondelegate/nowplayingsessiondidchangecanbecomeactive%28_%29.md)
  Tells the delegate that the session is eligible to become active.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Accessing the delegate object
- [var delegate: (any MPNowPlayingSessionDelegate)?](./mpnowplayingsession/delegate.md)
  The Now Playing session’s delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayingsessiondelegate)*