# identifier

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The unique identifier of a voice.

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
var identifier: String { get }
```

```objc
@property (nonatomic, readonly) NSString * identifier;
```

## See Also

### Inspecting voices
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
- [AVSpeechSynthesisVoice.Traits](./traits.md)
  Traits that describe a voice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisvoice/identifier)*