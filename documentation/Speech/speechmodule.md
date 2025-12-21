# SpeechModule

**Framework**: Speech  
**Kind**: protocol

Protocol that all analyzer modules conform to.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol SpeechModule : AnyObject, Sendable
```

## Topics

### Checking audio format support
- [var availableCompatibleAudioFormats: [AVAudioFormat]](speechmodule/availablecompatibleaudioformats.md)
  The audio formats that this module is able to analyze, given its configuration.
### Getting results
- [var results: Self.Results](speechmodule/results-swift.property.md)
  An asynchronous sequence containing this module’s analysis results. Results are added to the sequence as they are created.
- [associatedtype Result : SpeechModuleResult, Sendable](speechmodule/result.md)
- [associatedtype Results : Sendable, AsyncSequence](speechmodule/results-swift.associatedtype.md)

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Inherited By
- [LocaleDependentSpeechModule](localedependentspeechmodule.md)
### Conforming Types
- [DictationTranscriber](dictationtranscriber.md)
- [SpeechDetector](speechdetector.md)
- [SpeechTranscriber](speechtranscriber.md)

## See Also

- [class SpeechTranscriber](speechtranscriber.md)
  A speech-to-text transcription module that’s appropriate for normal conversation and general purposes.
- [class DictationTranscriber](dictationtranscriber.md)
  A speech-to-text transcription module that’s similar to system dictation features and compatible with older devices.
- [class SpeechDetector](speechdetector.md)
  A module that performs a voice activity detection (VAD) analysis.
- [protocol LocaleDependentSpeechModule](localedependentspeechmodule.md)
  A module that requires locale-specific assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechmodule)*