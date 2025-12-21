# SpeechTranscriber

**Framework**: Speech  
**Kind**: class

A speech-to-text transcription module that’s appropriate for normal conversation and general purposes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final class SpeechTranscriber
```

#### Overview

Several transcriber instances can share the same backing engine instances and models, so long as the transcribers are configured similarly in certain respects.

##### Check Device Support

Use the [`isAvailable`](speechtranscriber/isavailable.md) or [`supportedLocales`](speechtranscriber/supportedlocales.md) properties to see if the current device supports the speech-to-text models used by `SpeechTranscriber`. If it does not, consider disabling the feature or using [`DictationTranscriber`](dictationtranscriber.md) instead.

## Topics

### Creating a transcriber
- [convenience init(locale: Locale, preset: SpeechTranscriber.Preset)](speechtranscriber/init(locale:preset:).md)
  Creates a general-purpose transcriber according to a preset.
- [convenience init(locale: Locale, transcriptionOptions: Set<SpeechTranscriber.TranscriptionOption>, reportingOptions: Set<SpeechTranscriber.ReportingOption>, attributeOptions: Set<SpeechTranscriber.ResultAttributeOption>)](speechtranscriber/init(locale:transcriptionoptions:reportingoptions:attributeoptions:).md)
  Creates a general-purpose transcriber.
- [SpeechTranscriber.Preset](speechtranscriber/preset.md)
  Predefined transcriber configurations.
### Configuring transcription
- [SpeechTranscriber.ReportingOption](speechtranscriber/reportingoption.md)
  Options relating to the transcriber’s result delivery.
- [SpeechTranscriber.ResultAttributeOption](speechtranscriber/resultattributeoption.md)
  Options relating to the attributes of the transcription.
- [SpeechTranscriber.TranscriptionOption](speechtranscriber/transcriptionoption.md)
  Options relating to the text of the transcription.
### Checking device support
- [static var isAvailable: Bool](speechtranscriber/isavailable.md)
  A Boolean value that indicates whether this module is available given the device’s hardware and capabilities.
### Checking locale support
- [static var installedLocales: [Locale]](speechtranscriber/installedlocales.md)
  The locales that the transcriber can transcribe into, considering only locales that are installed on the device.
- [static var supportedLocales: [Locale]](speechtranscriber/supportedlocales.md)
  The locales that the transcriber can transcribe into, including locales that may not be installed but are downloadable.
- [static func supportedLocale(equivalentTo: Locale) async -> Locale?](speechtranscriber/supportedlocale(equivalentto:).md)
  A locale from the module’s supported locales equivalent to the given locale.
### Getting results
- [SpeechTranscriber.Result](speechtranscriber/result.md)
  A phrase or passage of transcribed speech. The phrases are sent in order.

## Relationships

### Conforms To
- [LocaleDependentSpeechModule](localedependentspeechmodule.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SpeechModule](speechmodule.md)

## See Also

- [class DictationTranscriber](dictationtranscriber.md)
  A speech-to-text transcription module that’s similar to system dictation features and compatible with older devices.
- [class SpeechDetector](speechdetector.md)
  A module that performs a voice activity detection (VAD) analysis.
- [protocol SpeechModule](speechmodule.md)
  Protocol that all analyzer modules conform to.
- [protocol LocaleDependentSpeechModule](localedependentspeechmodule.md)
  A module that requires locale-specific assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechtranscriber)*