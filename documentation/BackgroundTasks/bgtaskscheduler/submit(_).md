# submit(_:)

**Framework**: Background Tasks  
**Kind**: method  
**Role**: Instance Method

Submit a previously registered background task for execution.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- tvOS 13.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use -submitTaskRequest:completionHandler: (Swift: submitTaskRequest(_:completionHandler:), or 'try await submitTaskRequest(_:)') to capture all error conditions

## Declaration

```swift
func submit(_ taskRequest: BGTaskRequest) throws
```

```objc
- (BOOL) submitTaskRequest:(BGTaskRequest *) taskRequest error:(NSError **) error;
```

## Mentions

- [Performing long-running tasks on iOS and iPadOS](../performing-long-running-tasks-on-ios-and-ipados.md)
- [Starting and Terminating Tasks During Development](../starting-and-terminating-tasks-during-development.md)

## Discussion

Submitting a task request for an unexecuted task that’s already in the queue replaces the previous task request.

There can be a total of 1 refresh task and 10 processing tasks scheduled at any time. Trying to schedule more tasks returns [`BGTaskScheduler.Error.Code.tooManyPendingTaskRequests`](./error/code/toomanypendingtaskrequests.md).

## Parameters

- `taskRequest`: A background task request object specifying the task identifier and optional configuration information.

## See Also

### Scheduling a task
- [func register(forTaskWithIdentifier: String, using: dispatch_queue_t?, launchHandler: (BGTask) -> Void) -> Bool](./register%28fortaskwithidentifier,using,launchhandler%29.md)
  Register a launch handler for the task with the associated identifier that’s executed on the specified queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/submit(_:))*