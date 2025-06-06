# audioSessionInterrupted

**Framework**: AVFoundation  
**Kind**: property

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

## See Also

- [static let appBackgrounded: AVPlayer.RateDidChangeReason](avplayer/ratedidchangereason/appbackgrounded.md)
  An app transitions to the background.
- [static let setRateCalled: AVPlayer.RateDidChangeReason](avplayer/ratedidchangereason/setratecalled.md)
  An app makes a call to set the player’s rate.
- [static let setRateFailed: AVPlayer.RateDidChangeReason](avplayer/ratedidchangereason/setratefailed.md)
  An attempt to change the player’s rate fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/ratedidchangereason/audiosessioninterrupted)*