# AVSpeechSynthesisVoice.Traits

**Framework**: AVFAudio  
**Kind**: struct

Traits that describe a voice.

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
struct Traits
```

## Topics

### Creating a voice trait
- [init(rawValue: UInt)](avspeechsynthesisvoice/traits/init(rawvalue:).md)
  Creates a voice trait with the corresponding integer that you specify.
### Inspecting a voice trait
- [static var isNoveltyVoice: AVSpeechSynthesisVoice.Traits](avspeechsynthesisvoice/traits/isnoveltyvoice.md)
  The trait that indicates a voice is a novelty voice.
- [static var isPersonalVoice: AVSpeechSynthesisVoice.Traits](avspeechsynthesisvoice/traits/ispersonalvoice.md)
  The trait that indicates a voice is a personal voice.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var identifier: String](avspeechsynthesisvoice/identifier.md)
  The unique identifier of a voice.
- [var name: String](avspeechsynthesisvoice/name.md)
  The name of a voice.
- [var quality: AVSpeechSynthesisVoiceQuality](avspeechsynthesisvoice/quality.md)
  The speech quality of a voice.
- [var gender: AVSpeechSynthesisVoiceGender](avspeechsynthesisvoice/gender.md)
  The gender for a voice.
- [var voiceTraits: AVSpeechSynthesisVoice.Traits](avspeechsynthesisvoice/voicetraits.md)
  The traits of a voice.
- [var audioFileSettings: [String : Any]](avspeechsynthesisvoice/audiofilesettings.md)
  A dictionary that contains audio file settings.
- [enum AVSpeechSynthesisVoiceQuality](avspeechsynthesisvoicequality.md)
  The speech quality of a voice.
- [enum AVSpeechSynthesisVoiceGender](avspeechsynthesisvoicegender.md)
  The gender for a voice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisvoice/traits)*