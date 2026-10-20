# AVSpeechSynthesisVoiceGender

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

The gender for a voice.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum AVSpeechSynthesisVoiceGender
```

```c
enum AVSpeechSynthesisVoiceGender : NSInteger;
```

## Topics

### Creating a voice gender
- [init?(rawValue: Int)](./avspeechsynthesisvoicegender/init%28rawvalue%29.md)
### Identifying voice genders
- [AVSpeechSynthesisVoiceGender.unspecified](./avspeechsynthesisvoicegender/unspecified.md)
  The nonspecific gender option.
- [AVSpeechSynthesisVoiceGender.male](./avspeechsynthesisvoicegender/male.md)
  The male voice option.
- [AVSpeechSynthesisVoiceGender.female](./avspeechsynthesisvoicegender/female.md)
  The female voice option.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Inspecting voices
- [var identifier: String](./avspeechsynthesisvoice/identifier.md)
  The unique identifier of a voice.
- [var name: String](./avspeechsynthesisvoice/name.md)
  The name of a voice.
- [var quality: AVSpeechSynthesisVoiceQuality](./avspeechsynthesisvoice/quality.md)
  The speech quality of a voice.
- [var gender: AVSpeechSynthesisVoiceGender](./avspeechsynthesisvoice/gender.md)
  The gender for a voice.
- [var voiceTraits: AVSpeechSynthesisVoice.Traits](./avspeechsynthesisvoice/voicetraits.md)
  The traits of a voice.
- [var audioFileSettings: [String : Any]](./avspeechsynthesisvoice/audiofilesettings.md)
  A dictionary that contains audio file settings.
- [enum AVSpeechSynthesisVoiceQuality](./avspeechsynthesisvoicequality.md)
  The speech quality of a voice.
- [AVSpeechSynthesisVoice.Traits](./avspeechsynthesisvoice/traits.md)
  Traits that describe a voice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisvoicegender)*