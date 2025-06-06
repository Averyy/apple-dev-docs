# speechRecognitionTask(_:didFinishRecognition:)

**Framework**: Speech  
**Kind**: method

Tells the delegate when the final utterance is recognized.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
optional func speechRecognitionTask(_ task: SFSpeechRecognitionTask, didFinishRecognition recognitionResult: SFSpeechRecognitionResult)
```

#### Discussion

When this method is called, the delegate should expect no further information about the utterance to be reported.

## Parameters

- `task`: The speech recognition task (an   object) that represents the request.
- `recognitionResult`: A recognized utterance that contains one or more transcription hypotheses in an   object.

## See Also

- [func speechRecognitionTask(SFSpeechRecognitionTask, didFinishSuccessfully: Bool)](sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didfinishsuccessfully:).md)
  Tells the delegate when the recognition of all requested utterances is finished.
- [func speechRecognitionTaskWasCancelled(SFSpeechRecognitionTask)](sfspeechrecognitiontaskdelegate/speechrecognitiontaskwascancelled(_:).md)
  Tells the delegate that the task has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didfinishrecognition:))*