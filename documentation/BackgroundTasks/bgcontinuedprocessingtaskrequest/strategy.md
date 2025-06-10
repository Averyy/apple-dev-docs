# strategy

**Framework**: Background Tasks  
**Kind**: property

The submission strategy for the scheduler to abide by.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
var strategy: BGContinuedProcessingTaskRequest.SubmissionStrategy { get set }
```

## Mentions

- [Performing long-running tasks on iOS and iPadOS](performing-long-running-tasks-on-ios-and-ipados.md)

#### Discussion

The default value is [`BGContinuedProcessingTaskRequest.SubmissionStrategy.queue`](bgcontinuedprocessingtaskrequest/submissionstrategy/queue.md).

## See Also

- [BGContinuedProcessingTaskRequest.SubmissionStrategy](bgcontinuedprocessingtaskrequest/submissionstrategy.md)
  The ways your app suggests the system handle your task’s submission under varying conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/strategy)*