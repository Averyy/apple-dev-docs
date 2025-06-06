# playImmediately(atRate:)

**Framework**: AVFoundation  
**Kind**: method

Plays the available media data immediately, at the specified rate.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
nonisolated
func playImmediately(atRate rate: Float)
```

#### Discussion

This method plays the available media data at the specified `rate` regardless of whether there is sufficient media buffered to ensure smooth playback. If media data exists in the playback buffer, calling this method changes the player’s playback rate to the specified `rate` and its [`timeControlStatus`](avplayer/timecontrolstatus-swift.property.md) to a value of [`AVPlayer.TimeControlStatus.playing`](avplayer/timecontrolstatus-swift.enum/playing.md). If the player has insufficient media data buffered to begin playback, the player will behave as if it has encountered a stall during playback, except that no [`playbackStalledNotification`](avplayeritem/playbackstallednotification.md) will be posted.

## Parameters

- `rate`: The specified playback rate.

## See Also

- [var automaticallyWaitsToMinimizeStalling: Bool](avplayer/automaticallywaitstominimizestalling.md)
  A Boolean value that indicates whether the player should automatically delay playback in order to minimize stalling.
- [var reasonForWaitingToPlay: AVPlayer.WaitingReason?](avplayer/reasonforwaitingtoplay.md)
  The reason the player is currently waiting for playback to begin or resume.
- [AVPlayer.WaitingReason](avplayer/waitingreason.md)
  The reasons a player is waiting to begin or resume playback.
- [var timeControlStatus: AVPlayer.TimeControlStatus](avplayer/timecontrolstatus-swift.property.md)
  A value that indicates whether playback is in progress, paused indefinitely, or waiting for network conditions to improve.
- [AVPlayer.TimeControlStatus](avplayer/timecontrolstatus-swift.enum.md)
  Constants that indicate the state of playback control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/playimmediately(atrate:))*