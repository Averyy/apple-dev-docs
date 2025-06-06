# allowHapticsAndSystemSoundsDuringRecording

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that indicates whether system sounds and haptics play while recording from audio input.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var allowHapticsAndSystemSoundsDuringRecording: Bool { get }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isOtherAudioPlaying: Bool](avaudiosession/isotheraudioplaying.md)
  A Boolean value that indicates whether another app is playing audio.
- [var secondaryAudioShouldBeSilencedHint: Bool](avaudiosession/secondaryaudioshouldbesilencedhint.md)
  A Boolean value that indicates whether another app, with a nonmixable audio session, is playing audio.
- [class let silenceSecondaryAudioHintNotification: NSNotification.Name](avaudiosession/silencesecondaryaudiohintnotification.md)
  A notification the system posts when the primary audio from other apps starts and stops.
- [func setAllowHapticsAndSystemSoundsDuringRecording(Bool) throws](avaudiosession/setallowhapticsandsystemsoundsduringrecording(_:).md)
  Sets a Boolean value that indicates whether system sounds and haptics play while recording from audio input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/allowhapticsandsystemsoundsduringrecording)*