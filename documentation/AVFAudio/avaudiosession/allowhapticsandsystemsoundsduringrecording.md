# allowHapticsAndSystemSoundsDuringRecording

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) BOOL allowHapticsAndSystemSoundsDuringRecording;
```

#### Discussion

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Mixing with other audio
- [var isOtherAudioPlaying: Bool](./isotheraudioplaying.md)
  A Boolean value that indicates whether another app is playing audio.
- [var secondaryAudioShouldBeSilencedHint: Bool](./secondaryaudioshouldbesilencedhint.md)
  A Boolean value that indicates whether another app, with a nonmixable audio session, is playing audio.
- [class let silenceSecondaryAudioHintNotification: NSNotification.Name](./silencesecondaryaudiohintnotification.md)
  A notification the system posts when the primary audio from other apps starts and stops.
- [func setAllowHapticsAndSystemSoundsDuringRecording(Bool) throws](./setallowhapticsandsystemsoundsduringrecording%28_%29.md)
  Sets a Boolean value that indicates whether system sounds and haptics play while recording from audio input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/allowhapticsandsystemsoundsduringrecording)*