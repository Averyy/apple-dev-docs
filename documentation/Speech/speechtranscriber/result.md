# SpeechTranscriber.Result

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
- [let alternatives: [AttributedString]](speechtranscriber/result/alternatives.md)
  All the alternative interpretations of the audio in this range. The interpretations are in descending order of likelihood.
- [var text: AttributedString](speechtranscriber/result/text.md)
  The most likely interpretation of the audio in this range.
### Working with transcriptions
- [AttributeScopes.SpeechAttributes.TimeRangeAttribute](../Foundation/AttributeScopes/SpeechAttributes/TimeRangeAttribute.md)
  The time range in the source audio corresponding to the associated transcription text.
- [AttributeScopes.SpeechAttributes.ConfidenceAttribute](../Foundation/AttributeScopes/SpeechAttributes/ConfidenceAttribute.md)
  A confidence level (0–1) of the associated transcription text.
- [func rangeOfAudioTimeRangeAttributes(intersecting: CMTimeRange) -> Range<AttributedString.Index>?](../Foundation/AttributedString/rangeOfAudioTimeRangeAttributes(intersecting:).md)
  Returns the range of indices of the receiver that are part of given time range.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SpeechModuleResult](speechmoduleresult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechtranscriber/result)*