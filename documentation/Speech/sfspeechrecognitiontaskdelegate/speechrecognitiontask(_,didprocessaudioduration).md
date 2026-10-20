# speechRecognitionTask(_:didProcessAudioDuration:)

**Framework**: Speech  
**Kind**: method  
**Role**: Instance Method

Tells the delegate how much audio has been processed by the task.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
optional func speechRecognitionTask(_ task: SFSpeechRecognitionTask, didProcessAudioDuration duration: TimeInterval)
```

```objc
- (void) speechRecognitionTask:(SFSpeechRecognitionTask *) task didProcessAudioDuration:(NSTimeInterval) duration;
```

## Parameters

- `task`: The speech recognition task (an [`SFSpeechRecognitionTask`](../sfspeechrecognitiontask.md) object) that represents the request.
- `duration`: The seconds of audio input that the recognizer has processed.

## See Also

### Finishing a speech recognition task
- [func speechRecognitionTask(SFSpeechRecognitionTask, didFinishRecognition: SFSpeechRecognitionResult)](./speechrecognitiontask%28_,didfinishrecognition%29.md)
  Tells the delegate when the final utterance is recognized.
- [func speechRecognitionTask(SFSpeechRecognitionTask, didFinishSuccessfully: Bool)](./speechrecognitiontask%28_,didfinishsuccessfully%29.md)
  Tells the delegate when the recognition of all requested utterances is finished.
- [func speechRecognitionTaskWasCancelled(SFSpeechRecognitionTask)](./speechrecognitiontaskwascancelled%28_%29.md)
  Tells the delegate that the task has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didprocessaudioduration:))*