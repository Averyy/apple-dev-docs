# init(locale:preset:)

**Framework**: Speech  
**Kind**: init

Creates a transcriber according to a preset.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
convenience init(locale: Locale, preset: DictationTranscriber.Preset)
```

## Parameters

- `locale`: A locale indicating a spoken and written language or script.
- `preset`: A structure that contains some transcriber options.

## See Also

- [convenience init(locale: Locale, contentHints: Set<DictationTranscriber.ContentHint>, transcriptionOptions: Set<DictationTranscriber.TranscriptionOption>, reportingOptions: Set<DictationTranscriber.ReportingOption>, attributeOptions: Set<DictationTranscriber.ResultAttributeOption>)](dictationtranscriber/init(locale:contenthints:transcriptionoptions:reportingoptions:attributeoptions:).md)
  Creates a transcriber.
- [DictationTranscriber.Preset](dictationtranscriber/preset.md)
  Predefined transcriber configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber/init(locale:preset:))*