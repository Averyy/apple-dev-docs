# setRateFailed

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

An attempt to change the player’s rate fails.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static let setRateFailed: AVPlayer.RateDidChangeReason
```

```c
extern AVPlayerRateDidChangeReason const AVPlayerRateDidChangeReasonSetRateFailed;
```

## See Also

### Rate change reasons
- [static let appBackgrounded: AVPlayer.RateDidChangeReason](./appbackgrounded.md)
  An app transitions to the background.
- [static let audioSessionInterrupted: AVPlayer.RateDidChangeReason](./audiosessioninterrupted.md)
  The system interrupts the app’s audio session.
- [static let setRateCalled: AVPlayer.RateDidChangeReason](./setratecalled.md)
  An app makes a call to set the player’s rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/ratedidchangereason/setratefailed)*