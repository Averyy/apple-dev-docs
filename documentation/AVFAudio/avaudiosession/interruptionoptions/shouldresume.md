# shouldResume

**Framework**: AVFAudio  
**Kind**: property

An option that indicates the interruption by another audio session has ended and the app can resume its audio session.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static var shouldResume: AVAudioSession.InterruptionOptions { get }
```

#### Discussion

If the interruption type is [`AVAudioSession.InterruptionType.ended`](avaudiosession/interruptiontype/ended.md), check for this value in the [`AVAudioSessionInterruptionOptionKey`](avaudiosessioninterruptionoptionkey.md) key in the `userInfo` dictionary of the [`interruptionNotification`](avaudiosession/interruptionnotification.md) notification. It serves as a hint that it’s appropriate for your app to resume audio playback without waiting for user input.

Apps that don’t require user input to begin audio playback (such as games) can ignore this flag and resume playback when an interruption ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/interruptionoptions/shouldresume)*