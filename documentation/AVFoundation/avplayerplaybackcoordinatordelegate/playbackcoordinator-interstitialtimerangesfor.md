# playbackCoordinator(_:interstitialTimeRangesFor:)

**Framework**: AVFoundation  
**Kind**: method

Asks the delegate for time ranges in a player item that don’t correspond to the primary content.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
optional func playbackCoordinator(_ coordinator: AVPlayerPlaybackCoordinator, interstitialTimeRangesFor playerItem: AVPlayerItem) -> [NSValue]
```

#### Return Value

An array of [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) objects that contain the interstitial time ranges.

#### Discussion

Implementing this method enables the coordinator to synchronize playback between participants that have different interstitials stitched into the primary content timeline.

If you don’t implement this method, the coordinator assumes that the entire item corresponds to the primary content.

## Parameters

- `coordinator`: The object coordinating playback.
- `playerItem`: The player item for which to retrieve interstitial time ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerplaybackcoordinatordelegate/playbackcoordinator(_:interstitialtimerangesfor:))*