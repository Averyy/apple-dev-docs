# AVAudioSession.InterruptionReason.sceneWasBackgrounded

**Framework**: AVFAudio  
**Kind**: case  
**Role**: Case

The system backgrounds the scene and interrupts the audio session.

**Availability**:
- visionOS

## Declaration

```swift
case sceneWasBackgrounded
```

```c
AVAudioSessionInterruptionReasonSceneWasBackgrounded
```

## See Also

### Identifying interruption reasons
- [AVAudioSession.InterruptionReason.default](./default.md)
  The system interrupts this audio session when it activates another.
- [AVAudioSession.InterruptionReason.builtInMicMuted](./builtinmicmuted.md)
  The system interrupts the audio session when the device mutes the built-in microphone.
- [AVAudioSession.InterruptionReason.routeDisconnected](./routedisconnected.md)
  The system interrupts the audio session due to a disconnection of an audio route.
- [AVAudioSession.InterruptionReason.appWasSuspended](./appwassuspended.md)
  The system suspends the app and interrupts the audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/interruptionreason/scenewasbackgrounded)*