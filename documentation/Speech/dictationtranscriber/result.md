# DictationTranscriber.Result

**Framework**: Speech  
**Kind**: struct

A phrase or passage of transcribed speech. The phrases are sent in order.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Result
```

#### Overview

If the transcriber is configured to send volatile results, each phrase is sent one or more times as the interpretation gets better and better until it is finalized.

## Topics

### Getting transcriptions
- [let alternatives: [AttributedString]](dictationtranscriber/result/alternatives.md)
  All the alternative interpretations of the audio in this range. The interpretations are in descending order of likelihood.
- [var text: AttributedString](dictationtranscriber/result/text.md)
  The most likely interpretation of the audio in this range.
### Working with transcriptions
- [AttributeScopes.SpeechAttributes.TimeRangeAttribute](../foundation/attributescopes/speechattributes/timerangeattribute.md)
  The time range in the source audio corresponding to the associated transcription text.
- [AttributeScopes.SpeechAttributes.ConfidenceAttribute](../foundation/attributescopes/speechattributes/confidenceattribute.md)
  A confidence level (0–1) of the associated transcription text.
- [func rangeOfAudioTimeRangeAttributes(intersecting: CMTimeRange) -> Range<AttributedString.Index>?](../foundation/attributedstring/rangeofaudiotimerangeattributes(intersecting:).md)
  Returns the range of the attributed string that is within the given time range.
### Getting audio range
- [var range: CMTimeRange](speechmoduleresult/range.md)
  The audio input range that this result applies to.
### Getting finalization state
- [var isFinal: Bool](speechmoduleresult/isfinal.md)
  Whether this result is final at the time it is produced.
- [var resultsFinalizationTime: CMTime](speechmoduleresult/resultsfinalizationtime.md)
  The audio input time up to which results from this module have been finalized (after this result). The module’s results are final up to but not including this time.

## Relationships

### Conforms To
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SpeechModuleResult](speechmoduleresult.md)

## See Also

- [var results: some Sendable & AsyncSequence<DictationTranscriber.Result, any Error>](dictationtranscriber/results.md)
  The asynchronous sequence of transcription results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber/result)*