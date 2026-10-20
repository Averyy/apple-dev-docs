# AVPlayer.WaitingReason

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

The reasons a player is waiting to begin or resume playback.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct WaitingReason
```

```c
typedef NSString * AVPlayerWaitingReason;
```

## Topics

### Player waiting reasons
- [static let evaluatingBufferingRate: AVPlayer.WaitingReason](./waitingreason/evaluatingbufferingrate.md)
  The player is waiting because it’s monitoring the buffer’s fill rate to determine whether playback is likely to complete without interruptions.
- [static let noItemToPlay: AVPlayer.WaitingReason](./waitingreason/noitemtoplay.md)
  The player is waiting because there’s no item to play.
- [static let toMinimizeStalls: AVPlayer.WaitingReason](./waitingreason/tominimizestalls.md)
  The player is waiting for appropriate playback conditions before starting playback.
- [static let interstitialEvent: AVPlayer.WaitingReason](./waitingreason/interstitialevent.md)
  The player is waiting for an interstitial event to complete.
- [static let waitingForCoordinatedPlayback: AVPlayer.WaitingReason](./waitingreason/waitingforcoordinatedplayback.md)
  The player is waiting for another participant in a coordinated playback session.
### Initializers
- [init(rawValue: String)](./waitingreason/init%28rawvalue%29.md)
  Creates a waiting reason with a string value.

## Relationships

### Conforms To
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
- [var timeControlStatus: AVPlayer.TimeControlStatus](./timecontrolstatus-swift.property.md)
  A value that indicates whether playback is in progress, paused indefinitely, or waiting for network conditions to improve.
- [AVPlayer.TimeControlStatus](./timecontrolstatus-swift.enum.md)
  Constants that indicate the state of playback control.
- [func playImmediately(atRate: Float)](./playimmediately%28atrate%29.md)
  Plays the available media data immediately, at the specified rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/waitingreason)*