# AVPlayerAudiovisualBackgroundPlaybackPolicy

**Framework**: AVFoundation  
**Kind**: enum

Policies that describe playback behavior when an app transitions to the background while playing video.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum AVPlayerAudiovisualBackgroundPlaybackPolicy
```

## Topics

### Policies
- [AVPlayerAudiovisualBackgroundPlaybackPolicy.automatic](avplayeraudiovisualbackgroundplaybackpolicy/automatic.md)
  The system decides whether playback continues.
- [AVPlayerAudiovisualBackgroundPlaybackPolicy.continuesIfPossible](avplayeraudiovisualbackgroundplaybackpolicy/continuesifpossible.md)
  The app continues playback, if possible.
- [AVPlayerAudiovisualBackgroundPlaybackPolicy.pauses](avplayeraudiovisualbackgroundplaybackpolicy/pauses.md)
  The app pauses playback.
### Initializers
- [init?(rawValue: Int)](avplayeraudiovisualbackgroundplaybackpolicy/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var audiovisualBackgroundPlaybackPolicy: AVPlayerAudiovisualBackgroundPlaybackPolicy](avplayer/audiovisualbackgroundplaybackpolicy.md)
  A policy that determines how playback of audiovisual media continues when the app transitions to the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeraudiovisualbackgroundplaybackpolicy)*