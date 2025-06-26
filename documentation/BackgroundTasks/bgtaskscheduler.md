# BGTaskScheduler

**Framework**: Background Tasks  
**Kind**: class

A class for scheduling tasks that add background support to your app’s most critical work.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class BGTaskScheduler
```

## Mentions

- [Performing long-running tasks on iOS and iPadOS](performing-long-running-tasks-on-ios-and-ipados.md)

#### Overview

Background tasks give your app a way to run code even when the app is suspended:

- To register, schedule, and run tasks in the background, see [`Using background tasks to update your app`](https://developer.apple.com/documentation/UIKit/using-background-tasks-to-update-your-app).
- To submit work in the foreground that can finish even if the app moves to the background, see [`Performing long-running tasks on iOS and iPadOS`](performing-long-running-tasks-on-ios-and-ipados.md).

## Topics

### Getting the shared task scheduler
- [class var shared: BGTaskScheduler](bgtaskscheduler/shared.md)
  The shared background task scheduler instance.
### Checking task requirements
- [class var supportedResources: BGContinuedProcessingTaskRequest.Resources](bgtaskscheduler/supportedresources.md)
  Additional system resources that a continuous background task can request.
### Scheduling a task
- [func register(forTaskWithIdentifier: String, using: dispatch_queue_t?, launchHandler: (BGTask) -> Void) -> Bool](bgtaskscheduler/register(fortaskwithidentifier:using:launchhandler:).md)
  Register a launch handler for the task with the associated identifier that’s executed on the specified queue.
- [func submit(BGTaskRequest) throws](bgtaskscheduler/submit(_:).md)
  Submit a previously registered background task for execution.
### Canceling a task
- [func cancel(taskRequestWithIdentifier: String)](bgtaskscheduler/cancel(taskrequestwithidentifier:).md)
  Cancel a previously scheduled task request.
- [func cancelAllTaskRequests()](bgtaskscheduler/cancelalltaskrequests.md)
  Cancel all scheduled task requests.
### Getting all scheduled tasks
- [func getPendingTaskRequests(completionHandler: ([BGTaskRequest]) -> Void)](bgtaskscheduler/getpendingtaskrequests(completionhandler:).md)
  Request a list of unexecuted scheduled task requests.
### Handling errors
- [BGTaskScheduler.Error](bgtaskscheduler/error.md)
  The Errors for the `BGTaskSchedulerError` domain.
- [BGTaskScheduler.Error.Code](bgtaskscheduler/error/code.md)
  An enumeration of the task scheduling errors.
- [class let errorDomain: String](bgtaskscheduler/errordomain.md)
  The background tasks error domain as a string.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Background Tasks updates](../Updates/BackgroundTasks.md)
  Learn about important changes in Background Tasks.
- [class BGTask](bgtask.md)
  An abstract class for the framework’s tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler)*