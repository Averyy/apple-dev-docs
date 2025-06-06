# AVAudioSession.InterruptionReason.builtInMicMuted

**Framework**: AVFAudio  
**Kind**: case

The system interrupts the audio session when the device mutes the built-in microphone.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case builtInMicMuted
```

#### Discussion

This interruption reason typically occurs when a user closes an iPad’s Smart Folio cover.

## See Also

- [AVAudioSession.InterruptionReason.default](avaudiosession/interruptionreason/default.md)
  The system interrupts this audio session when it activates another.
- [AVAudioSession.InterruptionReason.routeDisconnected](avaudiosession/interruptionreason/routedisconnected.md)
  The system interrupts the audio session due to a disconnection of an audio route.
- [AVAudioSession.InterruptionReason.appWasSuspended](avaudiosession/interruptionreason/appwassuspended.md)
  The system suspends the app and interrupts the audio session.
- [AVAudioSession.InterruptionReason.sceneWasBackgrounded](avaudiosession/interruptionreason/scenewasbackgrounded.md)
  The system backgrounds the scene and interrupts the audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/interruptionreason/builtinmicmuted)*