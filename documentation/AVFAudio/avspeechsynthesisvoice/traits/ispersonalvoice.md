# isPersonalVoice

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

The trait that indicates a voice is a personal voice.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static var isPersonalVoice: AVSpeechSynthesisVoice.Traits { get }
```

```c
AVSpeechSynthesisVoiceTraitIsPersonalVoice
```

#### Discussion

A user generates and owns a personal voice.

> **Note**:  The system only makes personal voices available when [`personalVoiceAuthorizationStatus`](../../avspeechsynthesizer/personalvoiceauthorizationstatus-swift.type.property.md) is [`AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus.authorized`](../../avspeechsynthesizer/personalvoiceauthorizationstatus-swift.enum/authorized.md).

## See Also

### Inspecting a voice trait
- [static var isNoveltyVoice: AVSpeechSynthesisVoice.Traits](./isnoveltyvoice.md)
  The trait that indicates a voice is a novelty voice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisvoice/traits/ispersonalvoice)*