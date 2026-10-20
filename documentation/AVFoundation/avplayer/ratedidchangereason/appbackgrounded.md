# appBackgrounded

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

An app transitions to the background.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static let appBackgrounded: AVPlayer.RateDidChangeReason
```

```c
extern AVPlayerRateDidChangeReason const AVPlayerRateDidChangeReasonAppBackgrounded;
```

## See Also

### Rate change reasons
- [static let audioSessionInterrupted: AVPlayer.RateDidChangeReason](./audiosessioninterrupted.md)
  The system interrupts the app’s audio session.
- [static let setRateCalled: AVPlayer.RateDidChangeReason](./setratecalled.md)
  An app makes a call to set the player’s rate.
- [static let setRateFailed: AVPlayer.RateDidChangeReason](./setratefailed.md)
  An attempt to change the player’s rate fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/ratedidchangereason/appbackgrounded)*