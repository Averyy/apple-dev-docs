# init(locale:transcriptionOptions:reportingOptions:attributeOptions:)

**Framework**: Speech  
**Kind**: init  
**Role**: Initializer

Creates a general-purpose transcriber.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
convenience init(locale: Locale, transcriptionOptions: Set<SpeechTranscriber.TranscriptionOption>, reportingOptions: Set<SpeechTranscriber.ReportingOption>, attributeOptions: Set<SpeechTranscriber.ResultAttributeOption>)
```

## Parameters

- `locale`: A locale indicating a spoken and written language or script.
- `transcriptionOptions`: A selection of options relating to the text of the transcription.
- `reportingOptions`: A selection of options relating to the transcriber’s result delivery.
- `attributeOptions`: A selection of options relating to the attributes of the transcription.

## See Also

### Creating a transcriber
- [convenience init(locale: Locale, preset: SpeechTranscriber.Preset)](./init%28locale,preset%29.md)
  Creates a general-purpose transcriber according to a preset.
- [SpeechTranscriber.Preset](./preset.md)
  Predefined transcriber configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechtranscriber/init(locale:transcriptionoptions:reportingoptions:attributeoptions:))*