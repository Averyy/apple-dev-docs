# DictationTranscriber.Preset

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

This example configures a transcriber according to the `shortDictation` preset, but adds emoji recognition:

```swift
let preset = DictationTranscriber.Preset.shortDictation
let transcriber = DictationTranscriber(
    locale: Locale.current,
    contentHints: preset.contentHints,
    transcriptionOptions: preset.transcriptionOptions.union([.emoji])
    reportingOptions: preset.reportingOptions
    attributeOptions: preset.attributeOptions
)
```

This table lists the presets and their configurations:

| Preset | [`shortForm`](dictationtranscriber/contenthint/shortform.md) | [`DictationTranscriber.ReportingOption.volatileResults`](dictationtranscriber/reportingoption/volatileresults.md) | [`DictationTranscriber.ReportingOption.frequentFinalization`](dictationtranscriber/reportingoption/frequentfinalization.md) | [`DictationTranscriber.ResultAttributeOption.audioTimeRange`](dictationtranscriber/resultattributeoption/audiotimerange.md) | [`DictationTranscriber.TranscriptionOption.punctuation`](dictationtranscriber/transcriptionoption/punctuation.md) |
| --- | --- | --- | --- | --- | --- |
| `phrase` |  | No | No | No | No |
| `shortDictation` |  | No | No | No |  |
| `progressiveShortDictation` |  |  |  | No |  |
| `longDictation` | No | No | No | No |  |
| `progressiveLongDictation` | No |  | No | No |  |
| `timeIndexedLongDictation` | No | No | No |  |  |

## Topics

### Standard presets
- [static let phrase: DictationTranscriber.Preset](dictationtranscriber/preset/phrase.md)
  Configuration for a short phrase without punctuation.
- [static let shortDictation: DictationTranscriber.Preset](dictationtranscriber/preset/shortdictation.md)
  Configuration for about a minute of audio.
- [static let progressiveShortDictation: DictationTranscriber.Preset](dictationtranscriber/preset/progressiveshortdictation.md)
  Configuration for immediate transcription of about a minute of live audio.
- [static let longDictation: DictationTranscriber.Preset](dictationtranscriber/preset/longdictation.md)
  Configuration for more than a minute of audio.
- [static let progressiveLongDictation: DictationTranscriber.Preset](dictationtranscriber/preset/progressivelongdictation.md)
  Configuration for immediate transcription of lengthy audio.
- [static let timeIndexedLongDictation: DictationTranscriber.Preset](dictationtranscriber/preset/timeindexedlongdictation.md)
  Configure for lengthy audio, cross-referencing words to time-codes.
### Creating a preset
- [init(contentHints: Set<DictationTranscriber.ContentHint>, transcriptionOptions: Set<DictationTranscriber.TranscriptionOption>, reportingOptions: Set<DictationTranscriber.ReportingOption>, attributeOptions: Set<DictationTranscriber.ResultAttributeOption>)](dictationtranscriber/preset/init(contenthints:transcriptionoptions:reportingoptions:attributeoptions:).md)
  Creates a preset.
### Getting preset properties
- [var attributeOptions: Set<DictationTranscriber.ResultAttributeOption>](dictationtranscriber/preset/attributeoptions.md)
  Options relating to the attributes of the transcription appropriate for this preset.
- [var contentHints: Set<DictationTranscriber.ContentHint>](dictationtranscriber/preset/contenthints.md)
  Expected characteristics of the spoken audio appropriate for this preset.
- [var reportingOptions: Set<DictationTranscriber.ReportingOption>](dictationtranscriber/preset/reportingoptions.md)
  Options relating to the transcriber’s result delivery appropriate for this preset.
- [var transcriptionOptions: Set<DictationTranscriber.TranscriptionOption>](dictationtranscriber/preset/transcriptionoptions.md)
  Options relating to the text of the transcription appropriate for this preset.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience init(locale: Locale, preset: DictationTranscriber.Preset)](dictationtranscriber/init(locale:preset:).md)
  Creates a transcriber according to a preset.
- [convenience init(locale: Locale, contentHints: Set<DictationTranscriber.ContentHint>, transcriptionOptions: Set<DictationTranscriber.TranscriptionOption>, reportingOptions: Set<DictationTranscriber.ReportingOption>, attributeOptions: Set<DictationTranscriber.ResultAttributeOption>)](dictationtranscriber/init(locale:contenthints:transcriptionoptions:reportingoptions:attributeoptions:).md)
  Creates a transcriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber/preset)*