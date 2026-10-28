# resume()

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Begins or resumes a machine learning task.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func resume()
```

```objc
- (void) resume;
```

## Discussion

Use this method to start a task for the first time or resumes a task that has paused. Tasks pause when they notify your app’s progress handlers, such as those you provide to an [`MLUpdateProgressHandlers`](../mlupdateprogresshandlers.md) instance.

## See Also

### Starting and stopping a task
- [func cancel()](./cancel%28%29.md)
  Cancels a machine learning task before it completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltask/resume())*