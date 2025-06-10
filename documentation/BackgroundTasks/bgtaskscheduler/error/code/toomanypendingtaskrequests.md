# BGTaskScheduler.Error.Code.tooManyPendingTaskRequests

**Framework**: Background Tasks  
**Kind**: case

A task scheduling error that indicates there are too many pending tasks of the type requested.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case tooManyPendingTaskRequests
```

#### Discussion

Try canceling some existing task requests and then resubmit the request that failed.

## See Also

- [BGTaskScheduler.Error.Code.notPermitted](bgtaskscheduler/error/code/notpermitted.md)
  A task scheduling error that indicates the app isn’t permitted to launch the task.
- [BGTaskScheduler.Error.Code.unavailable](bgtaskscheduler/error/code/unavailable.md)
  A task scheduling error that indicates the app or extension can’t schedule background work.
- [BGTaskScheduler.Error.Code.immediateRunIneligible](bgtaskscheduler/error/code/immediaterunineligible.md)
  A task scheduling error that indicates a task request didn’t run immediately due to system conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/error/code/toomanypendingtaskrequests)*