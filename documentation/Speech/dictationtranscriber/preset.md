# DictationTranscriber.Preset

**Framework**: Speech  
**Kind**: struct  
**Role**: Structure

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

## Overview

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

| Preset | [shortForm](./contenthint/shortform.md) | [volatileResults](./reportingoption/volatileresults.md) | [frequentFinalization](./reportingoption/frequentfinalization.md) | [audioTimeRange](./resultattributeoption/audiotimerange.md) | [punctuation](./transcriptionoption/punctuation.md) |
| --- | --- | --- | --- | --- | --- |
| `phrase` | **Yes** | No | No | No | No |
| `shortDictation` | **Yes** | No | No | No | **Yes** |
| `progressiveShortDictation` | **Yes** | **Yes** | **Yes** | No | **Yes** |
| `longDictation` | No | No | No | No | **Yes** |
| `progressiveLongDictation` | No | **Yes** | No | No | **Yes** |
| `timeIndexedLongDictation` | No | No | No | **Yes** | **Yes** |

## Topics

### Standard presets
- [static let phrase: DictationTranscriber.Preset](./preset/phrase.md)
  Configuration for a short phrase without punctuation.
- [static let shortDictation: DictationTranscriber.Preset](./preset/shortdictation.md)
  Configuration for about a minute of audio.
- [static let progressiveShortDictation: DictationTranscriber.Preset](./preset/progressiveshortdictation.md)
  Configuration for immediate transcription of about a minute of live audio.
- [static let longDictation: DictationTranscriber.Preset](./preset/longdictation.md)
  Configuration for more than a minute of audio.
- [static let progressiveLongDictation: DictationTranscriber.Preset](./preset/progressivelongdictation.md)
  Configuration for immediate transcription of lengthy audio.
- [static let timeIndexedLongDictation: DictationTranscriber.Preset](./preset/timeindexedlongdictation.md)
  Configure for lengthy audio, cross-referencing words to time-codes.
### Creating a preset
- [init(contentHints: Set<DictationTranscriber.ContentHint>, transcriptionOptions: Set<DictationTranscriber.TranscriptionOption>, reportingOptions: Set<DictationTranscriber.ReportingOption>, attributeOptions: Set<DictationTranscriber.ResultAttributeOption>)](./preset/init%28contenthints,transcriptionoptions,reportingoptions,attributeoptions%29.md)
  Creates a preset.
### Getting preset properties
- [var attributeOptions: Set<DictationTranscriber.ResultAttributeOption>](./preset/attributeoptions.md)
  Options relating to the attributes of the transcription appropriate for this preset.
- [var contentHints: Set<DictationTranscriber.ContentHint>](./preset/contenthints.md)
  Expected characteristics of the spoken audio appropriate for this preset.
- [var reportingOptions: Set<DictationTranscriber.ReportingOption>](./preset/reportingoptions.md)
  Options relating to the transcriber’s result delivery appropriate for this preset.
- [var transcriptionOptions: Set<DictationTranscriber.TranscriptionOption>](./preset/transcriptionoptions.md)
  Options relating to the text of the transcription appropriate for this preset.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a transcriber
- [convenience init(locale: Locale, preset: DictationTranscriber.Preset)](./init%28locale,preset%29.md)
  Creates a transcriber according to a preset.
- [convenience init(locale: Locale, contentHints: Set<DictationTranscriber.ContentHint>, transcriptionOptions: Set<DictationTranscriber.TranscriptionOption>, reportingOptions: Set<DictationTranscriber.ReportingOption>, attributeOptions: Set<DictationTranscriber.ResultAttributeOption>)](./init%28locale,contenthints,transcriptionoptions,reportingoptions,attributeoptions%29.md)
  Creates a transcriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber/preset)*