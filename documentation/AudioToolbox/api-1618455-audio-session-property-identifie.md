# Audio Session Property Identifiers

**Framework**: Audio Toolbox

Property identifiers used with Audio Session Services in iOS.

#### Overview

Use these property identifiers in concert with the [`AudioSessionGetProperty(_:_:_:)`](audiosessiongetproperty(_:_:_:).md), [`AudioSessionSetProperty(_:_:_:)`](audiosessionsetproperty(_:_:_:).md), and [`AudioSessionAddPropertyListener(_:_:_:)`](audiosessionaddpropertylistener(_:_:_:).md) functions.

## Topics

### Constants
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
- [var kAudioSessionProperty_OtherMixableAudioShouldDuck: Int](kaudiosessionproperty_othermixableaudioshouldduck.md)
  For audio session categories that allow audio mixing with other apps, specifies whether other audio should be reduced in level when your app produces sound. This property has a value of `FALSE` (0) by default. Set it to a nonzero value to turn on ducking.
- [var kAudioSessionProperty_OverrideCategoryMixWithOthers: Int](kaudiosessionproperty_overridecategorymixwithothers.md)
  Changes the mixing behavior of the [`kAudioSessionCategory_MediaPlayback`](kaudiosessioncategory_mediaplayback.md) and [`kAudioSessionCategory_PlayAndRecord`](kaudiosessioncategory_playandrecord.md) audio session categories.
- [var kAudioSessionProperty_OverrideCategoryDefaultToSpeaker: Int](kaudiosessionproperty_overridecategorydefaulttospeaker.md)
  Specifies whether or not to route audio to the speaker (instead of to the receiver) when no other audio route, such as a headset, is connected.
- [var kAudioSessionProperty_OverrideCategoryEnableBluetoothInput: Int](kaudiosessionproperty_overridecategoryenablebluetoothinput.md)
  Allows a paired Bluetooth device to appear as an available audio input route.
- [var kAudioSessionProperty_InterruptionType: Int](kaudiosessionproperty_interruptiontype.md)
  Indicates the type of an end-interruption event.
- [var kAudioSessionProperty_Mode: Int](kaudiosessionproperty_mode.md)
  A read/write `UIInt32` value that specifies the audio session mode.
- [var kAudioSessionProperty_InputSources: Int](kaudiosessionproperty_inputsources.md)
  Details on the available audio input sources.
- [var kAudioSessionProperty_OutputDestinations: Int](kaudiosessionproperty_outputdestinations.md)
  Details on the available audio output destinations.
- [var kAudioSessionProperty_InputSource: Int](kaudiosessionproperty_inputsource.md)
  The audio input source.
- [var kAudioSessionProperty_OutputDestination: Int](kaudiosessionproperty_outputdestination.md)
  The audio output destination.
- [var kAudioSessionProperty_InputGainAvailable: Int](kaudiosessionproperty_inputgainavailable.md)
  A read-only `UInt32` value that indicates whether or not audio input gain adjustment is available, where a nonzero value means adjustment is available.
- [var kAudioSessionProperty_InputGainScalar: Int](kaudiosessionproperty_inputgainscalar.md)
  A read/write `Float32` value that indicates the audio input gain setting for the active input source.
- [var kAudioSessionProperty_AudioRouteDescription: Int](kaudiosessionproperty_audioroutedescription.md)
  Information about an audio route.

## See Also

- [Audio Session Categories](1618427-audio-session-categories.md)
  Category identifiers for audio sessions, used as values for the [`kAudioSessionProperty_AudioCategory`](kaudiosessionproperty_audiocategory.md) property.
- [Audio Session Modes](1618405-audio-session-modes.md)
  Mode identifiers for audio sessions, used as values for the [`kAudioSessionProperty_Mode`](kaudiosessionproperty_mode.md) property.
- [Audio Session Category Route Overrides](1618372-audio-session-category-route-ove.md)
  Specifies whether the default audio route for the `PlayAndRecord` category should be overridden.
- [Audio Session Activation Flags](1618357-audio-session-activation-flags.md)
  Flags that provide additional information about your app’s audio intentions upon session activation or deactivation.
- [Audio Session Interruption States](1618425-audio-session-interruption-state.md)
  Identifiers used with the [`AudioSessionInterruptionListener`](audiosessioninterruptionlistener.md) callback function in iOS to indicate that an audio interruption has started or stopped.
- [typealias AudioSessionInterruptionType](audiosessioninterruptiontype.md)
  Values that indicate the nature of the interruption that ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1618455-audio-session-property-identifie)*