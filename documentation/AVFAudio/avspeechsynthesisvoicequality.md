# AVSpeechSynthesisVoiceQuality

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

The speech quality of a voice.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum AVSpeechSynthesisVoiceQuality
```

```c
enum AVSpeechSynthesisVoiceQuality : NSInteger;
```

## Topics

### Creating a voice quality
- [init?(rawValue: Int)](./avspeechsynthesisvoicequality/init%28rawvalue%29.md)
### Identifying voice qualities
- [AVSpeechSynthesisVoiceQuality.default](./avspeechsynthesisvoicequality/default.md)
  A basic quality voice that’s  available on the device by default.
- [AVSpeechSynthesisVoiceQuality.enhanced](./avspeechsynthesisvoicequality/enhanced.md)
  An enhanced quality voice that you must download to use.
- [AVSpeechSynthesisVoiceQuality.premium](./avspeechsynthesisvoicequality/premium.md)
  A premium quality voice that you must download to use.

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
- [enum AVSpeechSynthesisVoiceGender](./avspeechsynthesisvoicegender.md)
  The gender for a voice.
- [AVSpeechSynthesisVoice.Traits](./avspeechsynthesisvoice/traits.md)
  Traits that describe a voice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisvoicequality)*