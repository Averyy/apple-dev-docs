# speechRecognitionTask(_:didHypothesizeTranscription:)

**Framework**: Speech  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a hypothesized transcription is available.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
optional func speechRecognitionTask(_ task: SFSpeechRecognitionTask, didHypothesizeTranscription transcription: SFTranscription)
```

```objc
- (void) speechRecognitionTask:(SFSpeechRecognitionTask *) task didHypothesizeTranscription:(SFTranscription *) transcription;
```

#### Discussion

This method is called for all recognitions, including partial recognitions.

## Parameters

- `task`: The speech recognition task (an [`SFSpeechRecognitionTask`](../sfspeechrecognitiontask.md) object) that represents the request.
- `transcription`: The hypothesized transcription in an [`SFTranscription`](../sftranscription.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskdelegate/speechrecognitiontask(_:didhypothesizetranscription:))*