# kAudioSessionCategory_RecordAudio

**Framework**: Audio Toolbox  
**Kind**: var

For recording audio; this category silences playback audio. Recording continues with the screen locked.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioSessionCategory_RecordAudio: Int { get }
```

#### Discussion

This category is equivalent to the [`record`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession/Category-swift.struct/record) category provided in the AVFoundation framework.

## See Also

- [var kAudioSessionCategory_AmbientSound: Int](kaudiosessioncategory_ambientsound.md)
  For an app in which sound playback is nonprimary—that is, your app can be used successfully with the sound turned off.
- [var kAudioSessionCategory_SoloAmbientSound: Int](kaudiosessioncategory_soloambientsound.md)
  The default category, used unless you set a category with the [`AudioSessionSetProperty(_:_:_:)`](audiosessionsetproperty(_:_:_:).md) function.
- [var kAudioSessionCategory_MediaPlayback: Int](kaudiosessioncategory_mediaplayback.md)
  For playing recorded music or other sounds that are central to the successful use of your app.
- [var kAudioSessionCategory_PlayAndRecord: Int](kaudiosessioncategory_playandrecord.md)
  Allows recording (input) and playback (output) of audio, such as for a VOIP (voice over IP) app.
- [var kAudioSessionCategory_AudioProcessing: Int](kaudiosessioncategory_audioprocessing.md)
  For using an audio hardware codec or signal processor while not playing or recording audio. Use this category, for example, when performing offline audio format conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioncategory_recordaudio)*