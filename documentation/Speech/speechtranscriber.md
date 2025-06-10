# SpeechTranscriber

**Framework**: Speech  
**Kind**: class

A module that transcribes speech to text. This transcriber is appropriate for normal conversation and general purposes.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final class SpeechTranscriber
```

#### Overview

Several transcriber instances can share the same backing engine instances and models, so long as the transcribers are configured similarly in certain respects.

## Topics

### Structures
- [SpeechTranscriber.Preset](speechtranscriber/preset.md)
  Predefined transcriber configurations.
- [SpeechTranscriber.Result](speechtranscriber/result.md)
  A phrase or passage of transcribed speech. The phrases are sent in order.
### Initializers
- [convenience init(locale: Locale, preset: SpeechTranscriber.Preset)](speechtranscriber/init(locale:preset:).md)
  Creates a general-purpose transcriber according to a preset.
- [convenience init(locale: Locale, transcriptionOptions: Set<SpeechTranscriber.TranscriptionOption>, reportingOptions: Set<SpeechTranscriber.ReportingOption>, attributeOptions: Set<SpeechTranscriber.ResultAttributeOption>)](speechtranscriber/init(locale:transcriptionoptions:reportingoptions:attributeoptions:).md)
  Creates a general-purpose transcriber.
### Type Properties
- [static var installedLocales: [Locale]](speechtranscriber/installedlocales.md)
  The locales that the transcriber can transcribe into, considering only locales that are installed on the device.
- [static var supportedLocales: [Locale]](speechtranscriber/supportedlocales.md)
  The locales that the transcriber can transcribe into, including locales that may not be installed but are downloadable.
### Enumerations
- [SpeechTranscriber.ReportingOption](speechtranscriber/reportingoption.md)
  Options relating to the transcriber’s result delivery.
- [SpeechTranscriber.ResultAttributeOption](speechtranscriber/resultattributeoption.md)
  Options relating to the attributes of the transcription.
- [SpeechTranscriber.TranscriptionOption](speechtranscriber/transcriptionoption.md)
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
- [class DictationTranscriber](dictationtranscriber.md)
  A module that transcribes speech to text. This transcriber is used by [`SFSpeechRecognizer`](sfspeechrecognizer.md) and system dictation features.
- [class SpeechDetector](speechdetector.md)
  A module that performs a voice activity detection (VAD) analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechtranscriber)*