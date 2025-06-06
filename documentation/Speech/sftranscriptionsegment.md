# SFTranscriptionSegment

**Framework**: Speech  
**Kind**: class

A discrete part of an entire transcription, as identified by the speech recognizer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class SFTranscriptionSegment
```

#### Overview

Use [`SFTranscriptionSegment`](sftranscriptionsegment.md) to get details about a part of an overall [`SFTranscription`](sftranscription.md). An [`SFTranscriptionSegment`](sftranscriptionsegment.md) represents an utterance, which is a vocalized word or group of words that represent a single meaning to the speech recognizer ([`SFSpeechRecognizer`](sfspeechrecognizer.md)).

You don’t create transcription object segments directly. Instead, you access them from a transcription’s [`segments`](sftranscription/segments.md) property.

A transcription segment includes the following information:

- The text of the utterance, plus any alternative interpretations of the spoken word.
- The character range of the segment within the [`formattedString`](sftranscription/formattedstring.md) of its parent [`SFTranscription`](sftranscription.md).
- A [`confidence`](sftranscriptionsegment/confidence.md) value, indicating how likely it is that the specified string matches the audible speech.
- A [`timestamp`](sftranscriptionsegment/timestamp.md) and [`duration`](sftranscriptionsegment/duration.md) value, indicating the position of the segment within the provided audio stream.

## Topics

### Transcribing the Segment
- [var substring: String](sftranscriptionsegment/substring.md)
  The string representation of the utterance in the transcription segment.
- [var substringRange: NSRange](sftranscriptionsegment/substringrange.md)
  The range information for the transcription segment’s substring, relative to the overall transcription.
- [var alternativeSubstrings: [String]](sftranscriptionsegment/alternativesubstrings.md)
  An array of alternate interpretations of the utterance in the transcription segment.
### Assessing the Recognition Confidence Level
- [var confidence: Float](sftranscriptionsegment/confidence.md)
  The level of confidence the speech recognizer has in its recognition of the speech transcribed for the segment.
### Getting the Audio Timing Information
- [var timestamp: TimeInterval](sftranscriptionsegment/timestamp.md)
  The start time of the segment in the processed audio stream.
- [var duration: TimeInterval](sftranscriptionsegment/duration.md)
  The number of seconds it took for the user to speak the utterance represented by the segment.
### Deprecated
- [var voiceAnalytics: SFVoiceAnalytics?](sftranscriptionsegment/voiceanalytics.md)
  An analysis of the transcription segment’s vocal properties.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class SFSpeechRecognitionResult](sfspeechrecognitionresult.md)
  An object that contains the partial or final results of a speech recognition request.
- [class SFSpeechRecognitionMetadata](sfspeechrecognitionmetadata.md)
  The metadata of speech in the audio of a speech recognition request.
- [class SFTranscription](sftranscription.md)
  A textual representation of the specified speech in its entirety, as recognized by the speech recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sftranscriptionsegment)*