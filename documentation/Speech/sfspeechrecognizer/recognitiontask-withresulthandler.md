# recognitionTask(with:resultHandler:)

**Framework**: Speech  
**Kind**: method

Executes the speech recognition request and delivers the results to the specified handler block.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func recognitionTask(with request: SFSpeechRecognitionRequest, resultHandler: @escaping (SFSpeechRecognitionResult?, (any Error)?) -> Void) -> SFSpeechRecognitionTask
```

#### Return Value

The task object you can use to manage an in-progress recognition request.

#### Discussion

Use this method to initiate the speech recognition process on the audio contained in the request object. This method executes asynchronously and returns a [`SFSpeechRecognitionTask`](sfspeechrecognitiontask.md) object that you can use to cancel or finalize the recognition process later. As results become available, the method calls the block in the `resultHandler` parameter.

## Parameters

- `request`: A request (in an   object) to recognize speech from an audio source.
- `resultHandler`: The block to call when partial or final results are available, or when an error occurs. If the   property is  , this block may be called multiple times to deliver the partial and final results. The block has no return value and takes the following parameters:

## See Also

- [func recognitionTask(with: SFSpeechRecognitionRequest, delegate: any SFSpeechRecognitionTaskDelegate) -> SFSpeechRecognitionTask](sfspeechrecognizer/recognitiontask(with:delegate:).md)
  Recognizes speech from the audio source associated with the specified request, using the specified delegate to manage the results.
- [protocol SFSpeechRecognitionTaskDelegate](sfspeechrecognitiontaskdelegate.md)
  A protocol with methods for managing multi-utterance speech recognition requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognizer/recognitiontask(with:resulthandler:))*