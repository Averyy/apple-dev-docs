# AVAudioSession.InterruptionReason.routeDisconnected

**Framework**: AVFAudio  
**Kind**: case  
**Role**: Case

The system interrupts the audio session due to a disconnection of an audio route.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
case routeDisconnected
```

```c
AVAudioSessionInterruptionReasonRouteDisconnected
```

## See Also

### Identifying interruption reasons
- [AVAudioSession.InterruptionReason.default](./default.md)
  The system interrupts this audio session when it activates another.
- [AVAudioSession.InterruptionReason.builtInMicMuted](./builtinmicmuted.md)
  The system interrupts the audio session when the device mutes the built-in microphone.
- [AVAudioSession.InterruptionReason.sceneWasBackgrounded](./scenewasbackgrounded.md)
  The system backgrounds the scene and interrupts the audio session.
- [AVAudioSession.InterruptionReason.appWasSuspended](./appwassuspended.md)
  The system suspends the app and interrupts the audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/interruptionreason/routedisconnected)*