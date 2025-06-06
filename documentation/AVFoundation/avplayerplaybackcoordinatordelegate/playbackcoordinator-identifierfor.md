# playbackCoordinator(_:identifierFor:)

**Framework**: AVFoundation  
**Kind**: method

Returns an identifier for a player item.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
optional func playbackCoordinator(_ coordinator: AVPlayerPlaybackCoordinator, identifierFor playerItem: AVPlayerItem) -> String
```

#### Return Value

An identifier string.

#### Discussion

A coordinator calls this method to identify the items that its player object plays.

Implement this method to enable the coordinator to establish the identity of items that have different URLs. For example, two participants may play the same item, but one plays the item from a remote host and the other from a local version on a device.

If you don’t implement this method, the coordinator derives an identifier from the item’s asset.

## Parameters

- `coordinator`: The object coordinating playback.
- `playerItem`: The player item to return an identifier for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerplaybackcoordinatordelegate/playbackcoordinator(_:identifierfor:))*