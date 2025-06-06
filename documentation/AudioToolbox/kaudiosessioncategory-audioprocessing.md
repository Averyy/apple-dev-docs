# kAudioSessionCategory_AudioProcessing

**Framework**: Audio Toolbox  
**Kind**: var

For using an audio hardware codec or signal processor while not playing or recording audio. Use this category, for example, when performing offline audio format conversion.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioSessionCategory_AudioProcessing: Int { get }
```

#### Discussion

This category disables playback (audio output) and disables recording (audio input).

Audio processing does not normally continue when your app is in the background. However, when your app moves to the background, you can request additional time to complete processing. for more information, see [`Internationalizing Your App`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/ExpectedAppBehaviors/ExpectedAppBehaviors.html#//apple_ref/doc/uid/TP40007072-CH3-SW10) in [`App Programming Guide for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072).

This category is equivalent to the [`audioProcessing`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession/Category-swift.struct/audioProcessing) category provided in the AVFoundation framework.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioncategory_audioprocessing)*