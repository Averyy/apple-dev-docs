# Audio Session Category Route Overrides

**Framework**: Audio Toolbox

Specifies whether the default audio route for the `PlayAndRecord` category should be overridden.

#### Overview

The `kAudioSessionCategory_PlayAndRecord` category supports simultaneous input and output. You could use this category, for example, to add an effect to audio coming into the device’s microphone. By default, output audio for this category goes to the receiver—the speaker you hold to your ear when on a phone call. The `kAudioSessionOverrideAudioRoute_Speaker` constant lets you direct the output audio to the speaker situated at the bottom of the phone.

## Topics

### Constants
- [var kAudioSessionOverrideAudioRoute_None: Int](kaudiosessionoverrideaudioroute_none.md)
  Specifies, for the [`kAudioSessionCategory_PlayAndRecord`](kaudiosessioncategory_playandrecord.md) category, that output audio should go to the receiver. This is the default output audio route for this category.
- [var kAudioSessionOverrideAudioRoute_Speaker: Int](kaudiosessionoverrideaudioroute_speaker.md)
  Specifies, for the [`kAudioSessionCategory_PlayAndRecord`](kaudiosessioncategory_playandrecord.md) category,  that output audio should go to the speaker, not the receiver.

## See Also

- [Audio Session Property Identifiers](1618455-audio-session-property-identifie.md)
  Property identifiers used with Audio Session Services in iOS.
- [Audio Session Categories](1618427-audio-session-categories.md)
  Category identifiers for audio sessions, used as values for the [`kAudioSessionProperty_AudioCategory`](kaudiosessionproperty_audiocategory.md) property.
- [Audio Session Modes](1618405-audio-session-modes.md)
  Mode identifiers for audio sessions, used as values for the [`kAudioSessionProperty_Mode`](kaudiosessionproperty_mode.md) property.
- [Audio Session Activation Flags](1618357-audio-session-activation-flags.md)
  Flags that provide additional information about your app’s audio intentions upon session activation or deactivation.
- [Audio Session Interruption States](1618425-audio-session-interruption-state.md)
  Identifiers used with the [`AudioSessionInterruptionListener`](audiosessioninterruptionlistener.md) callback function in iOS to indicate that an audio interruption has started or stopped.
- [typealias AudioSessionInterruptionType](audiosessioninterruptiontype.md)
  Values that indicate the nature of the interruption that ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1618372-audio-session-category-route-ove)*