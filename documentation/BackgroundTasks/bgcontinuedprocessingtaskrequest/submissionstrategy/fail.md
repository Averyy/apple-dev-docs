# BGContinuedProcessingTaskRequest.SubmissionStrategy.fail

**Framework**: Background Tasks  
**Kind**: case

An option that fails the submission of a continuous background task if the system can’t run it immediately.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
case fail
```

## Mentions

- [Performing long-running tasks on iOS and iPadOS](performing-long-running-tasks-on-ios-and-ipados.md)

#### Discussion

Task processing might not start right away if the system is currently resource constrainted.

## See Also

- [BGContinuedProcessingTaskRequest.SubmissionStrategy.queue](bgcontinuedprocessingtaskrequest/submissionstrategy/queue.md)
  An option that queues a continuous background task to begin as soon as possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/submissionstrategy/fail)*