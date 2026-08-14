# AVPlaybackUserInterfacePlaybackControllable

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
protocol AVPlaybackUserInterfacePlaybackControllable : AnyObject, Observable
```

## Topics

### Instance Properties
- [var containsLiveStreamingContent: Bool](avplaybackuserinterfaceplaybackcontrollable-9he54/containslivestreamingcontent.md)
  Indicates whether the content is a live stream.
- [var error: (any Error)?](avplaybackuserinterfaceplaybackcontrollable-9he54/error.md)
  Error information when the source encounters a playback failure.
- [var isBuffering: Bool](avplaybackuserinterfaceplaybackcontrollable-9he54/isbuffering.md)
  Indicates whether the media source is currently stalled waiting for data.
- [var isPlaying: Bool](avplaybackuserinterfaceplaybackcontrollable-9he54/isplaying.md)
  Indicates whether playback is active.
- [var isReady: Bool](avplaybackuserinterfaceplaybackcontrollable-9he54/isready.md)
  Indicates whether the media source is ready to begin playback.
- [var playbackSpeed: Float](avplaybackuserinterfaceplaybackcontrollable-9he54/playbackspeed.md)
  The user’s preferred playback speed multiplier. This value is preserved across scanning operations.
- [var scanSpeed: Float](avplaybackuserinterfaceplaybackcontrollable-9he54/scanspeed.md)
  The speed multiplier used during scanning (fast-forward or rewind). This is a transient override active only while `state` is scanning. It does not affect `playbackSpeed`. When scanning ends, playback resumes at `playbackSpeed`.
- [var state: AVPlaybackUserInterfacePlaybackState](avplaybackuserinterfaceplaybackcontrollable-9he54/state.md)
  The current transport state of the playback source.
- [var supportedSeekCapabilities: AVPlaybackUserInterfaceSeekCapabilities](avplaybackuserinterfaceplaybackcontrollable-9he54/supportedseekcapabilities.md)
  The supported timeline navigation operations.

## Relationships

### Inherits From
- [Observable](../observation/observable.md)
### Inherited By
- [AVPlaybackUserInterfaceControllable](avplaybackuserinterfacecontrollable-92fri.md)

## See Also

- [enum AVPlaybackUserInterfacePlaybackState](avplaybackuserinterfaceplaybackstate.md)
  Describes possible transport states of the playback source.
- [struct AVPlaybackUserInterfaceSeekCapabilities](avplaybackuserinterfaceseekcapabilities.md)
  Describes navigation capabilities of the media source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-9he54)*