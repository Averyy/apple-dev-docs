# secondaryAudioShouldBeSilencedHint

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that indicates whether another app, with a nonmixable audio session, is playing audio.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var secondaryAudioShouldBeSilencedHint: Bool { get }
```

#### Discussion

Use this property as a hint to silence audio that’s secondary to the functionality of the app. For example, in a game that uses the [`ambient`](avaudiosession/category-swift.struct/ambient.md) category, you can use this property to mute the soundtrack while leaving sound effects unmuted.

## See Also

- [var isOtherAudioPlaying: Bool](avaudiosession/isotheraudioplaying.md)
  A Boolean value that indicates whether another app is playing audio.
- [class let silenceSecondaryAudioHintNotification: NSNotification.Name](avaudiosession/silencesecondaryaudiohintnotification.md)
  A notification the system posts when the primary audio from other apps starts and stops.
- [var allowHapticsAndSystemSoundsDuringRecording: Bool](avaudiosession/allowhapticsandsystemsoundsduringrecording.md)
  A Boolean value that indicates whether system sounds and haptics play while recording from audio input.
- [func setAllowHapticsAndSystemSoundsDuringRecording(Bool) throws](avaudiosession/setallowhapticsandsystemsoundsduringrecording(_:).md)
  Sets a Boolean value that indicates whether system sounds and haptics play while recording from audio input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/secondaryaudioshouldbesilencedhint)*