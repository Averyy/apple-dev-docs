# BGContinuedProcessingTaskRequest.SubmissionStrategy.fail

**Framework**: Background Tasks  
**Kind**: case  
**Role**: Case

An option that fails the submission of a continuous background task if the system can’t run it immediately.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
case fail
```

```c
BGContinuedProcessingTaskRequestSubmissionStrategyFail
```

## Mentions

- [Performing long-running tasks on iOS and iPadOS](../../performing-long-running-tasks-on-ios-and-ipados.md)

#### Discussion

Task processing might not start right away if the system is currently resource constrainted.

## See Also

### Choosing a strategy
- [BGContinuedProcessingTaskRequest.SubmissionStrategy.queue](./queue.md)
  An option that queues a continuous background task to begin as soon as possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/submissionstrategy/fail)*