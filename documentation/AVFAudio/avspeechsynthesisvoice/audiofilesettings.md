# audioFileSettings

**Framework**: AVFAudio  
**Kind**: property

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

#### Discussion

If you want to generate speech and save it as an audio file to share or play later, use this dictionary to create an [`AVAudioFile`](avaudiofile.md) instance and pass it as the `settings` parameter.

You can determine the [`AVAudioCommonFormat`](avaudiocommonformat.md) and interleaved properties of a voice from this dictionary. The format of this dictionary matches the data that [`AVSpeechSynthesizer.BufferCallback`](avspeechsynthesizer/buffercallback.md) provides for the same voice.

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
- [enum AVSpeechSynthesisVoiceQuality](avspeechsynthesisvoicequality.md)
  The speech quality of a voice.
- [enum AVSpeechSynthesisVoiceGender](avspeechsynthesisvoicegender.md)
  The gender for a voice.
- [AVSpeechSynthesisVoice.Traits](avspeechsynthesisvoice/traits.md)
  Traits that describe a voice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisvoice/audiofilesettings)*