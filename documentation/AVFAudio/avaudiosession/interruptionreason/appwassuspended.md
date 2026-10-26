# AVAudioSession.InterruptionReason.appWasSuspended

**Framework**: AVFAudio  
**Kind**: case  
**Role**: Case

The system suspends the app and interrupts the audio session.

**Availability**:
- iOS 14.5+ - Deprecated in 16.0
- iPadOS 14.5+ - Deprecated in 16.0
- Mac Catalyst 14.5+ - Deprecated in 16.0
- tvOS 14.5+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 7.4+ - Deprecated in 9.0

> **Deprecated**: wasSuspended reason no longer present

## Declaration

```swift
case appWasSuspended
```

```c
AVAudioSessionInterruptionReasonAppWasSuspended
```

#### Discussion

Starting in iOS 10, the system deactivates the audio session of most apps when it suspends the app process. The next time the app runs, it receives a notification that the system deactivated its audio session. This notification is necessarily delayed in time, because the system can’t send it until the app restarts.

## See Also

### Identifying interruption reasons
- [AVAudioSession.InterruptionReason.default](./default.md)
  The system interrupts this audio session when it activates another.
- [AVAudioSession.InterruptionReason.builtInMicMuted](./builtinmicmuted.md)
  The system interrupts the audio session when the device mutes the built-in microphone.
- [AVAudioSession.InterruptionReason.routeDisconnected](./routedisconnected.md)
  The system interrupts the audio session due to a disconnection of an audio route.
- [AVAudioSession.InterruptionReason.sceneWasBackgrounded](./scenewasbackgrounded.md)
  The system backgrounds the scene and interrupts the audio session.
- [AVAudioSessionInterruptionReasonDeviceUnauthenticated](../../avaudiosessioninterruptionreason/avaudiosessioninterruptionreasondeviceunauthenticated.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/interruptionreason/appwassuspended)*