# AVPlayer.TimeControlStatus

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVPlayerTimeControlStatus : NSInteger;
```

## Topics

### Status values
- [AVPlayer.TimeControlStatus.paused](./timecontrolstatus-swift.enum/paused.md)
  A state that indicates the player paused playback indefinitely.
- [AVPlayer.TimeControlStatus.waitingToPlayAtSpecifiedRate](./timecontrolstatus-swift.enum/waitingtoplayatspecifiedrate.md)
  A state that indicates that the player is waiting for network conditions to improve before it can start or resume playback.
- [AVPlayer.TimeControlStatus.playing](./timecontrolstatus-swift.enum/playing.md)
  A state that indicates that the player is currently playing media.
### Initializers
- [init?(rawValue: Int)](./timecontrolstatus-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [func playImmediately(atRate: Float)](./playimmediately%28atrate%29.md)
  Plays the available media data immediately, at the specified rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/timecontrolstatus-swift.enum)*