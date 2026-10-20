# AVPlayerInterstitialEvent.Cue

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * AVPlayerInterstitialEventCue;
```

## Topics

### Cues
- [static let noCue: AVPlayerInterstitialEvent.Cue](./cue-swift.struct/nocue.md)
  A cue that indicates that playback starts at the interstitial event time or date.
- [static let joinCue: AVPlayerInterstitialEvent.Cue](./cue-swift.struct/joincue.md)
  A cue that indicates that playback occurs before starting primary playback, regardless of initial primary playback position.
- [static let leaveCue: AVPlayerInterstitialEvent.Cue](./cue-swift.struct/leavecue.md)
  A cue that indicates event playback occurs after primary playback ends without error, either at the end of the primary asset or at the client-specified forward playback end time.
### Initializers
- [init(rawValue: String)](./cue-swift.struct/init%28rawvalue%29.md)
  Creates an interstitial event cue from its raw string value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring cues
- [var cue: AVPlayerInterstitialEvent.Cue](./cue-swift.property.md)
  A cue to schedule interstitial event playback at a predefined position during primary playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/cue-swift.struct)*