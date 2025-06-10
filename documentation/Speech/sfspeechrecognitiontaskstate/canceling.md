# SFSpeechRecognitionTaskState.canceling

**Framework**: Speech  
**Kind**: case

Delivery of recognition results has finished, but audio recording may be ongoing.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
case canceling
```

## See Also

- [SFSpeechRecognitionTaskState.completed](sfspeechrecognitiontaskstate/completed.md)
  Delivery of recognition requests has finished and audio recording has stopped.
- [SFSpeechRecognitionTaskState.finishing](sfspeechrecognitiontaskstate/finishing.md)
  Audio recording has stopped, but delivery of recognition results may continue.
- [SFSpeechRecognitionTaskState.running](sfspeechrecognitiontaskstate/running.md)
  Speech recognition (potentially including audio recording) is in progress.
- [SFSpeechRecognitionTaskState.starting](sfspeechrecognitiontaskstate/starting.md)
  Speech recognition (potentially including audio recording) has not yet started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskstate/canceling)*