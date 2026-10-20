# noCue

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A cue that indicates that playback starts at the interstitial event time or date.

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
static let noCue: AVPlayerInterstitialEvent.Cue
```

```c
extern AVPlayerInterstitialEventCue const AVPlayerInterstitialEventNoCue;
```

## See Also

### Cues
- [static let joinCue: AVPlayerInterstitialEvent.Cue](./joincue.md)
  A cue that indicates that playback occurs before starting primary playback, regardless of initial primary playback position.
- [static let leaveCue: AVPlayerInterstitialEvent.Cue](./leavecue.md)
  A cue that indicates event playback occurs after primary playback ends without error, either at the end of the primary asset or at the client-specified forward playback end time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/cue-swift.struct/nocue)*