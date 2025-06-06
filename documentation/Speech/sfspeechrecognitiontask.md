# SFSpeechRecognitionTask

**Framework**: Speech  
**Kind**: class

A task object for monitoring the speech recognition progress.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class SFSpeechRecognitionTask
```

#### Overview

Use an `SFSpeechRecognitionTask` object to determine the state of a speech recognition task, to cancel an ongoing task, or to signal the end of the task.

You don’t create speech recognition task objects directly. Instead, you receive one of these objects after calling [`recognitionTask(with:resultHandler:)`](sfspeechrecognizer/recognitiontask(with:resulthandler:).md) or [`recognitionTask(with:delegate:)`](sfspeechrecognizer/recognitiontask(with:delegate:).md) on your [`SFSpeechRecognizer`](sfspeechrecognizer.md) object.

## Topics

### Canceling a Speech Recognition Task
- [func cancel()](sfspeechrecognitiontask/cancel.md)
  Cancels the current speech recognition task.
- [var isCancelled: Bool](sfspeechrecognitiontask/iscancelled.md)
  A Boolean value that indicates whether the speech recognition task was canceled.
### Finishing a Speech Recognition Task
- [func finish()](sfspeechrecognitiontask/finish.md)
  Stops accepting new audio and finishes processing on the audio input that has already been accepted.
- [var isFinishing: Bool](sfspeechrecognitiontask/isfinishing.md)
  A Boolean value that indicates whether audio input has stopped.
### Monitoring Recognition Progress
- [var state: SFSpeechRecognitionTaskState](sfspeechrecognitiontask/state.md)
  The current state of the speech recognition task.
- [enum SFSpeechRecognitionTaskState](sfspeechrecognitiontaskstate.md)
  The state of the task associated with the recognition request.
- [var error: (any Error)?](sfspeechrecognitiontask/error.md)
  An error object that specifies the error that occurred during a speech recognition task.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontask)*