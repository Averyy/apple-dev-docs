# SFTranscription

**Framework**: Speech  
**Kind**: class

A textual representation of the specified speech in its entirety, as recognized by the speech recognizer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class SFTranscription
```

#### Overview

Use `SFTranscription` to obtain all the recognized utterances from your audio content. An  is a vocalized word or group of words that represent a single meaning to the speech recognizer ([`SFSpeechRecognizer`](sfspeechrecognizer.md)).

Use the [`formattedString`](sftranscription/formattedstring.md) property to retrieve the entire transcription of utterances, or use the [`segments`](sftranscription/segments.md) property to retrieve an individual utterance ([`SFTranscriptionSegment`](sftranscriptionsegment.md)).

You don’t create an `SFTranscription` directly. Instead, you retrieve it from an [`SFSpeechRecognitionResult`](sfspeechrecognitionresult.md) instance. The speech recognizer sends a speech recognition result to your app in one of two ways, depending on how your app started a speech recognition task.

You can start a speech recognition task by using the speech recognizer’s [`recognitionTask(with:resultHandler:)`](sfspeechrecognizer/recognitiontask(with:resulthandler:).md) method. When the task is complete, the speech recognizer sends an [`SFSpeechRecognitionResult`](sfspeechrecognitionresult.md) instance to your `resultHandler` closure. Alternatively, you can use the speech recognizer’s [`recognitionTask(with:delegate:)`](sfspeechrecognizer/recognitiontask(with:delegate:).md) method to start a speech recognition task. When the task is complete, the speech recognizer uses your [`SFSpeechRecognitionTaskDelegate`](sfspeechrecognitiontaskdelegate.md) to send an [`SFSpeechRecognitionResult`](sfspeechrecognitionresult.md) by using the delegate’s [`speechRecognitionTask(_:didFinishRecognition:)`](sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didfinishrecognition:).md) method.

An `SFTranscription` represents only a potential version of the speech. It might not be an accurate representation of the utterances.

## Topics

### Transcribing the Utterances
- [var formattedString: String](sftranscription/formattedstring.md)
  The entire transcription of utterances, formatted into a single, user-displayable string.
### Getting Individual Utterances
- [var segments: [SFTranscriptionSegment]](sftranscription/segments.md)
  An array of transcription segments that represent the parts of the transcription, as identified by the speech recognizer.
### Deprecated
- [var averagePauseDuration: TimeInterval](sftranscription/averagepauseduration.md)
  The average pause duration between words, measured in seconds.
- [var speakingRate: Double](sftranscription/speakingrate.md)
  The number of words spoken per minute.

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
- [class SFTranscriptionSegment](sftranscriptionsegment.md)
  A discrete part of an entire transcription, as identified by the speech recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sftranscription)*