# videoChat

**Framework**: AVFAudio  
**Kind**: property

A mode that indicates that your app is engaging in online video conferencing.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let videoChat: AVAudioSession.Mode
```

#### Discussion

This mode is appropriate for video chat apps that use the [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) or [`record`](avaudiosession/category-swift.struct/record.md) categories. When you set this mode, the session optimizes the device’s tonal equalization for voice and reduces the set of allowed audio routes to only those suitable for video chat. Setting this mode also causes the system to automatically apply the [`allowBluetoothHFP`](avaudiosession/categoryoptions-swift.struct/allowbluetoothhfp.md) and [`defaultToSpeaker`](avaudiosession/categoryoptions-swift.struct/defaulttospeaker.md) category options.

VoIP apps should also use the [`Audio Unit Voice I/O`](https://developer.apple.com/documentation/AudioToolbox/audio-unit-voice-i-o) as it provides useful voice features, including automatic gain correction, adjustment of voice processing, and muting. When an app uses this Audio Unit without explicitly setting its mode to a chat variant (voice, video, or game), the session sets the [`voiceChat`](avaudiosession/mode-swift.struct/voicechat.md) mode implicitly. However, if an app previously set its category to [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) and mode to [`videoChat`](avaudiosession/mode-swift.struct/videochat.md) or [`gameChat`](avaudiosession/mode-swift.struct/gamechat.md), instantiating the Audio Unit doesn’t cause the mode to change.

For apps that use one or more chat modes (voice, video, or game), but don’t use [`Audio Unit Voice I/O`](https://developer.apple.com/documentation/AudioToolbox/audio-unit-voice-i-o) or [`AVAudioEngine`](avaudioengine.md) with [`setVoiceProcessingEnabled(_:)`](avaudioionode/setvoiceprocessingenabled(_:).md), the system reduces the processing it applies to audio signals. Specifically, it doesn’t apply voice-specific processing, like echo cancellation and automatic gain correction, and disables dynamic processing on input and output, which results in a lower playback level.

## See Also

- [static let `default`: AVAudioSession.Mode](avaudiosession/mode-swift.struct/default.md)
  The default audio session mode.
- [static let dualRoute: AVAudioSession.Mode](avaudiosession/mode-swift.struct/dualroute.md)
  A mode that provides simultaneous use of the built-in microphone/speaker and a secondary audio device that supports input and output.
- [static let gameChat: AVAudioSession.Mode](avaudiosession/mode-swift.struct/gamechat.md)
  A mode that the GameKit framework sets on behalf of an application that uses GameKit’s voice chat service.
- [static let measurement: AVAudioSession.Mode](avaudiosession/mode-swift.struct/measurement.md)
  A mode that indicates that your app is performing measurement of audio input or output.
- [static let moviePlayback: AVAudioSession.Mode](avaudiosession/mode-swift.struct/movieplayback.md)
  A mode that indicates that your app is playing back movie content.
- [static let shortFormVideo: AVAudioSession.Mode](avaudiosession/mode-swift.struct/shortformvideo.md)
  Appropriate for applications playing short-form video content.
- [static let spokenAudio: AVAudioSession.Mode](avaudiosession/mode-swift.struct/spokenaudio.md)
  A mode used for continuous spoken audio to pause the audio when another app plays a short audio prompt.
- [static let videoRecording: AVAudioSession.Mode](avaudiosession/mode-swift.struct/videorecording.md)
  A mode that indicates that your app is recording a movie.
- [static let voiceChat: AVAudioSession.Mode](avaudiosession/mode-swift.struct/voicechat.md)
  A mode that indicates that your app is performing two-way voice communication, such as using Voice over Internet Protocol (VoIP).
- [static let voicePrompt: AVAudioSession.Mode](avaudiosession/mode-swift.struct/voiceprompt.md)
  A mode that indicates that your app plays audio using text-to-speech.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/mode-swift.struct/videochat)*