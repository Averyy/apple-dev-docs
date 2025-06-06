# kAudioSessionMode_Measurement

**Framework**: Audio Toolbox  
**Kind**: var

Specify this mode if your app is performing measurement of incoming audio.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioSessionMode_Measurement: Int { get }
```

#### Discussion

When this mode is in use, the device does not perform automatic gain adjustment on incoming audio. For use with the [`kAudioSessionCategory_RecordAudio`](kaudiosessioncategory_recordaudio.md) or [`kAudioSessionCategory_PlayAndRecord`](kaudiosessioncategory_playandrecord.md) audio session categories. On devices with more than one built-in microphone, the primary microphone is used.

This mode is equivalent to the [`measurement`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession/Mode-swift.struct/measurement) mode provided in the AVFoundation framework.

## See Also

- [var kAudioSessionMode_Default: Int](kaudiosessionmode_default.md)
  The default mode; used unless you set a mode with the [`AudioSessionSetProperty(_:_:_:)`](audiosessionsetproperty(_:_:_:).md) function.
- [var kAudioSessionMode_VoiceChat: Int](kaudiosessionmode_voicechat.md)
  Specify this mode if your app is performing two-way voice communication, such as using Voice over Internet Protocol (VoIP).
- [var kAudioSessionMode_VideoRecording: Int](kaudiosessionmode_videorecording.md)
  Specify this mode if your app is recording a movie.
- [var kAudioSessionMode_GameChat: Int](kaudiosessionmode_gamechat.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionmode_measurement)*