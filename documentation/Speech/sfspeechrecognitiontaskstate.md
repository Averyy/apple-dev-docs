# SFSpeechRecognitionTaskState

**Framework**: Speech  
**Kind**: enum

The state of the task associated with the recognition request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
enum SFSpeechRecognitionTaskState
```

## Topics

### Constants
- [SFSpeechRecognitionTaskState.canceling](sfspeechrecognitiontaskstate/canceling.md)
  Delivery of recognition results has finished, but audio recording may be ongoing.
- [SFSpeechRecognitionTaskState.completed](sfspeechrecognitiontaskstate/completed.md)
  Delivery of recognition requests has finished and audio recording has stopped.
- [SFSpeechRecognitionTaskState.finishing](sfspeechrecognitiontaskstate/finishing.md)
  Audio recording has stopped, but delivery of recognition results may continue.
- [SFSpeechRecognitionTaskState.running](sfspeechrecognitiontaskstate/running.md)
  Speech recognition (potentially including audio recording) is in progress.
- [SFSpeechRecognitionTaskState.starting](sfspeechrecognitiontaskstate/starting.md)
  Speech recognition (potentially including audio recording) has not yet started.
### Initializers
- [init?(rawValue: Int)](sfspeechrecognitiontaskstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var state: SFSpeechRecognitionTaskState](sfspeechrecognitiontask/state.md)
  The current state of the speech recognition task.
- [var error: (any Error)?](sfspeechrecognitiontask/error.md)
  An error object that specifies the error that occurred during a speech recognition task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskstate)*