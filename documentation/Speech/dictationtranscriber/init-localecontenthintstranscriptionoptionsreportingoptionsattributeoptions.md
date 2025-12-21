# init(locale:contentHints:transcriptionOptions:reportingOptions:attributeOptions:)

**Framework**: Speech  
**Kind**: init

Creates a transcriber.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
convenience init(locale: Locale, contentHints: Set<DictationTranscriber.ContentHint>, transcriptionOptions: Set<DictationTranscriber.TranscriptionOption>, reportingOptions: Set<DictationTranscriber.ReportingOption>, attributeOptions: Set<DictationTranscriber.ResultAttributeOption>)
```

## Parameters

- `locale`: A locale indicating a spoken and written language or script.
- `contentHints`: A selection of expected characteristics of the spoken audio.
- `transcriptionOptions`: A selection of options relating to the text of the transcription.
- `reportingOptions`: A selection of options relating to the transcriber’s result delivery.
- `attributeOptions`: A selection of options relating to the attributes of the transcription.

## See Also

- [convenience init(locale: Locale, preset: DictationTranscriber.Preset)](dictationtranscriber/init(locale:preset:).md)
  Creates a transcriber according to a preset.
- [DictationTranscriber.Preset](dictationtranscriber/preset.md)
  Predefined transcriber configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber/init(locale:contenthints:transcriptionoptions:reportingoptions:attributeoptions:))*