# AVAudioSession.Mode

**Framework**: AVFAudio  
**Kind**: struct

Audio session mode identifiers.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct Mode
```

#### Overview

While categories set the base behaviors for your app, you use modes to assign specialized behavior to an audio session category.

> ❗ **Important**:  Specifying a mode that the audio session category doesn’t support, such as setting the [`gameChat`](avaudiosession/mode-swift.struct/gamechat.md) mode for the [`multiRoute`](avaudiosession/category-swift.struct/multiroute.md) category, results in the audio session using the [`default`](avaudiosession/mode-swift.struct/default.md) mode behavior.

## Topics

### Creating a Mode
- [init(rawValue: String)](avaudiosession/mode-swift.struct/init(rawvalue:).md)
  Creates a new instance with the raw value you specify.
### Getting Standard Session Modes
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
- [static let videoChat: AVAudioSession.Mode](avaudiosession/mode-swift.struct/videochat.md)
  A mode that indicates that your app is engaging in online video conferencing.
- [static let videoRecording: AVAudioSession.Mode](avaudiosession/mode-swift.struct/videorecording.md)
  A mode that indicates that your app is recording a movie.
- [static let voiceChat: AVAudioSession.Mode](avaudiosession/mode-swift.struct/voicechat.md)
  A mode that indicates that your app is performing two-way voice communication, such as using Voice over Internet Protocol (VoIP).
- [static let voicePrompt: AVAudioSession.Mode](avaudiosession/mode-swift.struct/voiceprompt.md)
  A mode that indicates that your app plays audio using text-to-speech.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var mode: AVAudioSession.Mode](avaudiosession/mode-swift.property.md)
  The current audio session’s mode.
- [var availableModes: [AVAudioSession.Mode]](avaudiosession/availablemodes.md)
  The audio session modes available on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/mode-swift.struct)*