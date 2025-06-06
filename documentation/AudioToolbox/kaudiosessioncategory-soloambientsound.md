# kAudioSessionCategory_SoloAmbientSound

**Framework**: Audio Toolbox  
**Kind**: var

The default category, used unless you set a category with the [`AudioSessionSetProperty(_:_:_:)`](audiosessionsetproperty(_:_:_:).md) function.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioSessionCategory_SoloAmbientSound: Int { get }
```

#### Discussion

When you use this category, audio from other apps is silenced. Your audio is silenced by screen locking and by the Silent switch (called the  on iPhone).

This category is equivalent to the [`soloAmbient`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession/Category-swift.struct/soloAmbient) category provided in the AVFoundation framework.

## See Also

- [var kAudioSessionCategory_AmbientSound: Int](kaudiosessioncategory_ambientsound.md)
  For an app in which sound playback is nonprimary—that is, your app can be used successfully with the sound turned off.
- [var kAudioSessionCategory_MediaPlayback: Int](kaudiosessioncategory_mediaplayback.md)
  For playing recorded music or other sounds that are central to the successful use of your app.
- [var kAudioSessionCategory_RecordAudio: Int](kaudiosessioncategory_recordaudio.md)
  For recording audio; this category silences playback audio. Recording continues with the screen locked.
- [var kAudioSessionCategory_PlayAndRecord: Int](kaudiosessioncategory_playandrecord.md)
  Allows recording (input) and playback (output) of audio, such as for a VOIP (voice over IP) app.
- [var kAudioSessionCategory_AudioProcessing: Int](kaudiosessioncategory_audioprocessing.md)
  For using an audio hardware codec or signal processor while not playing or recording audio. Use this category, for example, when performing offline audio format conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioncategory_soloambientsound)*