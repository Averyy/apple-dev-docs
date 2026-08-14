# SFSpeechRecognitionMetadata

**Framework**: Speech  
**Kind**: class

The metadata of speech in the audio of a speech recognition request.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class SFSpeechRecognitionMetadata
```

## Topics

### Getting audio timing information
- [var averagePauseDuration: TimeInterval](sfspeechrecognitionmetadata/averagepauseduration.md)
  The average pause duration between words, measured in seconds.
- [var speakingRate: Double](sfspeechrecognitionmetadata/speakingrate.md)
  The number of words spoken per minute.
- [var speechDuration: TimeInterval](sfspeechrecognitionmetadata/speechduration.md)
  The duration in seconds of speech in the audio.
- [var speechStartTimestamp: TimeInterval](sfspeechrecognitionmetadata/speechstarttimestamp.md)
  The start timestamp of speech in the audio.
### Analyzing voice
- [var voiceAnalytics: SFVoiceAnalytics?](sfspeechrecognitionmetadata/voiceanalytics.md)
  An analysis of the transcription segment’s vocal properties.
### Initializers
- [init?(coder: NSCoder)](sfspeechrecognitionmetadata/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class SFSpeechRecognitionResult](sfspeechrecognitionresult.md)
  An object that contains the partial or final results of a speech recognition request.
- [class SFTranscription](sftranscription.md)
  A textual representation of the specified speech in its entirety, as recognized by the speech recognizer.
- [class SFTranscriptionSegment](sftranscriptionsegment.md)
  A discrete part of an entire transcription, as identified by the speech recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitionmetadata)*