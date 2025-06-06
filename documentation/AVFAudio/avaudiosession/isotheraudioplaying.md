# isOtherAudioPlaying

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that indicates whether another app is playing audio.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isOtherAudioPlaying: Bool { get }
```

#### Discussion

This property returns [`true`](https://developer.apple.com/documentation/swift/true) if any other audio is playing, including audio from an app using the [`ambient`](avaudiosession/category-swift.struct/ambient.md) category. Most apps should instead use the [`secondaryAudioShouldBeSilencedHint`](avaudiosession/secondaryaudioshouldbesilencedhint.md) property, because it’s more restrictive when considering whether primary audio from another app is playing.

## See Also

- [var secondaryAudioShouldBeSilencedHint: Bool](avaudiosession/secondaryaudioshouldbesilencedhint.md)
  A Boolean value that indicates whether another app, with a nonmixable audio session, is playing audio.
- [class let silenceSecondaryAudioHintNotification: NSNotification.Name](avaudiosession/silencesecondaryaudiohintnotification.md)
  A notification the system posts when the primary audio from other apps starts and stops.
- [var allowHapticsAndSystemSoundsDuringRecording: Bool](avaudiosession/allowhapticsandsystemsoundsduringrecording.md)
  A Boolean value that indicates whether system sounds and haptics play while recording from audio input.
- [func setAllowHapticsAndSystemSoundsDuringRecording(Bool) throws](avaudiosession/setallowhapticsandsystemsoundsduringrecording(_:).md)
  Sets a Boolean value that indicates whether system sounds and haptics play while recording from audio input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/isotheraudioplaying)*