# primaryLanguages

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSArray<NSString *> * primaryLanguages;
```

## Discussion

These languages are what a voice primarily supports. For example, if the primary language is `zh-CN —` with no additional [`supportedLanguages`](./supportedlanguages.md) — the system may switch voices to speak a phrase that contains other languages. Changing voices depends on user preferences and what accessibility feature is using the voice.

## See Also

### Inspecting a voice
- [var age: Int](./age.md)
  The age of the voice, in years.
- [var gender: AVSpeechSynthesisVoiceGender](./gender.md)
  The gender of the voice.
- [enum AVSpeechSynthesisVoiceGender](../avspeechsynthesisvoicegender.md)
  The gender for a voice.
- [var identifier: String](./identifier.md)
  The unique identifier for the voice.
- [var name: String](./name.md)
  The localized name of the voice.
- [var supportedLanguages: [String]](./supportedlanguages.md)
  A list of BCP 47 codes that identify the languages a voice supports.
- [var version: String](./version.md)
  The version of the voice.
- [var voiceSize: Int64](./voicesize.md)
  The size of the voice package on disk, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisprovidervoice/primarylanguages)*