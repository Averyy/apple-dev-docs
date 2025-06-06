# AVAudioSessionInterruptionWasSuspendedKey

**Framework**: AVFAudio  
**Kind**: var

A user info key used to determine if the interruption is due to the audio session being deactivated when the system suspended the app.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS ?+
- tvOS 10.3+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
let AVAudioSessionInterruptionWasSuspendedKey: String
```

#### Discussion

This [`userInfo`](https://developer.apple.com/documentation/foundation/nsnotification/1409222-userinfo) key is present only in [`AVAudioSession.InterruptionType.began`](avaudiosession/interruptiontype/began.md) interruption events, where the interruption is a direct result of the operating system suspending the app. Its associated value is a Boolean [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber), where a [`true`](https://developer.apple.com/documentation/swift/true) value indicates that the interruption is due to the system suspending the app, rather than being interrupted by another audio session.

## See Also

- [let AVAudioSessionInterruptionTypeKey: String](avaudiosessioninterruptiontypekey.md)
  A user info key to retrieve the interruption type.
- [let AVAudioSessionInterruptionOptionKey: String](avaudiosessioninterruptionoptionkey.md)
  A user info key to retrieve the interruption option.
- [let AVAudioSessionInterruptionReasonKey: String](avaudiosessioninterruptionreasonkey.md)
  A user info key to retrieve the interruption reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessioninterruptionwassuspendedkey)*