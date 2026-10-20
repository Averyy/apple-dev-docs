# kAudioSessionMode_Default

**Framework**: Audio Toolbox  
**Kind**: var  
**Role**: Global Variable

The default mode; used unless you set a mode with the [`AudioSessionSetProperty(_:_:_:)`](./audiosessionsetproperty%28_,_,_%29.md) function.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

> **Deprecated**: Deprecated in iOS 7.0.

## Declaration

```swift
var kAudioSessionMode_Default: Int { get }
```

```c
kAudioSessionMode_Default
```

#### Discussion

When this mode is in use, audio session behavior matches that of iOS versions prior to iOS 5.0. You can use this mode with every audio session category. On devices with more than one built-in microphone, the primary microphone is used.

This mode is equivalent to the [`default`](../AVFAudio/avaudiosession/mode-swift.struct/default.md) mode provided in the AVFoundation framework.

## See Also

### Constants
- [var kAudioSessionMode_VoiceChat: Int](./kaudiosessionmode_voicechat.md)
  Specify this mode if your app is performing two-way voice communication, such as using Voice over Internet Protocol (VoIP).
- [var kAudioSessionMode_VideoRecording: Int](./kaudiosessionmode_videorecording.md)
  Specify this mode if your app is recording a movie.
- [var kAudioSessionMode_Measurement: Int](./kaudiosessionmode_measurement.md)
  Specify this mode if your app is performing measurement of incoming audio.
- [var kAudioSessionMode_GameChat: Int](./kaudiosessionmode_gamechat.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionmode_default)*