# AVInterfacePlaybackControllable

**Framework**: AVKit  
**Kind**: protocol  
**Role**: Protocol

Provides playback control and state management for media content.

## Declaration

```objc
@protocol AVInterfacePlaybackControllable <NSObject>
```

## Topics

### Instance Properties
- [buffering](./avinterfaceplaybackcontrollable/buffering.md)
  Indicates whether the media source is currently buffering content. Returns YES when the source is loading data and cannot immediately continue playback. Must be key-value observable.
- [containsLiveStreamingContent](./avinterfaceplaybackcontrollable/containslivestreamingcontent.md)
  Indicates whether the content contains live streaming content. Returns YES for live streams and NO for on-demand content. Must be key-value observable.
- [defaultPlaybackSpeed](./avinterfaceplaybackcontrollable/defaultplaybackspeed.md)
  The default playback speed to use when playback begins. This value is used to set the initial playback rate when starting playback. A value of 1.0 represents normal speed. Must be key-value observable.
- [playbackError](./avinterfaceplaybackcontrollable/playbackerror.md)
  Error information when the source encounters a playback failure. Nil when playback is functioning normally. Must be key-value observable.
- [playbackSpeed](./avinterfaceplaybackcontrollable/playbackspeed.md)
  The current playback speed multiplier. A value of 1.0 represents normal speed, values greater than 1.0 represent faster playback, and values between 0.0 and 1.0 represent slower playback. Must be key-value observable.
- [playing](./avinterfaceplaybackcontrollable/playing.md)
  Indicates whether the media is currently playing. Setting this property starts or pauses playback. Must be key-value observable.
- [ready](./avinterfaceplaybackcontrollable/ready.md)
  Indicates whether the media source is ready for playback operations. Returns YES when the source has sufficient data and is prepared to begin playback. Use this property to determine when playback controls should be enabled and when the media can respond to play requests. Must be key-value observable.
- [scanSpeed](./avinterfaceplaybackcontrollable/scanspeed.md)
  The scanning speed multiplier used during fast-forward or rewind operations. A positive value indicates forward scanning, negative indicates backward scanning. Must be key-value observable.
- [state](./avinterfaceplaybackcontrollable/state.md)
  The current operational state of the interface source. Must be key-value observable.
- [supportedSeekCapabilities](./avinterfaceplaybackcontrollable/supportedseekcapabilities.md)
  An option set indicating which timeline navigation operations are supported by this media source. This property defines the available navigation capabilities, including precise seeking to specific time positions and accelerated scanning for fast-forward/rewind operations. The supported modes may vary based on content type, licensing restrictions, or technical limitations of the underlying media format. Must be key-value observable.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [AVInterfaceControllable](./avinterfacecontrollable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfaceplaybackcontrollable)*