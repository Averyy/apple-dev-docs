# SpeechTranscriber.Preset

**Framework**: Speech  
**Kind**: struct

Predefined transcriber configurations.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
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

| Preset | [`SpeechTranscriber.ReportingOption.volatileResults`](speechtranscriber/reportingoption/volatileresults.md) | [`SpeechTranscriber.ReportingOption.fastResults`](speechtranscriber/reportingoption/fastresults.md) | [`SpeechTranscriber.ReportingOption.alternativeTranscriptions`](speechtranscriber/reportingoption/alternativetranscriptions.md) | [`SpeechTranscriber.ResultAttributeOption.audioTimeRange`](speechtranscriber/resultattributeoption/audiotimerange.md) |
| --- | --- | --- | --- | --- |
| `transcription` | No | No | No | No |
| `transcriptionWithAlternatives` | No | No |  | No |
| `timeIndexedTranscriptionWithAlternatives` | No | No |  |  |
| `progressiveTranscription` |  |  | No | No |
| `timeIndexedProgressiveTranscription` |  |  | No |  |

## Topics

### Standard presets
- [static let transcription: SpeechTranscriber.Preset](speechtranscriber/preset/transcription.md)
  Configuration for basic, accurate transcription.
- [static let transcriptionWithAlternatives: SpeechTranscriber.Preset](speechtranscriber/preset/transcriptionwithalternatives.md)
  Configuration for transcription with editing suggestions.
- [static let timeIndexedTranscriptionWithAlternatives: SpeechTranscriber.Preset](speechtranscriber/preset/timeindexedtranscriptionwithalternatives.md)
  Configuration for transcription with editing suggestions, cross-referenced to source audio.
- [static let progressiveTranscription: SpeechTranscriber.Preset](speechtranscriber/preset/progressivetranscription.md)
  Configuration for immediate transcription of live audio.
- [static let timeIndexedProgressiveTranscription: SpeechTranscriber.Preset](speechtranscriber/preset/timeindexedprogressivetranscription.md)
  Configuration for immediate transcription of live audio, cross-referenced to stream time-codes.
### Creating a preset
- [init(transcriptionOptions: Set<SpeechTranscriber.TranscriptionOption>, reportingOptions: Set<SpeechTranscriber.ReportingOption>, attributeOptions: Set<SpeechTranscriber.ResultAttributeOption>)](speechtranscriber/preset/init(transcriptionoptions:reportingoptions:attributeoptions:).md)
  Creates a preset.
### Getting preset properties
- [var attributeOptions: Set<SpeechTranscriber.ResultAttributeOption>](speechtranscriber/preset/attributeoptions.md)
  Options relating to the attributes of the transcription appropriate for this preset.
- [var reportingOptions: Set<SpeechTranscriber.ReportingOption>](speechtranscriber/preset/reportingoptions.md)
  Options relating to the transcriber’s result delivery appropriate for this preset.
- [var transcriptionOptions: Set<SpeechTranscriber.TranscriptionOption>](speechtranscriber/preset/transcriptionoptions.md)
  Options relating to the text of the transcription appropriate for this preset.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience init(locale: Locale, preset: SpeechTranscriber.Preset)](speechtranscriber/init(locale:preset:).md)
  Creates a general-purpose transcriber according to a preset.
- [convenience init(locale: Locale, transcriptionOptions: Set<SpeechTranscriber.TranscriptionOption>, reportingOptions: Set<SpeechTranscriber.ReportingOption>, attributeOptions: Set<SpeechTranscriber.ResultAttributeOption>)](speechtranscriber/init(locale:transcriptionoptions:reportingoptions:attributeoptions:).md)
  Creates a general-purpose transcriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechtranscriber/preset)*