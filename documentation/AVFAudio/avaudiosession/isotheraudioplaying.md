# isOtherAudioPlaying

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, getter=isOtherAudioPlaying) BOOL otherAudioPlaying;
```

## Discussion

This property returns [`true`](../../Swift/true.md) if any other audio is playing, including audio from an app using the [`ambient`](./category-swift.struct/ambient.md) category. Most apps should instead use the [`secondaryAudioShouldBeSilencedHint`](./secondaryaudioshouldbesilencedhint.md) property, because it’s more restrictive when considering whether primary audio from another app is playing.

## See Also

### Mixing with other audio
- [var secondaryAudioShouldBeSilencedHint: Bool](./secondaryaudioshouldbesilencedhint.md)
  A Boolean value that indicates whether another app, with a nonmixable audio session, is playing audio.
- [class let silenceSecondaryAudioHintNotification: NSNotification.Name](./silencesecondaryaudiohintnotification.md)
  A notification the system posts when the primary audio from other apps starts and stops.
- [var allowHapticsAndSystemSoundsDuringRecording: Bool](./allowhapticsandsystemsoundsduringrecording.md)
  A Boolean value that indicates whether system sounds and haptics play while recording from audio input.
- [func setAllowHapticsAndSystemSoundsDuringRecording(Bool) throws](./setallowhapticsandsystemsoundsduringrecording%28_%29.md)
  Sets a Boolean value that indicates whether system sounds and haptics play while recording from audio input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/isotheraudioplaying)*