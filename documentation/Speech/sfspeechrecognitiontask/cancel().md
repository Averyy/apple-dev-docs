# cancel()

**Framework**: Speech  
**Kind**: method  
**Role**: Instance Method

Cancels the current speech recognition task.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func cancel()
```

```objc
- (void) cancel;
```

#### Discussion

You can cancel recognition tasks for both prerecorded and live audio input. For example, you might cancel a task in response to a user action or because the recording was interrupted.

When canceling a task, be sure to release any resources associated with the task, such as the audio input resources you are using to capture audio samples.

## See Also

### Canceling a speech recognition task
- [var isCancelled: Bool](./iscancelled.md)
  A Boolean value that indicates whether the speech recognition task was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontask/cancel())*