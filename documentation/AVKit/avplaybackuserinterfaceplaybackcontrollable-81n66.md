# AVPlaybackUserInterfacePlaybackControllable

**Framework**: AVKit  
**Kind**: protocol  
**Role**: Protocol

Provides playback control and state management for media content.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@protocol AVPlaybackUserInterfacePlaybackControllable <NSObject>
```

## Topics

### Instance Properties
- [buffering](./avplaybackuserinterfaceplaybackcontrollable-81n66/buffering.md)
  Indicates whether the media source is currently stalled waiting for data. Returns YES when the source cannot immediately sustain continuous playback. This may occur both before `isReady` becomes YES during initial loading, and after `isReady` is YES during mid-playback stalls. When YES, `isPlaying` may still be YES, indicating that playback should resume automatically once sufficient data is available. Must be key-value observable.
- [containsLiveStreamingContent](./avplaybackuserinterfaceplaybackcontrollable-81n66/containslivestreamingcontent.md)
  Indicates whether the content is a live stream. Returns YES for live streams and NO for on-demand content. Must be key-value observable.
- [defaultPlaybackSpeed](./avplaybackuserinterfaceplaybackcontrollable-81n66/defaultplaybackspeed.md)
  The default playback speed to use when playback begins. This value is used to set the initial playback rate when starting playback. A value of 1.0 represents normal speed. Must be key-value observable.
- [error](./avplaybackuserinterfaceplaybackcontrollable-81n66/error.md)
  Error information when the source encounters a playback failure. Nil when playback is functioning normally. Must be key-value observable.
- [playbackSpeed](./avplaybackuserinterfaceplaybackcontrollable-81n66/playbackspeed.md)
  The user’s preferred playback speed multiplier. This value is preserved across scanning operations. Must be key-value observable.
- [playing](./avplaybackuserinterfaceplaybackcontrollable-81n66/playing.md)
  Indicates whether playback is active. Setting this property to YES starts playback; setting it to NO pauses it. This property reflects playback intent — it should remain YES while `isBuffering` is YES, indicating that playback should resume automatically once sufficient data is available. Must be key-value observable.
- [ready](./avplaybackuserinterfaceplaybackcontrollable-81n66/ready.md)
  Indicates whether the media source is ready to begin playback. This property should transition from NO to YES once the source has loaded enough data to start playback, and should not revert. Use `isBuffering` to track temporary stalls that may occur after this point. Must be key-value observable.
- [scanSpeed](./avplaybackuserinterfaceplaybackcontrollable-81n66/scanspeed.md)
  The speed multiplier used during scanning (fast-forward or rewind). This is a transient override that is active only while `state` is scanning. It does not affect `playbackSpeed`. When scanning ends, playback resumes at `playbackSpeed`. Must be key-value observable.
- [state](./avplaybackuserinterfaceplaybackcontrollable-81n66/state.md)
  The current transport state of the playback source. Must be key-value observable.
- [supportedSeekCapabilities](./avplaybackuserinterfaceplaybackcontrollable-81n66/supportedseekcapabilities.md)
  An option set indicating which timeline navigation operations are supported by this media source. This property defines the available navigation capabilities, including precise seeking to specific time positions and accelerated scanning for fast-forward/rewind operations. The supported modes may vary based on content type, licensing restrictions, or technical limitations of the underlying media format. Must be key-value observable.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [AVPlaybackUserInterfaceControllable](./avplaybackuserinterfacecontrollable-7ti30.md)

## See Also

### Playback control
- [enum AVPlaybackUserInterfacePlaybackState](./avplaybackuserinterfaceplaybackstate.md)
  Describes possible transport states of the playback source.
- [struct AVPlaybackUserInterfaceSeekCapabilities](./avplaybackuserinterfaceseekcapabilities.md)
  Describes navigation capabilities of the media source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-81n66)*