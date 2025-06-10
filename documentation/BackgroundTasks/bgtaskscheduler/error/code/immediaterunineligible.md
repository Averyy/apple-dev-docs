# BGTaskScheduler.Error.Code.immediateRunIneligible

**Framework**: Background Tasks  
**Kind**: case

A task scheduling error that indicates a task request didn’t run immediately due to system conditions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case immediateRunIneligible
```

#### Discussion

The framework throws this error when a [`BGContinuedProcessingTaskRequest`](bgcontinuedprocessingtaskrequest.md) that your app submits with [`strategy`](bgcontinuedprocessingtaskrequest/strategy.md) set to  [`BGContinuedProcessingTaskRequest.SubmissionStrategy.fail`](bgcontinuedprocessingtaskrequest/submissionstrategy/fail.md) isn’t able to begin right away due to runtime conditions.

If the task that fails submission is of high importance and your app has other tasks submitted, you can try canceling the other task requests and resubmit the failed request.

## See Also

- [BGTaskScheduler.Error.Code.notPermitted](bgtaskscheduler/error/code/notpermitted.md)
  A task scheduling error that indicates the app isn’t permitted to launch the task.
- [BGTaskScheduler.Error.Code.tooManyPendingTaskRequests](bgtaskscheduler/error/code/toomanypendingtaskrequests.md)
  A task scheduling error that indicates there are too many pending tasks of the type requested.
- [BGTaskScheduler.Error.Code.unavailable](bgtaskscheduler/error/code/unavailable.md)
  A task scheduling error that indicates the app or extension can’t schedule background work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/error/code/immediaterunineligible)*