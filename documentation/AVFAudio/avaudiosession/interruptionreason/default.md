# AVAudioSession.InterruptionReason.default

**Framework**: AVFAudio  
**Kind**: case  
**Role**: Case

The system interrupts this audio session when it activates another.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case `default`
```

```c
AVAudioSessionInterruptionReasonDefault
```

## See Also

### Identifying interruption reasons
- [AVAudioSession.InterruptionReason.builtInMicMuted](./builtinmicmuted.md)
  The system interrupts the audio session when the device mutes the built-in microphone.
- [AVAudioSession.InterruptionReason.routeDisconnected](./routedisconnected.md)
  The system interrupts the audio session due to a disconnection of an audio route.
- [AVAudioSession.InterruptionReason.sceneWasBackgrounded](./scenewasbackgrounded.md)
  The system backgrounds the scene and interrupts the audio session.
- [AVAudioSession.InterruptionReason.appWasSuspended](./appwassuspended.md)
  The system suspends the app and interrupts the audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/interruptionreason/default)*