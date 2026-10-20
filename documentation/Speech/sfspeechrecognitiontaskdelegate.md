# SFSpeechRecognitionTaskDelegate

**Framework**: Speech  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol SFSpeechRecognitionTaskDelegate <NSObject>
```

#### Overview

The methods of this protocol give you fine-grained control over the speech recognition process. Specifically, you use this protocol when you want to know the following:

- When the first utterances of speech occur in the audio.
- When the speech recognizer stops accepting audio.
- When the speech recognition process finishes or is canceled.
- When the speech recognizer generates a potential transcription.

Adopt the methods of this protocol in an object and pass that object in to the `delegate` parameter of [`recognitionTask(with:delegate:)`](./sfspeechrecognizer/recognitiontask%28with,delegate%29.md) when starting your speech recognition task.

## Topics

### Tracking task progress
- [func speechRecognitionDidDetectSpeech(SFSpeechRecognitionTask)](./sfspeechrecognitiontaskdelegate/speechrecognitiondiddetectspeech%28_%29.md)
  Tells the delegate when the task first detects speech in the source audio.
- [func speechRecognitionTaskFinishedReadingAudio(SFSpeechRecognitionTask)](./sfspeechrecognitiontaskdelegate/speechrecognitiontaskfinishedreadingaudio%28_%29.md)
  Tells the delegate when the task is no longer accepting new audio input, even if final processing is in progress.
### Getting transcriptions
- [func speechRecognitionTask(SFSpeechRecognitionTask, didHypothesizeTranscription: SFTranscription)](./sfspeechrecognitiontaskdelegate/speechrecognitiontask%28_,didhypothesizetranscription%29.md)
  Tells the delegate that a hypothesized transcription is available.
### Finishing a speech recognition task
- [func speechRecognitionTask(SFSpeechRecognitionTask, didFinishRecognition: SFSpeechRecognitionResult)](./sfspeechrecognitiontaskdelegate/speechrecognitiontask%28_,didfinishrecognition%29.md)
  Tells the delegate when the final utterance is recognized.
- [func speechRecognitionTask(SFSpeechRecognitionTask, didFinishSuccessfully: Bool)](./sfspeechrecognitiontaskdelegate/speechrecognitiontask%28_,didfinishsuccessfully%29.md)
  Tells the delegate when the recognition of all requested utterances is finished.
- [func speechRecognitionTask(SFSpeechRecognitionTask, didProcessAudioDuration: TimeInterval)](./sfspeechrecognitiontaskdelegate/speechrecognitiontask%28_,didprocessaudioduration%29.md)
  Tells the delegate how much audio has been processed by the task.
- [func speechRecognitionTaskWasCancelled(SFSpeechRecognitionTask)](./sfspeechrecognitiontaskdelegate/speechrecognitiontaskwascancelled%28_%29.md)
  Tells the delegate that the task has been canceled.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### In-progress requests
- [class SFSpeechRecognitionTask](./sfspeechrecognitiontask.md)
  A task object for monitoring the speech recognition progress.
- [enum SFSpeechRecognitionTaskState](./sfspeechrecognitiontaskstate.md)
  The state of the task associated with the recognition request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskdelegate)*