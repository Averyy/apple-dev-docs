# secondaryAudioShouldBeSilencedHint

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) BOOL secondaryAudioShouldBeSilencedHint;
```

## Discussion

Use this property as a hint to silence audio that’s secondary to the functionality of the app. For example, in a game that uses the [`ambient`](./category-swift.struct/ambient.md) category, you can use this property to mute the soundtrack while leaving sound effects unmuted.

## See Also

### Mixing with other audio
- [var isOtherAudioPlaying: Bool](./isotheraudioplaying.md)
  A Boolean value that indicates whether another app is playing audio.
- [class let silenceSecondaryAudioHintNotification: NSNotification.Name](./silencesecondaryaudiohintnotification.md)
  A notification the system posts when the primary audio from other apps starts and stops.
- [var allowHapticsAndSystemSoundsDuringRecording: Bool](./allowhapticsandsystemsoundsduringrecording.md)
  A Boolean value that indicates whether system sounds and haptics play while recording from audio input.
- [func setAllowHapticsAndSystemSoundsDuringRecording(Bool) throws](./setallowhapticsandsystemsoundsduringrecording%28_%29.md)
  Sets a Boolean value that indicates whether system sounds and haptics play while recording from audio input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/secondaryaudioshouldbesilencedhint)*