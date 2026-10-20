# waitingForCoordinatedPlayback

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

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

```c
extern AVPlayerWaitingReason const AVPlayerWaitingForCoordinatedPlaybackReason;
```

## See Also

### Player waiting reasons
- [static let evaluatingBufferingRate: AVPlayer.WaitingReason](./evaluatingbufferingrate.md)
  The player is waiting because it’s monitoring the buffer’s fill rate to determine whether playback is likely to complete without interruptions.
- [static let noItemToPlay: AVPlayer.WaitingReason](./noitemtoplay.md)
  The player is waiting because there’s no item to play.
- [static let toMinimizeStalls: AVPlayer.WaitingReason](./tominimizestalls.md)
  The player is waiting for appropriate playback conditions before starting playback.
- [static let interstitialEvent: AVPlayer.WaitingReason](./interstitialevent.md)
  The player is waiting for an interstitial event to complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/waitingreason/waitingforcoordinatedplayback)*