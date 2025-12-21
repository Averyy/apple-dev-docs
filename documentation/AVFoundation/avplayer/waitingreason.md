# AVPlayer.WaitingReason

**Framework**: AVFoundation  
**Kind**: struct

The reasons a player is waiting to begin or resume playback.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct WaitingReason
```

## Topics

### Player waiting reasons
- [static let evaluatingBufferingRate: AVPlayer.WaitingReason](avplayer/waitingreason/evaluatingbufferingrate.md)
  The player is waiting because it’s monitoring the buffer’s fill rate to determine whether playback is likely to complete without interruptions.
- [static let noItemToPlay: AVPlayer.WaitingReason](avplayer/waitingreason/noitemtoplay.md)
  The player is waiting because there’s no item to play.
- [static let toMinimizeStalls: AVPlayer.WaitingReason](avplayer/waitingreason/tominimizestalls.md)
  The player is waiting for appropriate playback conditions before starting playback.
- [static let interstitialEvent: AVPlayer.WaitingReason](avplayer/waitingreason/interstitialevent.md)
  The player is waiting for an interstitial event to complete.
- [static let waitingForCoordinatedPlayback: AVPlayer.WaitingReason](avplayer/waitingreason/waitingforcoordinatedplayback.md)
  The player is waiting for another participant in a coordinated playback session.
### Initializers
- [init(rawValue: String)](avplayer/waitingreason/init(rawvalue:).md)
  Creates a waiting reason with a string value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var automaticallyWaitsToMinimizeStalling: Bool](avplayer/automaticallywaitstominimizestalling.md)
  A Boolean value that indicates whether the player should automatically delay playback in order to minimize stalling.
- [var reasonForWaitingToPlay: AVPlayer.WaitingReason?](avplayer/reasonforwaitingtoplay.md)
  The reason the player is currently waiting for playback to begin or resume.
- [var timeControlStatus: AVPlayer.TimeControlStatus](avplayer/timecontrolstatus-swift.property.md)
  A value that indicates whether playback is in progress, paused indefinitely, or waiting for network conditions to improve.
- [AVPlayer.TimeControlStatus](avplayer/timecontrolstatus-swift.enum.md)
  Constants that indicate the state of playback control.
- [func playImmediately(atRate: Float)](avplayer/playimmediately(atrate:).md)
  Plays the available media data immediately, at the specified rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/waitingreason)*