# spokenAudio

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

A mode used for continuous spoken audio to pause the audio when another app plays a short audio prompt.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let spokenAudio: AVAudioSession.Mode
```

```c
extern AVAudioSessionMode const AVAudioSessionModeSpokenAudio;
```

## Discussion

This mode is appropriate for apps that play continuous spoken audio, such as podcasts or audio books. Setting this mode indicates that your app should pause, rather than duck, its audio if another app plays a spoken audio prompt. After the interrupting app’s audio ends, you can resume your app’s audio playback.

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
- [static let videoChat: AVAudioSession.Mode](./videochat.md)
  A mode that indicates that your app is engaging in online video conferencing.
- [static let videoRecording: AVAudioSession.Mode](./videorecording.md)
  A mode that indicates that your app is recording a movie.
- [static let voiceChat: AVAudioSession.Mode](./voicechat.md)
  A mode that indicates that your app is performing two-way voice communication, such as using Voice over Internet Protocol (VoIP).
- [static let voicePrompt: AVAudioSession.Mode](./voiceprompt.md)
  A mode that indicates that your app plays audio using text-to-speech.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/mode-swift.struct/spokenaudio)*