# AVAudioSessionInterruptionWasSuspendedKey

**Framework**: AVFAudio  
**Kind**: var  
**Role**: Global Variable

A user info key used to determine if the interruption is due to the audio session being deactivated when the system suspended the app.

**Availability**:
- iOS 10.3+ - Deprecated in 14.5
- iPadOS 10.3+ - Deprecated in 14.5
- Mac Catalyst 13.1+ - Deprecated in 14.5
- macOS
- tvOS 10.3+ - Deprecated in 14.5
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 7.3

> **Deprecated**: Use [`AVAudioSessionInterruptionReasonKey`](./avaudiosessioninterruptionreasonkey.md) instead.

## Declaration

```swift
let AVAudioSessionInterruptionWasSuspendedKey: String
```

```c
extern NSString * const AVAudioSessionInterruptionWasSuspendedKey;
```

## Discussion

This [`userInfo`](../Foundation/nsnotification/userinfo.md) key is present only in [`AVAudioSession.InterruptionType.began`](./avaudiosession/interruptiontype/began.md) interruption events, where the interruption is a direct result of the operating system suspending the app. Its associated value is a Boolean [`NSNumber`](../Foundation/nsnumber.md), where a [`true`](../Swift/true.md) value indicates that the interruption is due to the system suspending the app, rather than being interrupted by another audio session.

## See Also

### User info keys
- [let AVAudioSessionInterruptionTypeKey: String](./avaudiosessioninterruptiontypekey.md)
  A user info key to retrieve the interruption type.
- [let AVAudioSessionInterruptionOptionKey: String](./avaudiosessioninterruptionoptionkey.md)
  A user info key to retrieve the interruption option.
- [let AVAudioSessionInterruptionReasonKey: String](./avaudiosessioninterruptionreasonkey.md)
  A user info key to retrieve the interruption reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessioninterruptionwassuspendedkey)*