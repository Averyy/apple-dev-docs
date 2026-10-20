# audioSessionInterrupted

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The system interrupts the app’s audio session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static let audioSessionInterrupted: AVPlayer.RateDidChangeReason
```

```c
extern AVPlayerRateDidChangeReason const AVPlayerRateDidChangeReasonAudioSessionInterrupted;
```

## See Also

### Rate change reasons
- [static let appBackgrounded: AVPlayer.RateDidChangeReason](./appbackgrounded.md)
  An app transitions to the background.
- [static let setRateCalled: AVPlayer.RateDidChangeReason](./setratecalled.md)
  An app makes a call to set the player’s rate.
- [static let setRateFailed: AVPlayer.RateDidChangeReason](./setratefailed.md)
  An attempt to change the player’s rate fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/ratedidchangereason/audiosessioninterrupted)*