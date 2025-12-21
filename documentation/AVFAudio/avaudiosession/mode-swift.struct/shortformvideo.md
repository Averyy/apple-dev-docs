# shortFormVideo

**Framework**: AVFAudio  
**Kind**: property

Appropriate for applications playing short-form video content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
static let shortFormVideo: AVAudioSession.Mode
```

#### Discussion

Only valid with [`playback`](avaudiosession/category-swift.struct/playback.md). Not applicable with [`AVAudioSession.RouteSharingPolicy.longFormAudio`](avaudiosession/routesharingpolicy-swift.enum/longformaudio.md), or [`AVAudioSession.RouteSharingPolicy.longFormVideo`](avaudiosession/routesharingpolicy-swift.enum/longformvideo.md).

When this mode is set:

- system will make informed decisions to automatically unmute the output of the media if the user shows intention of unmuting. - When auto-unmuted, [`userIntentToUnmuteOutputNotification`](avaudiosession/userintenttounmuteoutputnotification.md) and [`outputMuteStateChangeNotification`](avaudiosession/outputmutestatechangenotification.md) will be sent.
- if the session is output muted, system may prevent interrupting other active audio apps.

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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/mode-swift.struct/shortformvideo)*