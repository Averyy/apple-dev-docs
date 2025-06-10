# DictationTranscriber

**Framework**: Speech  
**Kind**: class

A module that transcribes speech to text. This transcriber is used by [`SFSpeechRecognizer`](sfspeechrecognizer.md) and system dictation features.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final class DictationTranscriber
```

#### Overview

Several transcriber instances can share the same backing engine instances and models, so long as the transcribers are configured similarly in certain respects.

## Topics

### Structures
- [DictationTranscriber.ContentHint](dictationtranscriber/contenthint.md)
  Expected characteristics of the spoken audio content and its delivery.
- [DictationTranscriber.Preset](dictationtranscriber/preset.md)
  Predefined transcriber configurations.
- [DictationTranscriber.Result](dictationtranscriber/result.md)
  A phrase or passage of transcribed speech. The phrases are sent in order.
### Initializers
- [convenience init(locale: Locale, contentHints: Set<DictationTranscriber.ContentHint>, transcriptionOptions: Set<DictationTranscriber.TranscriptionOption>, reportingOptions: Set<DictationTranscriber.ReportingOption>, attributeOptions: Set<DictationTranscriber.ResultAttributeOption>)](dictationtranscriber/init(locale:contenthints:transcriptionoptions:reportingoptions:attributeoptions:).md)
  Creates a transcriber.
- [convenience init(locale: Locale, preset: DictationTranscriber.Preset)](dictationtranscriber/init(locale:preset:).md)
  Creates a transcriber according to a preset.
### Type Properties
- [static var installedLocales: [Locale]](dictationtranscriber/installedlocales.md)
  The locales that the transcriber can transcribe into, considering only locales that are installed on the device.
- [static var supportedLocales: [Locale]](dictationtranscriber/supportedlocales.md)
  The locales that the transcriber can transcribe into, including locales that may not be installed but are downloadable.
### Enumerations
- [DictationTranscriber.ReportingOption](dictationtranscriber/reportingoption.md)
  Options relating to the transcriber’s result delivery.
- [DictationTranscriber.ResultAttributeOption](dictationtranscriber/resultattributeoption.md)
  Options relating to the attributes of the transcription.
- [DictationTranscriber.TranscriptionOption](dictationtranscriber/transcriptionoption.md)
  Options relating to the text of the transcription.

## Relationships

### Conforms To
- [LocaleDependentSpeechModule](localedependentspeechmodule.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SpeechModule](speechmodule.md)

## See Also

- [protocol SpeechModule](speechmodule.md)
  Protocol that all analyzer modules conform to.
- [protocol LocaleDependentSpeechModule](localedependentspeechmodule.md)
  If a module conforms to this protocol, then its assets depend on the locale setting.
- [class SpeechTranscriber](speechtranscriber.md)
  A module that transcribes speech to text. This transcriber is appropriate for normal conversation and general purposes.
- [class SpeechDetector](speechdetector.md)
  A module that performs a voice activity detection (VAD) analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber)*