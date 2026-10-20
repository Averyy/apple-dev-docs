# AVAudioSessionInterruptionReasonKey

**Framework**: AVFAudio  
**Kind**: var  
**Role**: Global Variable

A user info key to retrieve the interruption reason.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- tvOS
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 7.3+

> **Deprecated**: Use AVAudioSessionDeactivationContext.interruptionDetails.reason instead

## Declaration

```swift
let AVAudioSessionInterruptionReasonKey: String
```

```c
extern NSString * const AVAudioSessionInterruptionReasonKey;
```

## See Also

### User info keys
- [let AVAudioSessionInterruptionTypeKey: String](./avaudiosessioninterruptiontypekey.md)
  A user info key to retrieve the interruption type.
- [let AVAudioSessionInterruptionOptionKey: String](./avaudiosessioninterruptionoptionkey.md)
  A user info key to retrieve the interruption option.
- [let AVAudioSessionInterruptionWasSuspendedKey: String](./avaudiosessioninterruptionwassuspendedkey.md)
  A user info key used to determine if the interruption is due to the audio session being deactivated when the system suspended the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessioninterruptionreasonkey)*