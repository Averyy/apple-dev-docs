# voiceTraits

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The traits of a voice.

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
var voiceTraits: AVSpeechSynthesisVoice.Traits { get }
```

```objc
@property (nonatomic, readonly) AVSpeechSynthesisVoiceTraits voiceTraits;
```

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
- [var audioFileSettings: [String : Any]](./audiofilesettings.md)
  A dictionary that contains audio file settings.
- [enum AVSpeechSynthesisVoiceQuality](../avspeechsynthesisvoicequality.md)
  The speech quality of a voice.
- [enum AVSpeechSynthesisVoiceGender](../avspeechsynthesisvoicegender.md)
  The gender for a voice.
- [AVSpeechSynthesisVoice.Traits](./traits.md)
  Traits that describe a voice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisvoice/voicetraits)*