# speechRecognitionTaskWasCancelled(_:)

**Framework**: Speech  
**Kind**: method

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

#### Discussion

A speech recognition task can be canceled by the user, by your app, or by the system.

## Parameters

- `task`: The speech recognition task (an   object) that represents the request.

## See Also

- [func speechRecognitionTask(SFSpeechRecognitionTask, didFinishRecognition: SFSpeechRecognitionResult)](sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didfinishrecognition:).md)
  Tells the delegate when the final utterance is recognized.
- [func speechRecognitionTask(SFSpeechRecognitionTask, didFinishSuccessfully: Bool)](sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didfinishsuccessfully:).md)
  Tells the delegate when the recognition of all requested utterances is finished.
- [func speechRecognitionTask(SFSpeechRecognitionTask, didProcessAudioDuration: TimeInterval)](sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didprocessaudioduration:).md)
  Tells the delegate how much audio has been processed by the task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskdelegate/speechrecognitiontaskwascancelled(_:))*