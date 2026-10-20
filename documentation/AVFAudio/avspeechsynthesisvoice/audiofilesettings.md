# audioFileSettings

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A dictionary that contains audio file settings.

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
var audioFileSettings: [String : Any] { get }
```

```objc
@property (nonatomic, readonly) NSDictionary<NSString *,id> * audioFileSettings;
```

#### Discussion

If you want to generate speech and save it as an audio file to share or play later, use this dictionary to create an [`AVAudioFile`](../avaudiofile.md) instance and pass it as the `settings` parameter.

You can determine the [`AVAudioCommonFormat`](../avaudiocommonformat.md) and interleaved properties of a voice from this dictionary. The format of this dictionary matches the data that [`AVSpeechSynthesizer.BufferCallback`](../avspeechsynthesizer/buffercallback.md) provides for the same voice.

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
- [enum AVSpeechSynthesisVoiceQuality](../avspeechsynthesisvoicequality.md)
  The speech quality of a voice.
- [enum AVSpeechSynthesisVoiceGender](../avspeechsynthesisvoicegender.md)
  The gender for a voice.
- [AVSpeechSynthesisVoice.Traits](./traits.md)
  Traits that describe a voice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisvoice/audiofilesettings)*