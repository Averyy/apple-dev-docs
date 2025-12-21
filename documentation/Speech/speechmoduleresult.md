# SpeechModuleResult

**Framework**: Speech  
**Kind**: protocol

Protocol that all module results conform to.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol SpeechModuleResult
```

## Topics

### Getting audio range
- [var range: CMTimeRange](speechmoduleresult/range.md)
  The audio input range that this result applies to.
### Getting finalization state
- [var isFinal: Bool](speechmoduleresult/isfinal.md)
  Whether this result is final at the time it is produced.
- [var resultsFinalizationTime: CMTime](speechmoduleresult/resultsfinalizationtime.md)
  The audio input time up to which results from this module have been finalized (after this result). The module’s results are final up to but not including this time.

## Relationships

### Conforming Types
- [DictationTranscriber.Result](dictationtranscriber/result.md)
- [SpeechDetector.Result](speechdetector/result.md)
- [SpeechTranscriber.Result](speechtranscriber/result.md)

## See Also

- [struct AnalyzerInput](analyzerinput.md)
  Time-coded audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechmoduleresult)*