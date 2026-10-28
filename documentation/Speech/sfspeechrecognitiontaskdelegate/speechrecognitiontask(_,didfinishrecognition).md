# speechRecognitionTask(_:didFinishRecognition:)

**Framework**: Speech  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the final utterance is recognized.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
optional func speechRecognitionTask(_ task: SFSpeechRecognitionTask, didFinishRecognition recognitionResult: SFSpeechRecognitionResult)
```

```objc
- (void) speechRecognitionTask:(SFSpeechRecognitionTask *) task didFinishRecognition:(SFSpeechRecognitionResult *) recognitionResult;
```

## Discussion

When this method is called, the delegate should expect no further information about the utterance to be reported.

## Parameters

- `task`: The speech recognition task (an [`SFSpeechRecognitionTask`](../sfspeechrecognitiontask.md) object) that represents the request.
- `recognitionResult`: A recognized utterance that contains one or more transcription hypotheses in an [`SFSpeechRecognitionResult`](../sfspeechrecognitionresult.md) object.

## See Also

### Finishing a speech recognition task
- [func speechRecognitionTask(SFSpeechRecognitionTask, didFinishSuccessfully: Bool)](./speechrecognitiontask%28_,didfinishsuccessfully%29.md)
  Tells the delegate when the recognition of all requested utterances is finished.
- [func speechRecognitionTask(SFSpeechRecognitionTask, didProcessAudioDuration: TimeInterval)](./speechrecognitiontask%28_,didprocessaudioduration%29.md)
  Tells the delegate how much audio has been processed by the task.
- [func speechRecognitionTaskWasCancelled(SFSpeechRecognitionTask)](./speechrecognitiontaskwascancelled%28_%29.md)
  Tells the delegate that the task has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didfinishrecognition:))*