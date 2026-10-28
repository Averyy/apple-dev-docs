# interruptionNotification

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

A notification the system posts when an audio interruption occurs.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 2.0+

> **Deprecated**: Use AVAudioSessionDidBecomeInactiveNotification and AVAudioSessionResumptionRecommendationNotification instead

## Declaration

```swift
class let interruptionNotification: NSNotification.Name
```

```c
extern NSNotificationName const AVAudioSessionInterruptionNotification;
```

## Mentions

- [Handling audio interruptions](../handling-audio-interruptions.md)

## Discussion

The notification’s user-information dictionary contains the [`AVAudioSessionInterruptionTypeKey`](../avaudiosessioninterruptiontypekey.md) key. If the interruption type is [`AVAudioSession.InterruptionType.began`](./interruptiontype/began.md), the system interrupted your app’s audio session and it’s no longer active. If the interruption type is [`AVAudioSession.InterruptionType.ended`](./interruptiontype/ended.md), this dictionary also contains the [`AVAudioSessionInterruptionOptionKey`](../avaudiosessioninterruptionoptionkey.md) key.

See [Handling audio interruptions](../handling-audio-interruptions.md) for more information on using this notification.

The system posts this notification on the main thread.

> **Note**:  Starting in iOS 10, the system deactivates an app’s audio session when it suspends the app process. When the app starts running again, it receives an interruption notification that the system has deactivated its audio session. This notification is necessarily delayed in time because the system can only deliver it once the app is running again. If the system suspended your app’s audio session for this reason, the user-information dictionary contains the [`AVAudioSessionInterruptionWasSuspendedKey`](../avaudiosessioninterruptionwassuspendedkey.md) key with a value of [`true`](../../Swift/true.md).
>
> If you configured your audio session to be nonmixable (the default behavior for the [`playback`](./category-swift.struct/playback.md), [`playAndRecord`](./category-swift.struct/playandrecord.md), [`soloAmbient`](./category-swift.struct/soloambient.md), and [`multiRoute`](./category-swift.struct/multiroute.md) categories), deactivate your audio session if you’re not actively using audio when you go into the background. Doing so avoids having your audio session deactivated by the system (and receiving this somewhat confusing notification).

## Topics

### User info keys
- [let AVAudioSessionInterruptionTypeKey: String](../avaudiosessioninterruptiontypekey.md)
  A user info key to retrieve the interruption type.
- [let AVAudioSessionInterruptionOptionKey: String](../avaudiosessioninterruptionoptionkey.md)
  A user info key to retrieve the interruption option.
- [let AVAudioSessionInterruptionReasonKey: String](../avaudiosessioninterruptionreasonkey.md)
  A user info key to retrieve the interruption reason.
- [let AVAudioSessionInterruptionWasSuspendedKey: String](../avaudiosessioninterruptionwassuspendedkey.md)
  A user info key used to determine if the interruption is due to the audio session being deactivated when the system suspended the app.
### User info values
- [AVAudioSession.InterruptionType](./interruptiontype.md)
  Constants that describe the type of an audio interruption.
- [AVAudioSession.InterruptionOptions](./interruptionoptions.md)
  Constants that indicate the state of an audio session after an interruption.
- [AVAudioSession.InterruptionReason](./interruptionreason.md)
  Constants that define the reasons for an audio session interruption.

## See Also

### Handling interruptions
- [var prefersNoInterruptionsFromSystemAlerts: Bool](./prefersnointerruptionsfromsystemalerts.md)
  A Boolean value that indicates a preference for not interrupting the session with system alerts.
- [func setPrefersNoInterruptionsFromSystemAlerts(Bool) throws](./setprefersnointerruptionsfromsystemalerts%28_%29.md)
  Sets the preference for not interrupting the audio session with system alerts.
- [var prefersInterruptionOnRouteDisconnect: Bool](./prefersinterruptiononroutedisconnect.md)
  A Boolean value that indicates whether the system interrupts the audio session when the active route disconnects.
- [func setPrefersInterruptionOnRouteDisconnect(Bool) throws](./setprefersinterruptiononroutedisconnect%28_%29.md)
  Sets a preference to interrupt the audio session when the active route disconnects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/interruptionnotification)*