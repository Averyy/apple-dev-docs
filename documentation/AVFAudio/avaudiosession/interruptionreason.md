# AVAudioSession.InterruptionReason

**Framework**: AVFAudio  
**Kind**: enum

Constants that define the reasons for an audio session interruption.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum InterruptionReason
```

## Topics

### Interruption Reasons
- [AVAudioSession.InterruptionReason.default](avaudiosession/interruptionreason/default.md)
  The system interrupts this audio session when it activates another.
- [AVAudioSession.InterruptionReason.builtInMicMuted](avaudiosession/interruptionreason/builtinmicmuted.md)
  The system interrupts the audio session when the device mutes the built-in microphone.
- [AVAudioSession.InterruptionReason.routeDisconnected](avaudiosession/interruptionreason/routedisconnected.md)
  The system interrupts the audio session due to a disconnection of an audio route.
- [AVAudioSession.InterruptionReason.appWasSuspended](avaudiosession/interruptionreason/appwassuspended.md)
  The system suspends the app and interrupts the audio session.
- [AVAudioSession.InterruptionReason.sceneWasBackgrounded](avaudiosession/interruptionreason/scenewasbackgrounded.md)
  The system backgrounds the scene and interrupts the audio session.
### Initializers
- [init?(rawValue: UInt)](avaudiosession/interruptionreason/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [AVAudioSession.InterruptionType](avaudiosession/interruptiontype.md)
  Constants that describe the type of an audio interruption.
- [AVAudioSession.InterruptionOptions](avaudiosession/interruptionoptions.md)
  Constants that indicate the state of an audio session after an interruption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/interruptionreason)*