# SpeechDetector

**Framework**: Speech  
**Kind**: class

A module that performs a voice activity detection (VAD) analysis.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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

> **Note**: For certain use cases, such as those that include a lot of silence, it might be tempting to always enable VAD gating. In theory, this would preserve power by only running ASR’s speech transcription models when it is highly likely for there to be speech to transcribe. However, this introduces the potential for degraded accuracy if the VAD model is too aggressive and drops audio that does contain speech. This is an area of future exploration with ongoing experiments.

## Topics

### Structures
- [SpeechDetector.DetectionOptions](speechdetector/detectionoptions.md)
  Allows clients to customize an instance of a speech detector.
- [SpeechDetector.Result](speechdetector/result.md)
  A result from the speech detector.
### Initializers
- [convenience init()](speechdetector/init.md)
  Creates a speech detector with default settings.
- [init(detectionOptions: SpeechDetector.DetectionOptions, reportResults: Bool)](speechdetector/init(detectionoptions:reportresults:).md)
  Creates a speech detector.
### Instance Properties
- [var availableCompatibleAudioFormats: [AVAudioFormat]](speechdetector/availablecompatibleaudioformats.md)
- [var results: some Sendable & AsyncSequence<SpeechDetector.Result, any Error>](speechdetector/results-swift.property.md)
### Type Aliases
- [SpeechDetector.Results](speechdetector/results-swift.typealias.md)
### Enumerations
- [SpeechDetector.SensitivityLevel](speechdetector/sensitivitylevel.md)
  Determines how “aggressive” the voice activity detection (VAD) model will be.

## See Also

- [protocol SpeechModule](speechmodule.md)
  Protocol that all analyzer modules conform to.
- [protocol LocaleDependentSpeechModule](localedependentspeechmodule.md)
  If a module conforms to this protocol, then its assets depend on the locale setting.
- [class SpeechTranscriber](speechtranscriber.md)
  A module that transcribes speech to text. This transcriber is appropriate for normal conversation and general purposes.
- [class DictationTranscriber](dictationtranscriber.md)
  A module that transcribes speech to text. This transcriber is used by `SFSpeechRecognizer` and system dictation features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechdetector)*