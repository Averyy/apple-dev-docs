# waitingForCoordinatedPlayback

**Framework**: AVFoundation  
**Kind**: property

The player is waiting for another participant in a coordinated playback session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static let waitingForCoordinatedPlayback: AVPlayer.WaitingReason
```

## See Also

- [static let evaluatingBufferingRate: AVPlayer.WaitingReason](avplayer/waitingreason/evaluatingbufferingrate.md)
  The player is waiting because it’s monitoring the buffer’s fill rate to determine whether playback is likely to complete without interruptions.
- [static let noItemToPlay: AVPlayer.WaitingReason](avplayer/waitingreason/noitemtoplay.md)
  The player is waiting because there’s no item to play.
- [static let toMinimizeStalls: AVPlayer.WaitingReason](avplayer/waitingreason/tominimizestalls.md)
  The player is waiting for appropriate playback conditions before starting playback.
- [static let interstitialEvent: AVPlayer.WaitingReason](avplayer/waitingreason/interstitialevent.md)
  The player is waiting for an interstitial event to complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/waitingreason/waitingforcoordinatedplayback)*