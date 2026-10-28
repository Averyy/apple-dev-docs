# speechRecognitionTaskWasCancelled(_:)

**Framework**: Speech  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the task has been canceled.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
optional func speechRecognitionTaskWasCancelled(_ task: SFSpeechRecognitionTask)
```

```objc
- (void) speechRecognitionTaskWasCancelled:(SFSpeechRecognitionTask *) task;
```

## Discussion

A speech recognition task can be canceled by the user, by your app, or by the system.

## Parameters

- `task`: The speech recognition task (an [`SFSpeechRecognitionTask`](../sfspeechrecognitiontask.md) object) that represents the request.

## See Also

### Finishing a speech recognition task
- [func speechRecognitionTask(SFSpeechRecognitionTask, didFinishRecognition: SFSpeechRecognitionResult)](./speechrecognitiontask%28_,didfinishrecognition%29.md)
  Tells the delegate when the final utterance is recognized.
- [func speechRecognitionTask(SFSpeechRecognitionTask, didFinishSuccessfully: Bool)](./speechrecognitiontask%28_,didfinishsuccessfully%29.md)
  Tells the delegate when the recognition of all requested utterances is finished.
- [func speechRecognitionTask(SFSpeechRecognitionTask, didProcessAudioDuration: TimeInterval)](./speechrecognitiontask%28_,didprocessaudioduration%29.md)
  Tells the delegate how much audio has been processed by the task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskdelegate/speechrecognitiontaskwascancelled(_:))*