# AVAudioSessionInterruptionOptionKey

**Framework**: AVFAudio  
**Kind**: var  
**Role**: Global Variable

A user info key to retrieve the interruption option.

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
let AVAudioSessionInterruptionOptionKey: String
```

```c
extern NSString * const AVAudioSessionInterruptionOptionKey;
```

#### Discussion

The value for this key is an [`NSNumber`](../Foundation/nsnumber.md) object containing an unsigned integer that identifies any options associated with the interruption. For a list of possible flags, see [`AVAudioSession.InterruptionOptions`](./avaudiosession/interruptionoptions.md).

## See Also

### User info keys
- [let AVAudioSessionInterruptionTypeKey: String](./avaudiosessioninterruptiontypekey.md)
  A user info key to retrieve the interruption type.
- [let AVAudioSessionInterruptionReasonKey: String](./avaudiosessioninterruptionreasonkey.md)
  A user info key to retrieve the interruption reason.
- [let AVAudioSessionInterruptionWasSuspendedKey: String](./avaudiosessioninterruptionwassuspendedkey.md)
  A user info key used to determine if the interruption is due to the audio session being deactivated when the system suspended the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessioninterruptionoptionkey)*