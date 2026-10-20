# SFSpeechRecognitionTaskState.running

**Framework**: Speech  
**Kind**: case  
**Role**: Case

Speech recognition (potentially including audio recording) is in progress.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
case running
```

```c
SFSpeechRecognitionTaskStateRunning
```

## See Also

### Task states
- [SFSpeechRecognitionTaskState.canceling](./canceling.md)
  Delivery of recognition results has finished, but audio recording may be ongoing.
- [SFSpeechRecognitionTaskState.completed](./completed.md)
  Delivery of recognition requests has finished and audio recording has stopped.
- [SFSpeechRecognitionTaskState.finishing](./finishing.md)
  Audio recording has stopped, but delivery of recognition results may continue.
- [SFSpeechRecognitionTaskState.starting](./starting.md)
  Speech recognition (potentially including audio recording) has not yet started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskstate/running)*