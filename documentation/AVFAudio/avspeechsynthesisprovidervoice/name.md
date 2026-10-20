# name

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The localized name of the voice.

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
var name: String { get }
```

```objc
@property (nonatomic, readonly) NSString * name;
```

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
- [var primaryLanguages: [String]](./primarylanguages.md)
  A list of BCP 47 codes that identify the languages the synthesizer uses.
- [var supportedLanguages: [String]](./supportedlanguages.md)
  A list of BCP 47 codes that identify the languages a voice supports.
- [var version: String](./version.md)
  The version of the voice.
- [var voiceSize: Int64](./voicesize.md)
  The size of the voice package on disk, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisprovidervoice/name)*