# videoRecording

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

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

```c
extern AVAudioSessionMode const AVAudioSessionModeVideoRecording;
```

#### Discussion

This mode is valid only with the [`record`](../category-swift.struct/record.md) and [`playAndRecord`](../category-swift.struct/playandrecord.md) audio session categories. On devices with more than one built-in microphone, the audio session uses the microphone closest to the video camera.

Use this mode to ensure that the system provides appropriate audio-signal processing.

Use [`AVCaptureSession`](../../../AVFoundation/avcapturesession.md) in conjunction with the video recording mode for greater control of input and output routes. For example, setting the [`automaticallyConfiguresApplicationAudioSession`](../../../AVFoundation/avcapturesession/automaticallyconfiguresapplicationaudiosession.md) property results in the session automatically choosing the best input route for the device and camera used.

## See Also

### Getting standard session modes
- [static let `default`: AVAudioSession.Mode](./default.md)
  The default audio session mode.
- [static let dualRoute: AVAudioSession.Mode](./dualroute.md)
  A mode that provides simultaneous use of the built-in microphone/speaker and a secondary audio device that supports input and output.
- [static let gameChat: AVAudioSession.Mode](./gamechat.md)
  A mode that the GameKit framework sets on behalf of an application that uses GameKit’s voice chat service.
- [static let measurement: AVAudioSession.Mode](./measurement.md)
  A mode that indicates that your app is performing measurement of audio input or output.
- [static let moviePlayback: AVAudioSession.Mode](./movieplayback.md)
  A mode that indicates that your app is playing back movie content.
- [static let shortFormVideo: AVAudioSession.Mode](./shortformvideo.md)
  Appropriate for applications playing short-form video content.
- [static let spokenAudio: AVAudioSession.Mode](./spokenaudio.md)
  A mode used for continuous spoken audio to pause the audio when another app plays a short audio prompt.
- [static let videoChat: AVAudioSession.Mode](./videochat.md)
  A mode that indicates that your app is engaging in online video conferencing.
- [static let voiceChat: AVAudioSession.Mode](./voicechat.md)
  A mode that indicates that your app is performing two-way voice communication, such as using Voice over Internet Protocol (VoIP).
- [static let voicePrompt: AVAudioSession.Mode](./voiceprompt.md)
  A mode that indicates that your app plays audio using text-to-speech.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/mode-swift.struct/videorecording)*