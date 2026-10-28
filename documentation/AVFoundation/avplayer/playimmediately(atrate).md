# playImmediately(atRate:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) playImmediatelyAtRate:(float) rate;
```

## Discussion

This method plays the available media data at the specified `rate` regardless of whether there is sufficient media buffered to ensure smooth playback. If media data exists in the playback buffer, calling this method changes the player’s playback rate to the specified `rate` and its [`timeControlStatus`](./timecontrolstatus-swift.property.md) to a value of [`AVPlayer.TimeControlStatus.playing`](./timecontrolstatus-swift.enum/playing.md). If the player has insufficient media data buffered to begin playback, the player will behave as if it has encountered a stall during playback, except that no [`playbackStalledNotification`](../avplayeritem/playbackstallednotification.md) will be posted.

## Parameters

- `rate`: The specified playback rate.

## See Also

### Configuring waiting behavior
- [var automaticallyWaitsToMinimizeStalling: Bool](./automaticallywaitstominimizestalling.md)
  A Boolean value that indicates whether the player should automatically delay playback in order to minimize stalling.
- [var reasonForWaitingToPlay: AVPlayer.WaitingReason?](./reasonforwaitingtoplay.md)
  The reason the player is currently waiting for playback to begin or resume.
- [AVPlayer.WaitingReason](./waitingreason.md)
  The reasons a player is waiting to begin or resume playback.
- [var timeControlStatus: AVPlayer.TimeControlStatus](./timecontrolstatus-swift.property.md)
  A value that indicates whether playback is in progress, paused indefinitely, or waiting for network conditions to improve.
- [AVPlayer.TimeControlStatus](./timecontrolstatus-swift.enum.md)
  Constants that indicate the state of playback control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/playimmediately(atrate:))*