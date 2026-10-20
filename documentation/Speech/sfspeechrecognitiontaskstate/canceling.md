# SFSpeechRecognitionTaskState.canceling

**Framework**: Speech  
**Kind**: case  
**Role**: Case

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

```c
SFSpeechRecognitionTaskStateCanceling
```

## See Also

### Task states
- [SFSpeechRecognitionTaskState.completed](./completed.md)
  Delivery of recognition requests has finished and audio recording has stopped.
- [SFSpeechRecognitionTaskState.finishing](./finishing.md)
  Audio recording has stopped, but delivery of recognition results may continue.
- [SFSpeechRecognitionTaskState.running](./running.md)
  Speech recognition (potentially including audio recording) is in progress.
- [SFSpeechRecognitionTaskState.starting](./starting.md)
  Speech recognition (potentially including audio recording) has not yet started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskstate/canceling)*