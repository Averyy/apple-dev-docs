# speechRecognitionTask(_:didFinishSuccessfully:)

**Framework**: Speech  
**Kind**: method

Tells the delegate when the recognition of all requested utterances is finished.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
optional func speechRecognitionTask(_ task: SFSpeechRecognitionTask, didFinishSuccessfully successfully: Bool)
```

## Parameters

- `task`: The speech recognition task (an   object) that represents the request.
- `successfully`: A Boolean value that indicates whether the task was successful. When this parameter is  , use the   property of the task to get information about why the task was unsuccessful.

## See Also

- [func speechRecognitionTask(SFSpeechRecognitionTask, didFinishRecognition: SFSpeechRecognitionResult)](sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didfinishrecognition:).md)
  Tells the delegate when the final utterance is recognized.
- [func speechRecognitionTaskWasCancelled(SFSpeechRecognitionTask)](sfspeechrecognitiontaskdelegate/speechrecognitiontaskwascancelled(_:).md)
  Tells the delegate that the task has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didfinishsuccessfully:))*