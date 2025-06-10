# AVPlayerInterstitialEvent.Cue

**Framework**: AVFoundation  
**Kind**: struct

A structure that defines standard cues to play interstitial content.

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
struct Cue
```

## Topics

### Cues
- [static let noCue: AVPlayerInterstitialEvent.Cue](avplayerinterstitialevent/cue-swift.struct/nocue.md)
  A cue that indicates that playback starts at the interstitial event time or date.
- [static let joinCue: AVPlayerInterstitialEvent.Cue](avplayerinterstitialevent/cue-swift.struct/joincue.md)
  A cue that indicates that playback occurs before starting primary playback, regardless of initial primary playback position.
- [static let leaveCue: AVPlayerInterstitialEvent.Cue](avplayerinterstitialevent/cue-swift.struct/leavecue.md)
  A cue that indicates event playback occurs after primary playback ends without error, either at the end of the primary asset or at the client-specified forward playback end time.
### Initializers
- [init(rawValue: String)](avplayerinterstitialevent/cue-swift.struct/init(rawvalue:).md)
  Creates an interstitial event cue from its raw string value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var cue: AVPlayerInterstitialEvent.Cue](avplayerinterstitialevent/cue-swift.property.md)
  A cue to schedule interstitial event playback at a predefined position during primary playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/cue-swift.struct)*