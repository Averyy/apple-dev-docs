# voiceChat

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

A mode that indicates that your app is performing two-way voice communication, such as using Voice over Internet Protocol (VoIP).

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let voiceChat: AVAudioSession.Mode
```

```c
extern AVAudioSessionMode const AVAudioSessionModeVoiceChat;
```

## Discussion

This mode is appropriate for Voice over IP (VoIP) apps that use the [`playAndRecord`](../category-swift.struct/playandrecord.md) category. When you set this mode, the session optimizes the device’s tonal equalization for voice and reduces the set of allowed audio routes to only those suitable for voice chat. Setting this mode also causes the system to automatically apply the [`allowBluetoothHFP`](../categoryoptions-swift.struct/allowbluetoothhfp.md) category option.

VoIP apps should also use the [Audio Unit Voice I/O](../../../AudioToolbox/audio-unit-voice-i-o.md) as it provides useful voice features, including automatic gain correction, adjustment of voice processing, and muting. When an app uses this Audio Unit without explicitly setting its mode to a chat variant (voice, video, or game), the session sets the [`voiceChat`](./voicechat.md) mode implicitly. However, if an app previously set its category to [`playAndRecord`](../category-swift.struct/playandrecord.md) and mode to [`videoChat`](./videochat.md) or [`gameChat`](./gamechat.md), instantiating the Audio Unit doesn’t cause the mode to change.

For apps that use one or more chat modes (voice, video, or game), but don’t use [Audio Unit Voice I/O](../../../AudioToolbox/audio-unit-voice-i-o.md) or [`AVAudioEngine`](../../avaudioengine.md) with [`setVoiceProcessingEnabled(_:)`](../../avaudioionode/setvoiceprocessingenabled%28_%29.md), the system reduces the processing it applies to audio signals. Specifically, it doesn’t apply voice-specific processing, like echo cancellation and automatic gain correction, and disables dynamic processing on input and output, which results in a lower playback level.

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
- [static let videoRecording: AVAudioSession.Mode](./videorecording.md)
  A mode that indicates that your app is recording a movie.
- [static let voicePrompt: AVAudioSession.Mode](./voiceprompt.md)
  A mode that indicates that your app plays audio using text-to-speech.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/mode-swift.struct/voicechat)*