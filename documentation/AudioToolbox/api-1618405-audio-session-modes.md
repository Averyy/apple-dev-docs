# Audio Session Modes

**Framework**: Audio Toolbox  
**Role**: API Collection

Mode identifiers for audio sessions, used as values for the [`kAudioSessionProperty_Mode`](./kaudiosessionproperty_mode.md) property.

#### Overview

Each app running in iOS has a single audio session, which in turn has a single mode. A mode refines the device’s audio configuration according to the purpose of the mode. You can change your audio session’s mode only when your audio session is inactive, and only if your audio session category is configured to disallow mixing with other apps.

> **Note**:  Misusing a mode by setting it for an inappropriate audio session category—such as setting the [`kAudioSessionMode_VoiceChat`](./kaudiosessionmode_voicechat.md) mode for the [`kAudioSessionCategory_AudioProcessing`](./kaudiosessioncategory_audioprocessing.md) category—results in the behavior provided by the [`kAudioSessionMode_Default`](./kaudiosessionmode_default.md) mode.

## Topics

### Constants
- [var kAudioSessionMode_Default: Int](./kaudiosessionmode_default.md)
  The default mode; used unless you set a mode with the [`AudioSessionSetProperty(_:_:_:)`](./audiosessionsetproperty%28_,_,_%29.md) function.
- [var kAudioSessionMode_VoiceChat: Int](./kaudiosessionmode_voicechat.md)
  Specify this mode if your app is performing two-way voice communication, such as using Voice over Internet Protocol (VoIP).
- [var kAudioSessionMode_VideoRecording: Int](./kaudiosessionmode_videorecording.md)
  Specify this mode if your app is recording a movie.
- [var kAudioSessionMode_Measurement: Int](./kaudiosessionmode_measurement.md)
  Specify this mode if your app is performing measurement of incoming audio.
- [var kAudioSessionMode_GameChat: Int](./kaudiosessionmode_gamechat.md)

## See Also

### Audio Session Support
- [Audio Session Property Identifiers](./api-1618455-audio-session-property-identifie.md)
  Property identifiers used with Audio Session Services in iOS.
- [Audio Session Categories](./api-1618427-audio-session-categories.md)
  Category identifiers for audio sessions, used as values for the [`kAudioSessionProperty_AudioCategory`](./kaudiosessionproperty_audiocategory.md) property.
- [Audio Session Category Route Overrides](./api-1618372-audio-session-category-route-ove.md)
  Specifies whether the default audio route for the `PlayAndRecord` category should be overridden.
- [Audio Session Activation Flags](./api-1618357-audio-session-activation-flags.md)
  Flags that provide additional information about your app’s audio intentions upon session activation or deactivation.
- [Audio Session Interruption States](./api-1618425-audio-session-interruption-state.md)
  Identifiers used with the [`AudioSessionInterruptionListener`](./audiosessioninterruptionlistener.md) callback function in iOS to indicate that an audio interruption has started or stopped.
- [typealias AudioSessionInterruptionType](./audiosessioninterruptiontype.md)
  Values that indicate the nature of the interruption that ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1618405-audio-session-modes)*