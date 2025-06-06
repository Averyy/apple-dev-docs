# timeControlStatus

**Framework**: AVFoundation  
**Kind**: property

A value that indicates whether playback is in progress, paused indefinitely, or waiting for network conditions to improve.

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
var timeControlStatus: AVPlayer.TimeControlStatus { get }
```

## Mentions

- [Controlling the transport behavior of a player](controlling-the-transport-behavior-of-a-player.md)

#### Discussion

When the value of [`automaticallyWaitsToMinimizeStalling`](avplayer/automaticallywaitstominimizestalling.md) is [`true`](https://developer.apple.com/documentation/swift/true), the player waits until your app resumes playback.

During playback, the value of the property changes between [`AVPlayer.TimeControlStatus.playing`](avplayer/timecontrolstatus-swift.enum/playing.md) and [`AVPlayer.TimeControlStatus.waitingToPlayAtSpecifiedRate`](avplayer/timecontrolstatus-swift.enum/waitingtoplayatspecifiedrate.md) depending on whether the player has sufficient media data to continue playback.

This property is key-value observable.

## See Also

- [var automaticallyWaitsToMinimizeStalling: Bool](avplayer/automaticallywaitstominimizestalling.md)
  A Boolean value that indicates whether the player should automatically delay playback in order to minimize stalling.
- [var reasonForWaitingToPlay: AVPlayer.WaitingReason?](avplayer/reasonforwaitingtoplay.md)
  The reason the player is currently waiting for playback to begin or resume.
- [AVPlayer.WaitingReason](avplayer/waitingreason.md)
  The reasons a player is waiting to begin or resume playback.
- [AVPlayer.TimeControlStatus](avplayer/timecontrolstatus-swift.enum.md)
  Constants that indicate the state of playback control.
- [func playImmediately(atRate: Float)](avplayer/playimmediately(atrate:).md)
  Plays the available media data immediately, at the specified rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/timecontrolstatus-swift.property)*