# measurement

**Framework**: AVFAudio  
**Kind**: property

A mode that indicates that your app is performing measurement of audio input or output.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let measurement: AVAudioSession.Mode
```

#### Discussion

Use this mode for apps that need to minimize the amount of system-supplied signal processing to input and output signals. If recording on devices with more than one built-in microphone, the session uses the primary microphone.

For use with the [`playback`](avaudiosession/category-swift.struct/playback.md), [`record`](avaudiosession/category-swift.struct/record.md), or [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) audio session categories.

> ❗ **Important**:  This mode disables some dynamics processing on input and output signals, resulting in a lower-output playback level.

 This mode disables some dynamics processing on input and output signals, resulting in a lower-output playback level.

## See Also

- [static let `default`: AVAudioSession.Mode](avaudiosession/mode-swift.struct/default.md)
  The default audio session mode.
- [static let gameChat: AVAudioSession.Mode](avaudiosession/mode-swift.struct/gamechat.md)
  A mode that the GameKit framework sets on behalf of an application that uses GameKit’s voice chat service.
- [static let moviePlayback: AVAudioSession.Mode](avaudiosession/mode-swift.struct/movieplayback.md)
  A mode that indicates that your app is playing back movie content.
- [static let spokenAudio: AVAudioSession.Mode](avaudiosession/mode-swift.struct/spokenaudio.md)
  A mode used for continuous spoken audio to pause the audio when another app plays a short audio prompt.
- [static let videoChat: AVAudioSession.Mode](avaudiosession/mode-swift.struct/videochat.md)
  A mode that indicates that your app is engaging in online video conferencing.
- [static let videoRecording: AVAudioSession.Mode](avaudiosession/mode-swift.struct/videorecording.md)
  A mode that indicates that your app is recording a movie.
- [static let voiceChat: AVAudioSession.Mode](avaudiosession/mode-swift.struct/voicechat.md)
  A mode that indicates that your app is performing two-way voice communication, such as using Voice over Internet Protocol (VoIP).
- [static let voicePrompt: AVAudioSession.Mode](avaudiosession/mode-swift.struct/voiceprompt.md)
  A mode that indicates that your app plays audio using text-to-speech.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/mode-swift.struct/measurement)*