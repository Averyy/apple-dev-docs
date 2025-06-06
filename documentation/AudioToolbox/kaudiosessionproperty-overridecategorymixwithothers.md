# kAudioSessionProperty_OverrideCategoryMixWithOthers

**Framework**: Audio Toolbox  
**Kind**: var

Changes the mixing behavior of the [`kAudioSessionCategory_MediaPlayback`](kaudiosessioncategory_mediaplayback.md) and [`kAudioSessionCategory_PlayAndRecord`](kaudiosessioncategory_playandrecord.md) audio session categories.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioSessionProperty_OverrideCategoryMixWithOthers: Int { get }
```

#### Discussion

A read/write `UInt32` value. By default, the value of this property is `FALSE` (`0`).

Setting this property to `TRUE` (any nonzero value) allows audio mixing with other apps. Other aspects of these categories, such as their Silent switch behavior, are not affected. (The switch is called the  on iPhone.)

When the audio session category changes, such as during an interruption, the value of this property reverts to `FALSE`. To regain mixing behavior you must then re-set this property.

Always check to see if setting this property succeeds or fails, and react appropriately; behavior may change in future releases of iOS.

## See Also

- [var kAudioSessionProperty_PreferredHardwareSampleRate: Int](kaudiosessionproperty_preferredhardwaresamplerate.md)
  Your preferred hardware sample rate for the audio session. A read/write `Float64` value. The actual sample rate may be different and can be obtained using the `kAudioSessionProperty_CurrentHardwareSampleRate` property.
- [var kAudioSessionProperty_PreferredHardwareIOBufferDuration: Int](kaudiosessionproperty_preferredhardwareiobufferduration.md)
  Your preferred hardware I/O buffer duration in seconds. Do not set this property unless you require lower I/O latency than is provided by default.
- [var kAudioSessionProperty_AudioCategory: Int](kaudiosessionproperty_audiocategory.md)
  The category for the audio session. A read/write `UInt32` value.
- [var kAudioSessionProperty_AudioRouteChange: Int](kaudiosessionproperty_audioroutechange.md)
  The reason the audio route changed.
- [var kAudioSessionProperty_CurrentHardwareSampleRate: Int](kaudiosessionproperty_currenthardwaresamplerate.md)
  Indicates the current hardware sample rate. A read-only `Float64` value.
- [var kAudioSessionProperty_CurrentHardwareInputNumberChannels: Int](kaudiosessionproperty_currenthardwareinputnumberchannels.md)
  Indicates the current number of audio hardware input channels. A read-only `UInt32` value.
- [var kAudioSessionProperty_CurrentHardwareOutputNumberChannels: Int](kaudiosessionproperty_currenthardwareoutputnumberchannels.md)
  Indicates the current number of audio hardware output channels. A read-only `UInt32` value.
- [var kAudioSessionProperty_CurrentHardwareOutputVolume: Int](kaudiosessionproperty_currenthardwareoutputvolume.md)
  Indicates the current audio output volume as `Float32` value between 0.0 and 1.0. Read-only. This value is available to your app by way of a property listener callback function. See [`AudioSessionAddPropertyListener(_:_:_:)`](audiosessionaddpropertylistener(_:_:_:).md).
- [var kAudioSessionProperty_CurrentHardwareInputLatency: Int](kaudiosessionproperty_currenthardwareinputlatency.md)
  Indicates the current hardware input latency, in seconds, as a read-only `Float32` value.
- [var kAudioSessionProperty_CurrentHardwareOutputLatency: Int](kaudiosessionproperty_currenthardwareoutputlatency.md)
  Indicates the current hardware output latency, in seconds, as a read-only `Float32` value.
- [var kAudioSessionProperty_CurrentHardwareIOBufferDuration: Int](kaudiosessionproperty_currenthardwareiobufferduration.md)
  Indicates the current hardware IO buffer duration, in seconds, as a read-only `Float32` value.
- [var kAudioSessionProperty_OtherAudioIsPlaying: Int](kaudiosessionproperty_otheraudioisplaying.md)
  Indicates whether or not another app (typically, the iPod app) is currently playing audio. Read-only. A non-zero `UInt32` value indicates that other audio is playing.
- [var kAudioSessionProperty_OverrideAudioRoute: Int](kaudiosessionproperty_overrideaudioroute.md)
  Specifies whether or not to override the audio session category’s typical audio route.
- [var kAudioSessionProperty_AudioInputAvailable: Int](kaudiosessionproperty_audioinputavailable.md)
  Indicates if audio input is available (a nonzero value) or not (a value of 0).
- [var kAudioSessionProperty_ServerDied: Int](kaudiosessionproperty_serverdied.md)
  Indicates if the audio server has died (indicated by a nonzero `UInt32` value) or is still running (a value of 0).


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionproperty_overridecategorymixwithothers)*