# kAudioSessionMode_VoiceChat

**Framework**: Audio Toolbox  
**Kind**: var

Specify this mode if your app is performing two-way voice communication, such as using Voice over Internet Protocol (VoIP).

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioSessionMode_VoiceChat: Int { get }
```

#### Discussion

When this mode is in use, the device’s tonal equalization is optimized for voice. For use with the [`kAudioSessionCategory_PlayAndRecord`](kaudiosessioncategory_playandrecord.md) audio session category. On devices with more than one built-in microphone, the primary microphone is used.

Using this mode has the side effect of setting the [`kAudioSessionProperty_OverrideCategoryEnableBluetoothInput`](kaudiosessionproperty_overridecategoryenablebluetoothinput.md) category override to `TRUE`.

This mode is equivalent to the [`voiceChat`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession/Mode-swift.struct/voiceChat) mode provided in the AVFoundation framework.

## See Also

- [var kAudioSessionMode_Default: Int](kaudiosessionmode_default.md)
  The default mode; used unless you set a mode with the [`AudioSessionSetProperty(_:_:_:)`](audiosessionsetproperty(_:_:_:).md) function.
- [var kAudioSessionMode_VideoRecording: Int](kaudiosessionmode_videorecording.md)
  Specify this mode if your app is recording a movie.
- [var kAudioSessionMode_Measurement: Int](kaudiosessionmode_measurement.md)
  Specify this mode if your app is performing measurement of incoming audio.
- [var kAudioSessionMode_GameChat: Int](kaudiosessionmode_gamechat.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionmode_voicechat)*