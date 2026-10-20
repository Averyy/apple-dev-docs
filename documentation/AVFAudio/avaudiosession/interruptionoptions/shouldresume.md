# shouldResume

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

An option that indicates the interruption by another audio session has ended and the app can resume its audio session.

**Availability**:
- iOS 6.0+ - Deprecated in 27.0
- iPadOS 6.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 2.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAudioSessionResumptionRecommendationNotification instead

## Declaration

```swift
static var shouldResume: AVAudioSession.InterruptionOptions { get }
```

```c
AVAudioSessionInterruptionOptionShouldResume
```

#### Discussion

If the interruption type is [`AVAudioSession.InterruptionType.ended`](../interruptiontype/ended.md), check for this value in the [`AVAudioSessionInterruptionOptionKey`](../../avaudiosessioninterruptionoptionkey.md) key in the `userInfo` dictionary of the [`interruptionNotification`](../interruptionnotification.md) notification. It serves as a hint that it’s appropriate for your app to resume audio playback without waiting for user input.

Apps that don’t require user input to begin audio playback (such as games) can ignore this flag and resume playback when an interruption ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/interruptionoptions/shouldresume)*