# AVSpeechSynthesisVoice.Traits

**Framework**: AVFAudio  
**Kind**: struct  
**Role**: Structure

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

```c
enum AVSpeechSynthesisVoiceTraits : NSUInteger;
```

## Topics

### Creating a voice trait
- [init(rawValue: UInt)](./traits/init%28rawvalue%29.md)
  Creates a voice trait with the corresponding integer that you specify.
### Inspecting a voice trait
- [static var isNoveltyVoice: AVSpeechSynthesisVoice.Traits](./traits/isnoveltyvoice.md)
  The trait that indicates a voice is a novelty voice.
- [static var isPersonalVoice: AVSpeechSynthesisVoice.Traits](./traits/ispersonalvoice.md)
  The trait that indicates a voice is a personal voice.
- [AVSpeechSynthesisVoiceTraitNone](../avspeechsynthesisvoicetraits/avspeechsynthesisvoicetraitnone.md)
  The trait that indicates a voice is a regular voice.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Inspecting voices
- [var identifier: String](./identifier.md)
  The unique identifier of a voice.
- [var name: String](./name.md)
  The name of a voice.
- [var quality: AVSpeechSynthesisVoiceQuality](./quality.md)
  The speech quality of a voice.
- [var gender: AVSpeechSynthesisVoiceGender](./gender.md)
  The gender for a voice.
- [var voiceTraits: AVSpeechSynthesisVoice.Traits](./voicetraits.md)
  The traits of a voice.
- [var audioFileSettings: [String : Any]](./audiofilesettings.md)
  A dictionary that contains audio file settings.
- [enum AVSpeechSynthesisVoiceQuality](../avspeechsynthesisvoicequality.md)
  The speech quality of a voice.
- [enum AVSpeechSynthesisVoiceGender](../avspeechsynthesisvoicegender.md)
  The gender for a voice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisvoice/traits)*