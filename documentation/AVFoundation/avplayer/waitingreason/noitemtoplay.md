# noItemToPlay

**Framework**: AVFoundation  
**Kind**: property

The player is waiting because there’s no item to play.

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
static let noItemToPlay: AVPlayer.WaitingReason
```

## See Also

- [static let evaluatingBufferingRate: AVPlayer.WaitingReason](avplayer/waitingreason/evaluatingbufferingrate.md)
  The player is waiting because it’s monitoring the buffer’s fill rate to determine whether playback is likely to complete without interruptions.
- [static let toMinimizeStalls: AVPlayer.WaitingReason](avplayer/waitingreason/tominimizestalls.md)
  The player is waiting for appropriate playback conditions before starting playback.
- [static let interstitialEvent: AVPlayer.WaitingReason](avplayer/waitingreason/interstitialevent.md)
  The player is waiting for an interstitial event to complete.
- [static let waitingForCoordinatedPlayback: AVPlayer.WaitingReason](avplayer/waitingreason/waitingforcoordinatedplayback.md)
  The player is waiting for another participant in a coordinated playback session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/waitingreason/noitemtoplay)*