# kAudioSessionMode_VideoRecording

**Framework**: Audio Toolbox  
**Kind**: var  
**Role**: Global Variable

Specify this mode if your app is recording a movie.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
var kAudioSessionMode_VideoRecording: Int { get }
```

```c
kAudioSessionMode_VideoRecording
```

#### Discussion

For use with the [`kAudioSessionCategory_RecordAudio`](./kaudiosessioncategory_recordaudio.md) audio session category. Also works with the [`kAudioSessionCategory_PlayAndRecord`](./kaudiosessioncategory_playandrecord.md) category. On devices with more than one built-in microphone, the microphone closest to the video camera is used.

Using this mode may result in the system providing appropriate audio signal processing.

This mode is equivalent to the [`videoRecording`](../AVFAudio/avaudiosession/mode-swift.struct/videorecording.md) mode provided in the AVFoundation framework.

## See Also

### Constants
- [var kAudioSessionMode_Default: Int](./kaudiosessionmode_default.md)
  The default mode; used unless you set a mode with the [`AudioSessionSetProperty(_:_:_:)`](./audiosessionsetproperty%28_,_,_%29.md) function.
- [var kAudioSessionMode_VoiceChat: Int](./kaudiosessionmode_voicechat.md)
  Specify this mode if your app is performing two-way voice communication, such as using Voice over Internet Protocol (VoIP).
- [var kAudioSessionMode_Measurement: Int](./kaudiosessionmode_measurement.md)
  Specify this mode if your app is performing measurement of incoming audio.
- [var kAudioSessionMode_GameChat: Int](./kaudiosessionmode_gamechat.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionmode_videorecording)*