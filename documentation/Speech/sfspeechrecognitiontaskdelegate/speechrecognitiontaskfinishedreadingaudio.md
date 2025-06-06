# speechRecognitionTaskFinishedReadingAudio(_:)

**Framework**: Speech  
**Kind**: method

Tells the delegate when the task is no longer accepting new audio input, even if final processing is in progress.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
optional func speechRecognitionTaskFinishedReadingAudio(_ task: SFSpeechRecognitionTask)
```

## Parameters

- `task`: The speech recognition task (an   object) that represents the request.

## See Also

- [func speechRecognitionDidDetectSpeech(SFSpeechRecognitionTask)](sfspeechrecognitiontaskdelegate/speechrecognitiondiddetectspeech(_:).md)
  Tells the delegate when the task first detects speech in the source audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskdelegate/speechrecognitiontaskfinishedreadingaudio(_:))*