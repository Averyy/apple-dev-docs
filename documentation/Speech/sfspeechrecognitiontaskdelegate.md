# SFSpeechRecognitionTaskDelegate

**Framework**: Speech  
**Kind**: protocol

A protocol with methods for managing multi-utterance speech recognition requests.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
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

### Tracking the Task Progress
- [func speechRecognitionDidDetectSpeech(SFSpeechRecognitionTask)](sfspeechrecognitiontaskdelegate/speechrecognitiondiddetectspeech(_:).md)
  Tells the delegate when the task first detects speech in the source audio.
- [func speechRecognitionTaskFinishedReadingAudio(SFSpeechRecognitionTask)](sfspeechrecognitiontaskdelegate/speechrecognitiontaskfinishedreadingaudio(_:).md)
  Tells the delegate when the task is no longer accepting new audio input, even if final processing is in progress.
### Getting Transcriptions
- [func speechRecognitionTask(SFSpeechRecognitionTask, didHypothesizeTranscription: SFTranscription)](sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didhypothesizetranscription:).md)
  Tells the delegate that a hypothesized transcription is available.
### Finishing a Speech Recognition Task
- [func speechRecognitionTask(SFSpeechRecognitionTask, didFinishRecognition: SFSpeechRecognitionResult)](sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didfinishrecognition:).md)
  Tells the delegate when the final utterance is recognized.
- [func speechRecognitionTask(SFSpeechRecognitionTask, didFinishSuccessfully: Bool)](sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didfinishsuccessfully:).md)
  Tells the delegate when the recognition of all requested utterances is finished.
- [func speechRecognitionTaskWasCancelled(SFSpeechRecognitionTask)](sfspeechrecognitiontaskdelegate/speechrecognitiontaskwascancelled(_:).md)
  Tells the delegate that the task has been canceled.
### Instance Methods
- [func speechRecognitionTask(SFSpeechRecognitionTask, didProcessAudioDuration: TimeInterval)](sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didprocessaudioduration:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func recognitionTask(with: SFSpeechRecognitionRequest, resultHandler: (SFSpeechRecognitionResult?, (any Error)?) -> Void) -> SFSpeechRecognitionTask](sfspeechrecognizer/recognitiontask(with:resulthandler:).md)
  Executes the speech recognition request and delivers the results to the specified handler block.
- [func recognitionTask(with: SFSpeechRecognitionRequest, delegate: any SFSpeechRecognitionTaskDelegate) -> SFSpeechRecognitionTask](sfspeechrecognizer/recognitiontask(with:delegate:).md)
  Recognizes speech from the audio source associated with the specified request, using the specified delegate to manage the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskdelegate)*