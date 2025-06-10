# SFSpeechRecognitionTaskState

**Framework**: Speech  
**Kind**: enum

The state of the task associated with the recognition request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
enum SFSpeechRecognitionTaskState
```

## Topics

### Task states
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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class SFSpeechRecognitionTask](sfspeechrecognitiontask.md)
  A task object for monitoring the speech recognition progress.
- [protocol SFSpeechRecognitionTaskDelegate](sfspeechrecognitiontaskdelegate.md)
  A protocol with methods for managing multi-utterance speech recognition requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontaskstate)*