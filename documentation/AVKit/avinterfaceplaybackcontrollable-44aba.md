# AVInterfacePlaybackControllable

**Framework**: AVKit  
**Kind**: protocol

Provides playback control and state management for media content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
protocol AVInterfacePlaybackControllable : Observable
```

## Topics

### Inspecting playback state
- [var isPlaying: Bool](avinterfaceplaybackcontrollable-44aba/isplaying.md)
  Indicates whether the media is currently playing.
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
### Controlling playback speed
- [var playbackSpeed: Float](avinterfaceplaybackcontrollable-44aba/playbackspeed.md)
  The current playback speed multiplier.
- [var scanSpeed: Float](avinterfaceplaybackcontrollable-44aba/scanspeed.md)
  The scanning speed multiplier used during fast-forward or rewind operations.
- [var supportedSeekCapabilities: AVInterfaceSeekCapabilities](avinterfaceplaybackcontrollable-44aba/supportedseekcapabilities.md)
  The supported timeline navigation operations.

## Relationships

### Inherits From
- [Observable](../Observation/Observable.md)
### Inherited By
- [AVInterfaceControllable](avinterfacecontrollable-3xs3i.md)

## See Also

- [enum AVInterfacePlaybackState](avinterfaceplaybackstate.md)
  Describes possible playback states of the interface source.
- [struct AVInterfaceSeekCapabilities](avinterfaceseekcapabilities.md)
  Describes navigation capabilities of the media source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfaceplaybackcontrollable-44aba)*