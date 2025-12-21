# SpeechDetector

**Framework**: Speech  
**Kind**: class

A module that performs a voice activity detection (VAD) analysis.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final class SpeechDetector
```

#### Overview

This module asks “is there speech?” and provides you with the ability to gate transcription by the presence of voices, saving power otherwise used by attempting to transcribe what is likely to be silence.

To enable voice activated transcription, initialize a [`SpeechDetector`](speechdetector.md) module. Like any other module, it can be set when first initializing SpeechAnalyzer:

```None
let transcriber = SpeechTranscriber(..)
let speechDetector = SpeechDetector()
let analyzer = SpeechAnalyzer(.., modules: [speechDetector, transcriber])
```

or later on with [`setModules(_:)`](speechanalyzer/setmodules(_:).md):

```None
let analyzer = SpeechAnalyzer(..)
let transcriber = SpeechTranscriber(..)
let speechDetector = SpeechDetector()
try await analyzer.setModules([transcriber, speechDetector])
```

> ❗ **Important**: This module only functions in conjunction with a [`SpeechTranscriber`](speechtranscriber.md) or [`DictationTranscriber`](dictationtranscriber.md) module.

> **Note**: For certain use cases, such as those with a lot of silence, it might be tempting to always enable voice activated transcription. But if the model drops audio that does contain speech, there could be a tradeoff between the power being saved by always having VAD enabled and potentially lower accuracy transcriptions. You can set the aggressiveness of the VAD model with [`SpeechDetector.SensitivityLevel`](speechdetector/sensitivitylevel.md). While [`SpeechDetector.SensitivityLevel.medium`](speechdetector/sensitivitylevel/medium.md) is recommended for most use cases, the value of these tradeoffs will be context-specific.

## Topics

### Creating a detector
- [convenience init()](speechdetector/init.md)
  Creates a speech detector with default settings.
- [init(detectionOptions: SpeechDetector.DetectionOptions, reportResults: Bool)](speechdetector/init(detectionoptions:reportresults:).md)
  Creates a speech detector.
- [SpeechDetector.DetectionOptions](speechdetector/detectionoptions.md)
  Allows clients to customize an instance of a speech detector.
- [SpeechDetector.SensitivityLevel](speechdetector/sensitivitylevel.md)
  Determines how “aggressive” the voice activity detection (VAD) model will be.
### Getting results
- [SpeechDetector.Result](speechdetector/result.md)
  A result from the speech detector. Please note, these must be enabled via [`init(detectionOptions:reportResults:)`](speechdetector/init(detectionoptions:reportresults:).md) and currently only support error handling from the VAD model.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SpeechModule](speechmodule.md)

## See Also

- [class SpeechTranscriber](speechtranscriber.md)
  A speech-to-text transcription module that’s appropriate for normal conversation and general purposes.
- [class DictationTranscriber](dictationtranscriber.md)
  A speech-to-text transcription module that’s similar to system dictation features and compatible with older devices.
- [protocol SpeechModule](speechmodule.md)
  Protocol that all analyzer modules conform to.
- [protocol LocaleDependentSpeechModule](localedependentspeechmodule.md)
  A module that requires locale-specific assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechdetector)*