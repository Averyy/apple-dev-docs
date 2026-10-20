# speechRecognitionTask(_:didFinishSuccessfully:)

**Framework**: Speech  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the recognition of all requested utterances is finished.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
optional func speechRecognitionTask(_ task: SFSpeechRecognitionTask, didFinishSuccessfully successfully: Bool)
```

```objc
- (void) speechRecognitionTask:(SFSpeechRecognitionTask *) task didFinishSuccessfully:(BOOL) successfully;
```

## Parameters

- `task`: The speech recognition task (an [`SFSpeechRecognitionTask`](../sfspeechrecognitiontask.md) object) that represents the request.
- `successfully`: A Boolean value that indicates whether the task was successful. When this parameter is `false`, use the [`error`](../sfspeechrecognitiontask/error.md) property of the task to get information about why the task was unsuccessful.

## See Also

### Finishing a speech recognition task
- [func speechRecognitionTask(SFSpeechRecognitionTask, didFinishRecognition: SFSpeechRecognitionResult)](./speechrecognitiontask%28_,didfinishrecognition%29.md)
  Tells the delegate when the final utterance is recognized.
- [func speechRecognitionTask(SFSpeechRecognitionTask, didProcessAudioDuration: TimeInterval)](./speechrecognitiontask%28_,didprocessaudioduration%29.md)
  Tells the delegate how much audio has been processed by the task.
- [func speechRecognitionTaskWasCancelled(SFSpeechRecognitionTask)](./speechrecognitiontaskwascancelled%28_%29.md)
  Tells the delegate that the task has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didfinishsuccessfully:))*