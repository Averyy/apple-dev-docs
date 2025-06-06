# state

**Framework**: Speech  
**Kind**: property

The current state of the speech recognition task.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var state: SFSpeechRecognitionTaskState { get }
```

#### Discussion

Check the value of this property to get the state of the in-progress speech recognition session. For valid values, see [`SFSpeechRecognitionTaskState`](sfspeechrecognitiontaskstate.md).

## See Also

- [enum SFSpeechRecognitionTaskState](sfspeechrecognitiontaskstate.md)
  The state of the task associated with the recognition request.
- [var error: (any Error)?](sfspeechrecognitiontask/error.md)
  An error object that specifies the error that occurred during a speech recognition task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontask/state)*