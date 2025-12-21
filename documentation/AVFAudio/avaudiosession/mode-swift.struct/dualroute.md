# dualRoute

**Framework**: AVFAudio  
**Kind**: property

A mode that provides simultaneous use of the built-in microphone/speaker and a secondary audio device that supports input and output.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
static let dualRoute: AVAudioSession.Mode
```

#### Discussion

This mode can only be used with the [`multiRoute`](avaudiosession/category-swift.struct/multiroute.md) category. It additionally requires you to set the [`allowBluetoothHFP`](avaudiosession/categoryoptions-swift.struct/allowbluetoothhfp.md) option.

Enabling this mode results in the following behavior:

- The primary audio route is always the built-in microphone/speaker.
- The supported secondary route types are [`headsetMic`](avaudiosession/port/headsetmic.md), [`headphones`](avaudiosession/port/headphones.md), [`bluetoothLE`](avaudiosession/port/bluetoothle.md), and [`bluetoothHFP`](avaudiosession/port/bluetoothhfp.md).
- Only audio routes that support input and output are available for use.
- The hardware volume controls adjusts the volume for both primary and secondary routes.
- The system may engage appropriate signal processing for output routes.

> ❗ **Important**: This API may not be used to enable recordings of others without their awareness.

## See Also

- [static let `default`: AVAudioSession.Mode](avaudiosession/mode-swift.struct/default.md)
  The default audio session mode.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/mode-swift.struct/dualroute)*