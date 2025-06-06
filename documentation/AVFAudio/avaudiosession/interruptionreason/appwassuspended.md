# AVAudioSession.InterruptionReason.appWasSuspended

**Framework**: AVFAudio  
**Kind**: case

The system suspends the app and interrupts the audio session.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- tvOS 14.5+
- visionOS 1.0+
- watchOS 7.4+

## Declaration

```swift
case appWasSuspended
```

#### Discussion

Starting in iOS 10, the system deactivates the audio session of most apps when it suspends the app process. The next time the app runs, it receives a notification that the system deactivated its audio session. This notification is necessarily delayed in time, because the system can’t send it until the app restarts.

## See Also

- [AVAudioSession.InterruptionReason.default](avaudiosession/interruptionreason/default.md)
  The system interrupts this audio session when it activates another.
- [AVAudioSession.InterruptionReason.builtInMicMuted](avaudiosession/interruptionreason/builtinmicmuted.md)
  The system interrupts the audio session when the device mutes the built-in microphone.
- [AVAudioSession.InterruptionReason.routeDisconnected](avaudiosession/interruptionreason/routedisconnected.md)
  The system interrupts the audio session due to a disconnection of an audio route.
- [AVAudioSession.InterruptionReason.sceneWasBackgrounded](avaudiosession/interruptionreason/scenewasbackgrounded.md)
  The system backgrounds the scene and interrupts the audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/interruptionreason/appwassuspended)*