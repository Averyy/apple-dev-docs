# Audio Session Categories

**Framework**: Audio Toolbox

Category identifiers for audio sessions, used as values for the [`kAudioSessionProperty_AudioCategory`](kaudiosessionproperty_audiocategory.md) property.

#### Overview

Each app running in iOS has a single audio session, which in turn has a single category. You can change your audio session’s category while your app is running.

You can refine the configuration provided by the [`kAudioSessionCategory_RecordAudio`](kaudiosessioncategory_recordaudio.md) and [`kAudioSessionCategory_PlayAndRecord`](kaudiosessioncategory_playandrecord.md) categories by using an audio session mode, as described in [`Audio Session Modes`](1618405-audio-session-modes.md).

Use the [`kAudioSessionCategory_AmbientSound`](kaudiosessioncategory_ambientsound.md) category when you want your sounds to mix with other audio (such as from the iPod app). Use one of the other playback categories when you want audio from other apps to be silenced when your session is active. However, you can enable mixing for the [`kAudioSessionCategory_MediaPlayback`](kaudiosessioncategory_mediaplayback.md) and [`kAudioSessionCategory_PlayAndRecord`](kaudiosessioncategory_playandrecord.md) categories by using the [`kAudioSessionProperty_OverrideCategoryMixWithOthers`](kaudiosessionproperty_overridecategorymixwithothers.md) property. For more information on audio session categories, see [`Audio Session Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Audio/Conceptual/AudioSessionProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007875).

## Topics

### Constants
- [var kAudioSessionCategory_AmbientSound: Int](kaudiosessioncategory_ambientsound.md)
  For an app in which sound playback is nonprimary—that is, your app can be used successfully with the sound turned off.
- [var kAudioSessionCategory_SoloAmbientSound: Int](kaudiosessioncategory_soloambientsound.md)
  The default category, used unless you set a category with the [`AudioSessionSetProperty(_:_:_:)`](audiosessionsetproperty(_:_:_:).md) function.
- [var kAudioSessionCategory_MediaPlayback: Int](kaudiosessioncategory_mediaplayback.md)
  For playing recorded music or other sounds that are central to the successful use of your app.
- [var kAudioSessionCategory_RecordAudio: Int](kaudiosessioncategory_recordaudio.md)
  For recording audio; this category silences playback audio. Recording continues with the screen locked.
- [var kAudioSessionCategory_PlayAndRecord: Int](kaudiosessioncategory_playandrecord.md)
  Allows recording (input) and playback (output) of audio, such as for a VOIP (voice over IP) app.
- [var kAudioSessionCategory_AudioProcessing: Int](kaudiosessioncategory_audioprocessing.md)
  For using an audio hardware codec or signal processor while not playing or recording audio. Use this category, for example, when performing offline audio format conversion.

## See Also

- [Audio Session Property Identifiers](1618455-audio-session-property-identifie.md)
  Property identifiers used with Audio Session Services in iOS.
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1618427-audio-session-categories)*