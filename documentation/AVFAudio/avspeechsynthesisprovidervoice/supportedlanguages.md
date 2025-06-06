# supportedLanguages

**Framework**: AVFAudio  
**Kind**: property

A list of BCP 47 codes that identify the languages a voice supports.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var supportedLanguages: [String] { get }
```

#### Discussion

These languages are what a voice supports — when given a multi-language phrase — without the need to switch voice. For example, if the primary language is `zh-CN`, and this value contains `zh-CN` and `en-US`, a synthesizer that receives a phrase with both languages would speak the entire phrase.

## See Also

- [var age: Int](avspeechsynthesisprovidervoice/age.md)
  The age of the voice, in years.
- [var gender: AVSpeechSynthesisVoiceGender](avspeechsynthesisprovidervoice/gender.md)
  The gender of the voice.
- [enum AVSpeechSynthesisVoiceGender](avspeechsynthesisvoicegender.md)
  The gender for a voice.
- [var identifier: String](avspeechsynthesisprovidervoice/identifier.md)
  The unique identifier for the voice.
- [var name: String](avspeechsynthesisprovidervoice/name.md)
  The localized name of the voice.
- [var primaryLanguages: [String]](avspeechsynthesisprovidervoice/primarylanguages.md)
  A list of BCP 47 codes that identify the languages the synthesizer uses.
- [var version: String](avspeechsynthesisprovidervoice/version.md)
  The version of the voice.
- [var voiceSize: Int64](avspeechsynthesisprovidervoice/voicesize.md)
  The size of the voice package on disk, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisprovidervoice/supportedlanguages)*