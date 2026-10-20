# measurement

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

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

```c
extern AVAudioSessionMode const AVAudioSessionModeMeasurement;
```

#### Discussion

Use this mode for apps that need to minimize the amount of system-supplied signal processing to input and output signals. If recording on devices with more than one built-in microphone, the session uses the primary microphone.

For use with the [`playback`](../category-swift.struct/playback.md), [`record`](../category-swift.struct/record.md), or [`playAndRecord`](../category-swift.struct/playandrecord.md) audio session categories.

> ❗ **Important**:  This mode disables some dynamics processing on input and output signals, resulting in a lower-output playback level.

## See Also

### Getting standard session modes
- [static let `default`: AVAudioSession.Mode](./default.md)
  The default audio session mode.
- [static let dualRoute: AVAudioSession.Mode](./dualroute.md)
  A mode that provides simultaneous use of the built-in microphone/speaker and a secondary audio device that supports input and output.
- [static let gameChat: AVAudioSession.Mode](./gamechat.md)
  A mode that the GameKit framework sets on behalf of an application that uses GameKit’s voice chat service.
- [static let moviePlayback: AVAudioSession.Mode](./movieplayback.md)
  A mode that indicates that your app is playing back movie content.
- [static let shortFormVideo: AVAudioSession.Mode](./shortformvideo.md)
  Appropriate for applications playing short-form video content.
- [static let spokenAudio: AVAudioSession.Mode](./spokenaudio.md)
  A mode used for continuous spoken audio to pause the audio when another app plays a short audio prompt.
- [static let videoChat: AVAudioSession.Mode](./videochat.md)
  A mode that indicates that your app is engaging in online video conferencing.
- [static let videoRecording: AVAudioSession.Mode](./videorecording.md)
  A mode that indicates that your app is recording a movie.
- [static let voiceChat: AVAudioSession.Mode](./voicechat.md)
  A mode that indicates that your app is performing two-way voice communication, such as using Voice over Internet Protocol (VoIP).
- [static let voicePrompt: AVAudioSession.Mode](./voiceprompt.md)
  A mode that indicates that your app plays audio using text-to-speech.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/mode-swift.struct/measurement)*