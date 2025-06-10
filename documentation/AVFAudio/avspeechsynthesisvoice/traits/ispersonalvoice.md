# isPersonalVoice

**Framework**: AVFAudio  
**Kind**: property

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

#### Discussion

A user generates and owns a personal voice.

> **Note**:  The system only makes personal voices available when [`personalVoiceAuthorizationStatus`](avspeechsynthesizer/personalvoiceauthorizationstatus-swift.type.property.md) is [`AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus.authorized`](avspeechsynthesizer/personalvoiceauthorizationstatus-swift.enum/authorized.md).

## See Also

- [static var isNoveltyVoice: AVSpeechSynthesisVoice.Traits](avspeechsynthesisvoice/traits/isnoveltyvoice.md)
  The trait that indicates a voice is a novelty voice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisvoice/traits/ispersonalvoice)*