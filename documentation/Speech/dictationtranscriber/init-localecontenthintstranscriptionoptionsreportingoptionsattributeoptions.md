# init(locale:contentHints:transcriptionOptions:reportingOptions:attributeOptions:)

**Framework**: Speech  
**Kind**: init

Creates a transcriber.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber/init(locale:contenthints:transcriptionoptions:reportingoptions:attributeoptions:))*