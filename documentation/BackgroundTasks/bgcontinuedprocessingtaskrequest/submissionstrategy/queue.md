# BGContinuedProcessingTaskRequest.SubmissionStrategy.queue

**Framework**: Background Tasks  
**Kind**: case

An option that queues a continuous background task to begin as soon as possible.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
case queue
```

## Mentions

- [Performing long-running tasks on iOS and iPadOS](performing-long-running-tasks-on-ios-and-ipados.md)

#### Discussion

This option adds the task request to the back of a queue. The system runs the task as soon as possible. The system might be unable to run a submitted task immediately if the system is currently at the maximum level of concurrent tasks.

> ❗ **Important**: The system cancels queued [`BGContinuedProcessingTaskRequest`](bgcontinuedprocessingtaskrequest.md) objects if someone closes your app using the app switcher.

## See Also

- [BGContinuedProcessingTaskRequest.SubmissionStrategy.fail](bgcontinuedprocessingtaskrequest/submissionstrategy/fail.md)
  An option that fails the submission of a continuous background task if the system can’t run it immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/submissionstrategy/queue)*