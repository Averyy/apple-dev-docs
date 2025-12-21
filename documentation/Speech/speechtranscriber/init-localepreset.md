# init(locale:preset:)

**Framework**: Speech  
**Kind**: init

Creates a general-purpose transcriber according to a preset.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
convenience init(locale: Locale, preset: SpeechTranscriber.Preset)
```

## Parameters

- `locale`: A locale indicating a spoken and written language or script.
- `preset`: A structure that contains some transcriber options.

## See Also

- [convenience init(locale: Locale, transcriptionOptions: Set<SpeechTranscriber.TranscriptionOption>, reportingOptions: Set<SpeechTranscriber.ReportingOption>, attributeOptions: Set<SpeechTranscriber.ResultAttributeOption>)](speechtranscriber/init(locale:transcriptionoptions:reportingoptions:attributeoptions:).md)
  Creates a general-purpose transcriber.
- [SpeechTranscriber.Preset](speechtranscriber/preset.md)
  Predefined transcriber configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechtranscriber/init(locale:preset:))*