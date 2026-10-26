# AVAudioSession.InterruptionReason

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Constants that define the reasons for an audio session interruption.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum InterruptionReason
```

```c
enum AVAudioSessionInterruptionReason : NSUInteger;
```

## Topics

### Creating an interruption reason
- [init?(rawValue: UInt)](./interruptionreason/init%28rawvalue%29.md)
### Identifying interruption reasons
- [AVAudioSession.InterruptionReason.default](./interruptionreason/default.md)
  The system interrupts this audio session when it activates another.
- [AVAudioSession.InterruptionReason.builtInMicMuted](./interruptionreason/builtinmicmuted.md)
  The system interrupts the audio session when the device mutes the built-in microphone.
- [AVAudioSession.InterruptionReason.routeDisconnected](./interruptionreason/routedisconnected.md)
  The system interrupts the audio session due to a disconnection of an audio route.
- [AVAudioSession.InterruptionReason.sceneWasBackgrounded](./interruptionreason/scenewasbackgrounded.md)
  The system backgrounds the scene and interrupts the audio session.
- [AVAudioSession.InterruptionReason.appWasSuspended](./interruptionreason/appwassuspended.md)
  The system suspends the app and interrupts the audio session.
- [AVAudioSessionInterruptionReasonDeviceUnauthenticated](../avaudiosessioninterruptionreason/avaudiosessioninterruptionreasondeviceunauthenticated.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### User info values
- [AVAudioSession.InterruptionType](./interruptiontype.md)
  Constants that describe the type of an audio interruption.
- [AVAudioSession.InterruptionOptions](./interruptionoptions.md)
  Constants that indicate the state of an audio session after an interruption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/interruptionreason)*