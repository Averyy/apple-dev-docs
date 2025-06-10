# DictationTranscriber.Preset

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

### Initializers
- [init(contentHints: Set<DictationTranscriber.ContentHint>, transcriptionOptions: Set<DictationTranscriber.TranscriptionOption>, reportingOptions: Set<DictationTranscriber.ReportingOption>, attributeOptions: Set<DictationTranscriber.ResultAttributeOption>)](dictationtranscriber/preset/init(contenthints:transcriptionoptions:reportingoptions:attributeoptions:).md)
  Creates a preset.
### Instance Properties
- [var attributeOptions: Set<DictationTranscriber.ResultAttributeOption>](dictationtranscriber/preset/attributeoptions.md)
  Options relating to the attributes of the transcription appropriate for this preset.
- [var contentHints: Set<DictationTranscriber.ContentHint>](dictationtranscriber/preset/contenthints.md)
  Expected characteristics of the spoken audio appropriate for this preset.
- [var reportingOptions: Set<DictationTranscriber.ReportingOption>](dictationtranscriber/preset/reportingoptions.md)
  Options relating to the transcriber’s result delivery appropriate for this preset.
- [var transcriptionOptions: Set<DictationTranscriber.TranscriptionOption>](dictationtranscriber/preset/transcriptionoptions.md)
  Options relating to the text of the transcription appropriate for this preset.
### Type Properties
- [static let longDictation: DictationTranscriber.Preset](dictationtranscriber/preset/longdictation.md)
- [static let phrase: DictationTranscriber.Preset](dictationtranscriber/preset/phrase.md)
- [static let progressiveLongDictation: DictationTranscriber.Preset](dictationtranscriber/preset/progressivelongdictation.md)
- [static let progressiveShortDictation: DictationTranscriber.Preset](dictationtranscriber/preset/progressiveshortdictation.md)
- [static let shortDictation: DictationTranscriber.Preset](dictationtranscriber/preset/shortdictation.md)
- [static let timeIndexedLongDictation: DictationTranscriber.Preset](dictationtranscriber/preset/timeindexedlongdictation.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [DictationTranscriber.ContentHint](dictationtranscriber/contenthint.md)
  Expected characteristics of the spoken audio content and its delivery.
- [DictationTranscriber.Result](dictationtranscriber/result.md)
  A phrase or passage of transcribed speech. The phrases are sent in order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber/preset)*