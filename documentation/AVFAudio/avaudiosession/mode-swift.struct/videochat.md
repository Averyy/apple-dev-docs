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

Use this mode for video chat apps that use the [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) or [`record`](avaudiosession/category-swift.struct/record.md) categories. When you set this mode, the audio session optimizes the device’s tonal equalization for voice. It also reduces the set of allowable audio routes to only those appropriate for video chat.

Using this mode has the side effect of enabling the [`allowBluetooth`](avaudiosession/categoryoptions-swift.struct/allowbluetooth.md) category option.

For apps that use voice or video chat, also use the Voice-Processing I/O audio unit. The Voice-Processing I/O unit provides several features for VoIP apps, including automatic gain correction, adjustment of voice processing, and muting. See [`Voice-Processing I/O Unit`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MusicAudio/Conceptual/AudioUnitHostingGuide_iOS/UsingSpecificAudioUnits/UsingSpecificAudioUnits.html#//apple_ref/doc/uid/TP40009492-CH17-SW6) for more information.

If an app uses the Voice-Processing I/O audio unit and hasn’t set its mode to one of the chat modes (voice, video, or game), the session sets the [`voiceChat`](avaudiosession/mode-swift.struct/voicechat.md) mode implicitly. On the other hand, if the app had previously set its category to [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) and its mode to [`videoChat`](avaudiosession/mode-swift.struct/videochat.md) or [`gameChat`](avaudiosession/mode-swift.struct/gamechat.md), instantiating the Voice-Processing I/O audio unit doesn’t cause the mode to change.

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
- [static let videoRecording: AVAudioSession.Mode](avaudiosession/mode-swift.struct/videorecording.md)
  A mode that indicates that your app is recording a movie.
- [static let voiceChat: AVAudioSession.Mode](avaudiosession/mode-swift.struct/voicechat.md)
  A mode that indicates that your app is performing two-way voice communication, such as using Voice over Internet Protocol (VoIP).
- [static let voicePrompt: AVAudioSession.Mode](avaudiosession/mode-swift.struct/voiceprompt.md)
  A mode that indicates that your app plays audio using text-to-speech.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/mode-swift.struct/videochat)*