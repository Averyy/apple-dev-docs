# AVPlayer.TimeControlStatus

**Framework**: AVFoundation  
**Kind**: enum

Constants that indicate the state of playback control.

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
enum TimeControlStatus
```

## Topics

### Status Values
- [AVPlayer.TimeControlStatus.paused](avplayer/timecontrolstatus-swift.enum/paused.md)
  A state that indicates the player paused playback indefinitely.
- [AVPlayer.TimeControlStatus.waitingToPlayAtSpecifiedRate](avplayer/timecontrolstatus-swift.enum/waitingtoplayatspecifiedrate.md)
  A state that indicates that the player is waiting for network conditions to improve before it can start or resume playback.
- [AVPlayer.TimeControlStatus.playing](avplayer/timecontrolstatus-swift.enum/playing.md)
  A state that indicates that the player is currently playing media.
### Initializers
- [init?(rawValue: Int)](avplayer/timecontrolstatus-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var automaticallyWaitsToMinimizeStalling: Bool](avplayer/automaticallywaitstominimizestalling.md)
  A Boolean value that indicates whether the player should automatically delay playback in order to minimize stalling.
- [var reasonForWaitingToPlay: AVPlayer.WaitingReason?](avplayer/reasonforwaitingtoplay.md)
  The reason the player is currently waiting for playback to begin or resume.
- [AVPlayer.WaitingReason](avplayer/waitingreason.md)
  The reasons a player is waiting to begin or resume playback.
- [var timeControlStatus: AVPlayer.TimeControlStatus](avplayer/timecontrolstatus-swift.property.md)
  A value that indicates whether playback is in progress, paused indefinitely, or waiting for network conditions to improve.
- [func playImmediately(atRate: Float)](avplayer/playimmediately(atrate:).md)
  Plays the available media data immediately, at the specified rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/timecontrolstatus-swift.enum)*