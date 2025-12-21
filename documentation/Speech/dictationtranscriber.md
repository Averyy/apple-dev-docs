# DictationTranscriber

**Framework**: Speech  
**Kind**: class

A speech-to-text transcription module that’s similar to system dictation features and compatible with older devices.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final class DictationTranscriber
```

#### Overview

This transcriber uses the same speech-to-text machine learning models as system dictation features do, or as [`SFSpeechRecognizer`](sfspeechrecognizer.md) does when it is configured for on-device operation. This transcriber does not support languages or locales that `SFSpeechRecognizer` only supports via network access.

Several transcriber instances can share the same backing engine instances and models, so long as the transcribers are configured similarly in certain respects.

##### Improve Accuracy

You can bias recognition towards certain words, supply custom vocabulary, or adjust the transcriber’s algorithm to improve the transcriber’s accuracy.

To bias recognition towards certain words, create an [`AnalysisContext`](analysiscontext.md) object and add those words to its [`contextualStrings`](analysiscontext/contextualstrings.md) property. Create a [`SpeechAnalyzer`](speechanalyzer.md) instance with that context object or set the analyzer’s [`context`](speechanalyzer/context.md) property.

To supply custom vocabulary, create an [`SFSpeechLanguageModel`](sfspeechlanguagemodel.md) object and configure the transcriber with a corresponding [`customizedLanguage(modelConfiguration:)`](dictationtranscriber/contenthint/customizedlanguage(modelconfiguration:).md) option.

To adjust the transcriber’s algorithm, configure the transcriber with relevant [`DictationTranscriber.ContentHint`](dictationtranscriber/contenthint.md) parameter. For example, you may use [`farField`](dictationtranscriber/contenthint/farfield.md) hint to improve accuracy of distant speech.

## Topics

### Creating a transcriber
- [convenience init(locale: Locale, preset: DictationTranscriber.Preset)](dictationtranscriber/init(locale:preset:).md)
  Creates a transcriber according to a preset.
- [convenience init(locale: Locale, contentHints: Set<DictationTranscriber.ContentHint>, transcriptionOptions: Set<DictationTranscriber.TranscriptionOption>, reportingOptions: Set<DictationTranscriber.ReportingOption>, attributeOptions: Set<DictationTranscriber.ResultAttributeOption>)](dictationtranscriber/init(locale:contenthints:transcriptionoptions:reportingoptions:attributeoptions:).md)
  Creates a transcriber.
- [DictationTranscriber.Preset](dictationtranscriber/preset.md)
  Predefined transcriber configurations.
### Configuring transcription
- [DictationTranscriber.ContentHint](dictationtranscriber/contenthint.md)
  Expected characteristics of the spoken audio content and its delivery.
- [DictationTranscriber.ReportingOption](dictationtranscriber/reportingoption.md)
  Options relating to the transcriber’s result delivery.
- [DictationTranscriber.ResultAttributeOption](dictationtranscriber/resultattributeoption.md)
  Options relating to the attributes of the transcription.
- [DictationTranscriber.TranscriptionOption](dictationtranscriber/transcriptionoption.md)
  Options relating to the text of the transcription.
### Checking locale support
- [static var installedLocales: [Locale]](dictationtranscriber/installedlocales.md)
  The locales that the transcriber can transcribe into, considering only locales that are installed on the device.
- [static var supportedLocales: [Locale]](dictationtranscriber/supportedlocales.md)
  The locales that the transcriber can transcribe into, including locales that may not be installed but are downloadable.
- [static func supportedLocale(equivalentTo: Locale) async -> Locale?](dictationtranscriber/supportedlocale(equivalentto:).md)
  A locale from the module’s supported locales equivalent to the given locale.
### Getting results
- [DictationTranscriber.Result](dictationtranscriber/result.md)
  A phrase or passage of transcribed speech. The phrases are sent in order.

## Relationships

### Conforms To
- [LocaleDependentSpeechModule](localedependentspeechmodule.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SpeechModule](speechmodule.md)

## See Also

- [class SpeechTranscriber](speechtranscriber.md)
  A speech-to-text transcription module that’s appropriate for normal conversation and general purposes.
- [class SpeechDetector](speechdetector.md)
  A module that performs a voice activity detection (VAD) analysis.
- [protocol SpeechModule](speechmodule.md)
  Protocol that all analyzer modules conform to.
- [protocol LocaleDependentSpeechModule](localedependentspeechmodule.md)
  A module that requires locale-specific assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber)*