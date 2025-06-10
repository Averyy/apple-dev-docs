# SpeechTranscriber.Preset

**Framework**: Speech  
**Kind**: struct

Predefined transcriber configurations.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct Preset
```

#### Overview

You can configure a transcriber with a preset, or modify the values of a preset’s properties and configure a transcriber with the modified values. You can also create your own presets by extending this type.

It is not necessary to use a preset at all; you can also use the transcriber’s designated initializer to completely customize its configuration.

This example configures a transcriber according to the `timeIndexedOfflineTranscriptionWithAlternatives` preset, but adds etiquette filtering and removes alternative transcriptions:

```swift
let preset = SpeechTranscriber.Preset.timeIndexedOfflineTranscriptionWithAlternatives
let transcriber = SpeechTranscriber(
    locale: Locale.current,
    transcriptionOptions: preset.transcriptionOptions.union([.etiquetteReplacements])
    reportingOptions: preset.reportingOptions.subtracting([.alternativeTranscriptions])
    attributeOptions: preset.attributeOptions
)
```

This table lists the presets and their configurations:

| Preset | [`SpeechTranscriber.ReportingOption.volatileResults`](speechtranscriber/reportingoption/volatileresults.md) | [`SpeechTranscriber.ReportingOption.frequentFinalization`](speechtranscriber/reportingoption/frequentfinalization.md) | [`SpeechTranscriber.ReportingOption.alternativeTranscriptions`](speechtranscriber/reportingoption/alternativetranscriptions.md) | [`SpeechTranscriber.ResultAttributeOption.audioTimeRange`](speechtranscriber/resultattributeoption/audiotimerange.md) |
| --- | --- | --- | --- | --- |
| `progressiveLiveTranscription` |  |  | No | No |
| `offlineTranscription` | No | No | No | No |
| `offlineTranscriptionWithAlternatives` | No | No |  | No |
| `timeIndexedOfflineTranscriptionWithAlternatives` | No | No |  |  |
| `timeIndexedLiveCaptioning` | No |  | No |  |

## Topics

### Initializers
- [init(transcriptionOptions: Set<SpeechTranscriber.TranscriptionOption>, reportingOptions: Set<SpeechTranscriber.ReportingOption>, attributeOptions: Set<SpeechTranscriber.ResultAttributeOption>)](speechtranscriber/preset/init(transcriptionoptions:reportingoptions:attributeoptions:).md)
  Creates a preset.
### Instance Properties
- [var attributeOptions: Set<SpeechTranscriber.ResultAttributeOption>](speechtranscriber/preset/attributeoptions.md)
  Options relating to the attributes of the transcription appropriate for this preset.
- [var reportingOptions: Set<SpeechTranscriber.ReportingOption>](speechtranscriber/preset/reportingoptions.md)
  Options relating to the transcriber’s result delivery appropriate for this preset.
- [var transcriptionOptions: Set<SpeechTranscriber.TranscriptionOption>](speechtranscriber/preset/transcriptionoptions.md)
  Options relating to the text of the transcription appropriate for this preset.
### Type Properties
- [static let offlineTranscription: SpeechTranscriber.Preset](speechtranscriber/preset/offlinetranscription.md)
- [static let offlineTranscriptionWithAlternatives: SpeechTranscriber.Preset](speechtranscriber/preset/offlinetranscriptionwithalternatives.md)
- [static let progressiveLiveTranscription: SpeechTranscriber.Preset](speechtranscriber/preset/progressivelivetranscription.md)
- [static let timeIndexedLiveCaptioning: SpeechTranscriber.Preset](speechtranscriber/preset/timeindexedlivecaptioning.md)
- [static let timeIndexedOfflineTranscriptionWithAlternatives: SpeechTranscriber.Preset](speechtranscriber/preset/timeindexedofflinetranscriptionwithalternatives.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [SpeechTranscriber.Result](speechtranscriber/result.md)
  A phrase or passage of transcribed speech. The phrases are sent in order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechtranscriber/preset)*