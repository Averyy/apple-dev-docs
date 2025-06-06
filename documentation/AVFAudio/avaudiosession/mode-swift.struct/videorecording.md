# videoRecording

**Framework**: AVFAudio  
**Kind**: property

A mode that indicates that your app is recording a movie.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let videoRecording: AVAudioSession.Mode
```

#### Discussion

This mode is valid only with the [`record`](avaudiosession/category-swift.struct/record.md) and [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) audio session categories. On devices with more than one built-in microphone, the audio session uses the microphone closest to the video camera.

Use this mode to ensure that the system provides appropriate audio-signal processing.

Use [`AVCaptureSession`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession) in conjunction with the video recording mode for greater control of input and output routes. For example, setting the [`automaticallyConfiguresApplicationAudioSession`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession/automaticallyConfiguresApplicationAudioSession) property results in the session automatically choosing the best input route for the device and camera used.

## See Also

- [static let `default`: AVAudioSession.Mode](avaudiosession/mode-swift.struct/default.md)
  The default audio session mode.
- [static let gameChat: AVAudioSession.Mode](avaudiosession/mode-swift.struct/gamechat.md)
  A mode that the GameKit framework sets on behalf of an application that uses GameKit’s voice chat service.
- [static let measurement: AVAudioSession.Mode](avaudiosession/mode-swift.struct/measurement.md)
  A mode that indicates that your app is performing measurement of audio input or output.
- [static let moviePlayback: AVAudioSession.Mode](avaudiosession/mode-swift.struct/movieplayback.md)
  A mode that indicates that your app is playing back movie content.
- [static let spokenAudio: AVAudioSession.Mode](avaudiosession/mode-swift.struct/spokenaudio.md)
  A mode used for continuous spoken audio to pause the audio when another app plays a short audio prompt.
- [static let videoChat: AVAudioSession.Mode](avaudiosession/mode-swift.struct/videochat.md)
  A mode that indicates that your app is engaging in online video conferencing.
- [static let voiceChat: AVAudioSession.Mode](avaudiosession/mode-swift.struct/voicechat.md)
  A mode that indicates that your app is performing two-way voice communication, such as using Voice over Internet Protocol (VoIP).
- [static let voicePrompt: AVAudioSession.Mode](avaudiosession/mode-swift.struct/voiceprompt.md)
  A mode that indicates that your app plays audio using text-to-speech.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/mode-swift.struct/videorecording)*