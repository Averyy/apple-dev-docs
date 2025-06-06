# leaveCue

**Framework**: AVFoundation  
**Kind**: property

A cue that indicates event playback occurs after primary playback ends without error, either at the end of the primary asset or at the client-specified forward playback end time.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static let leaveCue: AVPlayerInterstitialEvent.Cue
```

## See Also

- [static let noCue: AVPlayerInterstitialEvent.Cue](avplayerinterstitialevent/cue-swift.struct/nocue.md)
  A cue that indicates that playback starts at the interstitial event time or date.
- [static let joinCue: AVPlayerInterstitialEvent.Cue](avplayerinterstitialevent/cue-swift.struct/joincue.md)
  A cue that indicates that playback occurs before starting primary playback, regardless of initial primary playback position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/cue-swift.struct/leavecue)*