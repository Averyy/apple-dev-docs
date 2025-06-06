# AVAudioSessionInterruptionOptionKey

**Framework**: AVFAudio  
**Kind**: var

A user info key to retrieve the interruption option.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let AVAudioSessionInterruptionOptionKey: String
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing an unsigned integer that identifies any options associated with the interruption. For a list of possible flags, see [`AVAudioSession.InterruptionOptions`](avaudiosession/interruptionoptions.md).

## See Also

- [let AVAudioSessionInterruptionTypeKey: String](avaudiosessioninterruptiontypekey.md)
  A user info key to retrieve the interruption type.
- [let AVAudioSessionInterruptionReasonKey: String](avaudiosessioninterruptionreasonkey.md)
  A user info key to retrieve the interruption reason.
- [let AVAudioSessionInterruptionWasSuspendedKey: String](avaudiosessioninterruptionwassuspendedkey.md)
  A user info key used to determine if the interruption is due to the audio session being deactivated when the system suspended the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessioninterruptionoptionkey)*