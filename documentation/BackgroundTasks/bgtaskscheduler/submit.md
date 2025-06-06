# submit(_:)

**Framework**: Background Tasks  
**Kind**: method

Submit a previously registered background task for execution.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func submit(_ taskRequest: BGTaskRequest) throws
```

## Mentions

- [Starting and Terminating Tasks During Development](starting-and-terminating-tasks-during-development.md)

#### Discussion

Submitting a task request for an unexecuted task that’s already in the queue replaces the previous task request.

There can be a total of 1 refresh task and 10 processing tasks scheduled at any time. Trying to schedule more tasks returns [`BGTaskScheduler.Error.Code.tooManyPendingTaskRequests`](bgtaskscheduler/error/code/toomanypendingtaskrequests.md).

## Parameters

- `taskRequest`: A background task request object specifying the task identifier and optional configuration information.

## See Also

- [func register(forTaskWithIdentifier: String, using: dispatch_queue_t?, launchHandler: (BGTask) -> Void) -> Bool](bgtaskscheduler/register(fortaskwithidentifier:using:launchhandler:).md)
  Register a launch handler for the task with the associated identifier that’s executed on the specified queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/submit(_:))*