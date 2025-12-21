# AVPlayerPlaybackCoordinatorDelegate

**Framework**: AVFoundation  
**Kind**: protocol

A protocol that defines the methods to implement to participate in playback coordination.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
protocol AVPlayerPlaybackCoordinatorDelegate : NSObjectProtocol, Sendable
```

## Topics

### Identifying items
- [func playbackCoordinator(AVPlayerPlaybackCoordinator, identifierFor: AVPlayerItem) -> String](avplayerplaybackcoordinatordelegate/playbackcoordinator(_:identifierfor:).md)
  Returns an identifier for a player item.
### Retrieving interstitial time ranges
- [func playbackCoordinator(AVPlayerPlaybackCoordinator, interstitialTimeRangesFor: AVPlayerItem) -> [NSValue]](avplayerplaybackcoordinatordelegate/playbackcoordinator(_:interstitialtimerangesfor:).md)
  Asks the delegate for time ranges in a player item that don’t correspond to the primary content.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var delegate: (any AVPlayerPlaybackCoordinatorDelegate)?](avplayerplaybackcoordinator/delegate.md)
  A delegate object for the playback coordinator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerplaybackcoordinatordelegate)*