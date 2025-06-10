# speechRecognitionTask(_:didProcessAudioDuration:)

**Framework**: Speech  
**Kind**: method

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

## Parameters

- `task`: The speech recognition task (an   object) that represents the request.
- `duration`: The seconds of audio input that the recognizer has processed.

## See Also

- [func speechRecognitionTask(SFSpeechRecognitionTask, didFinishRecognition: SFSpeechRecognitionResult)](sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didfinishrecognition:).md)
  Tells the delegate when the final utterance is recognized.
- [func speechRecognitionTask(SFSpeechRecognitionTask, didFinishSuccessfully: Bool)](sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didfinishsuccessfully:).md)
  Tells the delegate when the recognition of all requested utterances is finished.
- [func speechRecognitionTaskWasCancelled(SFSpeechRecognitionTask)](sfspeechrecognitiontaskdelegate/speechrecognitiontaskwascancelled(_:).md)
  Tells the delegate that the task has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didprocessaudioduration:))*