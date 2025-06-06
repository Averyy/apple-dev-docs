# BGTaskScheduler

**Framework**: Background Tasks  
**Kind**: class

A class for scheduling task requests that launch your app in the background.

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

#### Overview

Background tasks give your app a way to run code while the app is suspended. To learn how to register, schedule, and run a background task, see [`Using background tasks to update your app`](https://developer.apple.com/documentation/UIKit/using-background-tasks-to-update-your-app).

## Topics

### Getting the shared task scheduler
- [class var shared: BGTaskScheduler](bgtaskscheduler/shared.md)
  The shared background task scheduler instance.
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

- [Starting and Terminating Tasks During Development](starting-and-terminating-tasks-during-development.md)
  Use the debugger during development to start tasks and to terminate them before completion.
- [Refreshing and Maintaining Your App Using Background Tasks](refreshing-and-maintaining-your-app-using-background-tasks.md)
  Use scheduled background tasks for refreshing your app content and for performing maintenance.
- [Choosing Background Strategies for Your App](choosing-background-strategies-for-your-app.md)
  Select the best method of scheduling background runtime for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler)*