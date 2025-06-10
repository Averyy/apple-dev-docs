# speechRecognitionDidDetectSpeech(_:)

**Framework**: Speech  
**Kind**: method

Tells the delegate when the task first detects speech in the source audio.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
optional func speechRecognitionDidDetectSpeech(_ task: SFSpeechRecognitionTask)
```

## Parameters

- `task`: The speech recognition task (an   object) that represents the request.

## See Also

- [func speechRecognitionTaskFinishedReadingAudio(SFSpeechRecognitionTask)](sfspeechrecognitiontaskdelegate/speechrecognitiontaskfinishedreadingaudio(_:).md)
  Tells the delegate when the task is no longer accepting new audio input, even if final processing is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskdelegate/speechrecognitiondiddetectspeech(_:))*