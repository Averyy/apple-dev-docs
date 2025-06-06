# primaryLanguages

**Framework**: AVFAudio  
**Kind**: property

A list of BCP 47 codes that identify the languages the synthesizer uses.

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
var primaryLanguages: [String] { get }
```

#### Discussion

These languages are what a voice primarily supports. For example, if the primary language is `zh-CN —` with no additional [`supportedLanguages`](avspeechsynthesisprovidervoice/supportedlanguages.md) — the system may switch voices to speak a phrase that contains other languages. Changing voices depends on user preferences and what accessibility feature is using the voice.

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
- [var supportedLanguages: [String]](avspeechsynthesisprovidervoice/supportedlanguages.md)
  A list of BCP 47 codes that identify the languages a voice supports.
- [var version: String](avspeechsynthesisprovidervoice/version.md)
  The version of the voice.
- [var voiceSize: Int64](avspeechsynthesisprovidervoice/voicesize.md)
  The size of the voice package on disk, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisprovidervoice/primarylanguages)*