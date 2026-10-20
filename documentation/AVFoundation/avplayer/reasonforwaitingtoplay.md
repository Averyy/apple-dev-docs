# reasonForWaitingToPlay

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The reason the player is currently waiting for playback to begin or resume.

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
var reasonForWaitingToPlay: AVPlayer.WaitingReason? { get }
```

```objc
@property (readonly, nullable) AVPlayerWaitingReason reasonForWaitingToPlay;
```

#### Discussion

When the value of the player’s [`timeControlStatus`](./timecontrolstatus-swift.property.md) is [`AVPlayer.TimeControlStatus.waitingToPlayAtSpecifiedRate`](./timecontrolstatus-swift.enum/waitingtoplayatspecifiedrate.md), you can use this property determine the reason the player is currently waiting for playback to begin or resume. Possible values for this property are:

- [`toMinimizeStalls`](./waitingreason/tominimizestalls.md)
- [`noItemToPlay`](./waitingreason/noitemtoplay.md)
- [`evaluatingBufferingRate`](./waitingreason/evaluatingbufferingrate.md)

The value of this property will be `nil` if the player’s [`timeControlStatus`](./timecontrolstatus-swift.property.md) is a value other than [`AVPlayer.TimeControlStatus.waitingToPlayAtSpecifiedRate`](./timecontrolstatus-swift.enum/waitingtoplayatspecifiedrate.md).

You can use the value of this property to conditionally show UI indicating the player’s waiting state. This property is observable using key-value observing.

## See Also

### Configuring waiting behavior
- [var automaticallyWaitsToMinimizeStalling: Bool](./automaticallywaitstominimizestalling.md)
  A Boolean value that indicates whether the player should automatically delay playback in order to minimize stalling.
- [AVPlayer.WaitingReason](./waitingreason.md)
  The reasons a player is waiting to begin or resume playback.
- [var timeControlStatus: AVPlayer.TimeControlStatus](./timecontrolstatus-swift.property.md)
  A value that indicates whether playback is in progress, paused indefinitely, or waiting for network conditions to improve.
- [AVPlayer.TimeControlStatus](./timecontrolstatus-swift.enum.md)
  Constants that indicate the state of playback control.
- [func playImmediately(atRate: Float)](./playimmediately%28atrate%29.md)
  Plays the available media data immediately, at the specified rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/reasonforwaitingtoplay)*