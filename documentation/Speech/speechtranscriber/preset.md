# SpeechTranscriber.Preset

**Framework**: Speech  
**Kind**: struct  
**Role**: Structure

Predefined transcriber configurations.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Preset
```

#### Overview

You can configure a transcriber with a preset, or modify the values of a preset’s properties and configure a transcriber with the modified values. You can also create your own presets by extending this type.

It is not necessary to use a preset at all; you can also use the transcriber’s designated initializer to completely customize its configuration.

This example configures a transcriber according to the `timeIndexedTranscriptionWithAlternatives` preset, but adds etiquette filtering and removes alternative transcriptions:

```swift
let preset = SpeechTranscriber.Preset.timeIndexedTranscriptionWithAlternatives
let transcriber = SpeechTranscriber(
    locale: Locale.current,
    transcriptionOptions: preset.transcriptionOptions.union([.etiquetteReplacements])
    reportingOptions: preset.reportingOptions.subtracting([.alternativeTranscriptions])
    attributeOptions: preset.attributeOptions
)
```

This table lists the presets and their configurations:

| Preset | [volatileResults](./reportingoption/volatileresults.md) | [fastResults](./reportingoption/fastresults.md) | [alternativeTranscriptions](./reportingoption/alternativetranscriptions.md) | [audioTimeRange](./resultattributeoption/audiotimerange.md) |
| --- | --- | --- | --- | --- |
| `transcription` | No | No | No | No |
| `transcriptionWithAlternatives` | No | No | **Yes** | No |
| `timeIndexedTranscriptionWithAlternatives` | No | No | **Yes** | **Yes** |
| `progressiveTranscription` | **Yes** | **Yes** | No | No |
| `timeIndexedProgressiveTranscription` | **Yes** | **Yes** | No | **Yes** |

## Topics

### Standard presets
- [static let transcription: SpeechTranscriber.Preset](./preset/transcription.md)
  Configuration for basic, accurate transcription.
- [static let transcriptionWithAlternatives: SpeechTranscriber.Preset](./preset/transcriptionwithalternatives.md)
  Configuration for transcription with editing suggestions.
- [static let timeIndexedTranscriptionWithAlternatives: SpeechTranscriber.Preset](./preset/timeindexedtranscriptionwithalternatives.md)
  Configuration for transcription with editing suggestions, cross-referenced to source audio.
- [static let progressiveTranscription: SpeechTranscriber.Preset](./preset/progressivetranscription.md)
  Configuration for immediate transcription of live audio.
- [static let timeIndexedProgressiveTranscription: SpeechTranscriber.Preset](./preset/timeindexedprogressivetranscription.md)
  Configuration for immediate transcription of live audio, cross-referenced to stream time-codes.
### Creating a preset
- [init(transcriptionOptions: Set<SpeechTranscriber.TranscriptionOption>, reportingOptions: Set<SpeechTranscriber.ReportingOption>, attributeOptions: Set<SpeechTranscriber.ResultAttributeOption>)](./preset/init%28transcriptionoptions,reportingoptions,attributeoptions%29.md)
  Creates a preset.
### Getting preset properties
- [var attributeOptions: Set<SpeechTranscriber.ResultAttributeOption>](./preset/attributeoptions.md)
  Options relating to the attributes of the transcription appropriate for this preset.
- [var reportingOptions: Set<SpeechTranscriber.ReportingOption>](./preset/reportingoptions.md)
  Options relating to the transcriber’s result delivery appropriate for this preset.
- [var transcriptionOptions: Set<SpeechTranscriber.TranscriptionOption>](./preset/transcriptionoptions.md)
  Options relating to the text of the transcription appropriate for this preset.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a transcriber
- [convenience init(locale: Locale, preset: SpeechTranscriber.Preset)](./init%28locale,preset%29.md)
  Creates a general-purpose transcriber according to a preset.
- [convenience init(locale: Locale, transcriptionOptions: Set<SpeechTranscriber.TranscriptionOption>, reportingOptions: Set<SpeechTranscriber.ReportingOption>, attributeOptions: Set<SpeechTranscriber.ResultAttributeOption>)](./init%28locale,transcriptionoptions,reportingoptions,attributeoptions%29.md)
  Creates a general-purpose transcriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechtranscriber/preset)*