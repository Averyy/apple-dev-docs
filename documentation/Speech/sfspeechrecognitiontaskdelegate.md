# SFSpeechRecognitionTaskDelegate

**Framework**: Speech  
**Kind**: protocol

A protocol with methods for managing multi-utterance speech recognition requests.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
protocol SFSpeechRecognitionTaskDelegate : NSObjectProtocol
```

#### Overview

The methods of this protocol give you fine-grained control over the speech recognition process. Specifically, you use this protocol when you want to know the following:

- When the first utterances of speech occur in the audio.
- When the speech recognizer stops accepting audio.
- When the speech recognition process finishes or is canceled.
- When the speech recognizer generates a potential transcription.

Adopt the methods of this protocol in an object and pass that object in to the `delegate` parameter of [`recognitionTask(with:delegate:)`](sfspeechrecognizer/recognitiontask(with:delegate:).md) when starting your speech recognition task.

## Topics

### Tracking task progress
- [func speechRecognitionDidDetectSpeech(SFSpeechRecognitionTask)](sfspeechrecognitiontaskdelegate/speechrecognitiondiddetectspeech(_:).md)
  Tells the delegate when the task first detects speech in the source audio.
- [func speechRecognitionTaskFinishedReadingAudio(SFSpeechRecognitionTask)](sfspeechrecognitiontaskdelegate/speechrecognitiontaskfinishedreadingaudio(_:).md)
  Tells the delegate when the task is no longer accepting new audio input, even if final processing is in progress.
### Getting transcriptions
- [func speechRecognitionTask(SFSpeechRecognitionTask, didHypothesizeTranscription: SFTranscription)](sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didhypothesizetranscription:).md)
  Tells the delegate that a hypothesized transcription is available.
### Finishing a speech recognition task
- [func speechRecognitionTask(SFSpeechRecognitionTask, didFinishRecognition: SFSpeechRecognitionResult)](sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didfinishrecognition:).md)
  Tells the delegate when the final utterance is recognized.
- [func speechRecognitionTask(SFSpeechRecognitionTask, didFinishSuccessfully: Bool)](sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didfinishsuccessfully:).md)
  Tells the delegate when the recognition of all requested utterances is finished.
- [func speechRecognitionTask(SFSpeechRecognitionTask, didProcessAudioDuration: TimeInterval)](sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didprocessaudioduration:).md)
  Tells the delegate how much audio has been processed by the task.
- [func speechRecognitionTaskWasCancelled(SFSpeechRecognitionTask)](sfspeechrecognitiontaskdelegate/speechrecognitiontaskwascancelled(_:).md)
  Tells the delegate that the task has been canceled.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class SFSpeechRecognitionTask](sfspeechrecognitiontask.md)
  A task object for monitoring the speech recognition progress.
- [enum SFSpeechRecognitionTaskState](sfspeechrecognitiontaskstate.md)
  The state of the task associated with the recognition request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskdelegate)*