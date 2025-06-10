# SpeechModule

**Framework**: Speech  
**Kind**: protocol

Protocol that all analyzer modules conform to.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol SpeechModule : AnyObject, Sendable
```

## Topics

### Associated Types
- [associatedtype Result : SpeechModuleResult, Sendable](speechmodule/result.md)
- [associatedtype Results : Sendable, AsyncSequence](speechmodule/results-swift.associatedtype.md)
### Instance Properties
- [var availableCompatibleAudioFormats: [AVAudioFormat]](speechmodule/availablecompatibleaudioformats.md)
  The audio formats that this module is able to analyze, given its configuration.
- [var results: Self.Results](speechmodule/results-swift.property.md)
  An asynchronous sequence containing this module’s analysis results. Results are added to the sequence as they are created.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Inherited By
- [LocaleDependentSpeechModule](localedependentspeechmodule.md)
### Conforming Types
- [DictationTranscriber](dictationtranscriber.md)
- [SpeechTranscriber](speechtranscriber.md)

## See Also

- [protocol LocaleDependentSpeechModule](localedependentspeechmodule.md)
  If a module conforms to this protocol, then its assets depend on the locale setting.
- [class SpeechTranscriber](speechtranscriber.md)
  A module that transcribes speech to text. This transcriber is appropriate for normal conversation and general purposes.
- [class DictationTranscriber](dictationtranscriber.md)
  A module that transcribes speech to text. This transcriber is used by [`SFSpeechRecognizer`](sfspeechrecognizer.md) and system dictation features.
- [class SpeechDetector](speechdetector.md)
  A module that performs a voice activity detection (VAD) analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechmodule)*