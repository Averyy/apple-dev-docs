# isPlaying

**Framework**: AVKit  
**Kind**: property  
**Required**: Yes

Indicates whether the media is currently playing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
var isPlaying: Bool { get set }
```

## See Also

- [var isReady: Bool](avinterfaceplaybackcontrollable-44aba/isready.md)
  Indicates whether the media source is ready for playback operations.
- [var isBuffering: Bool](avinterfaceplaybackcontrollable-44aba/isbuffering.md)
  Indicates whether the media source is currently buffering content.
- [var state: AVInterfacePlaybackState](avinterfaceplaybackcontrollable-44aba/state.md)
  The current operational state of the interface source.
- [var playbackError: (any Error)?](avinterfaceplaybackcontrollable-44aba/playbackerror.md)
  Error information when the source encounters a playback failure.
- [var containsLiveStreamingContent: Bool](avinterfaceplaybackcontrollable-44aba/containslivestreamingcontent.md)
  Indicates whether the content contains live streaming content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfaceplaybackcontrollable-44aba/isplaying)*