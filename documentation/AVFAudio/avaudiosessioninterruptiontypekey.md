# AVAudioSessionInterruptionTypeKey

**Framework**: AVFAudio  
**Kind**: var

A user info key to retrieve the interruption type.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let AVAudioSessionInterruptionTypeKey: String
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing an unsigned integer that identifies the type of interruption. For a list of possible values, see [`AVAudioSession.InterruptionType`](avaudiosession/interruptiontype.md).

## See Also

- [let AVAudioSessionInterruptionOptionKey: String](avaudiosessioninterruptionoptionkey.md)
  A user info key to retrieve the interruption option.
- [let AVAudioSessionInterruptionReasonKey: String](avaudiosessioninterruptionreasonkey.md)
  A user info key to retrieve the interruption reason.
- [let AVAudioSessionInterruptionWasSuspendedKey: String](avaudiosessioninterruptionwassuspendedkey.md)
  A user info key used to determine if the interruption is due to the audio session being deactivated when the system suspended the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessioninterruptiontypekey)*