# submitTaskRequest(_:completionHandler:)

**Framework**: Background Tasks  
**Kind**: method

Submits a background task request to be scheduled with a completion handler.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func submitTaskRequest(_ taskRequest: BGTaskRequest) async throws
```

#### Discussion

This method asynchronously submits the task request and invokes the completion handler with any errors that occur during submission.

Submitting a task request for an unexecuted task that’s already in the queue replaces the previous task request.

There can be a total of 1 refresh task and 10 processing tasks scheduled at any time. Trying to schedule more tasks will result in an error with code [`BGTaskScheduler.Error.Code.tooManyPendingTaskRequests`](bgtaskscheduler/error/code/toomanypendingtaskrequests.md).

Common errors include:

- [`BGTaskScheduler.Error.Code.notPermitted`](bgtaskscheduler/error/code/notpermitted.md): Task identifier not permitted or unsupported resources requested
- [`BGTaskScheduler.Error.Code.tooManyPendingTaskRequests`](bgtaskscheduler/error/code/toomanypendingtaskrequests.md): Too many pending tasks of this type
- [`BGTaskScheduler.Error.Code.unavailable`](bgtaskscheduler/error/code/unavailable.md): Background refresh disabled or app not permitted
- [`BGTaskScheduler.Error.Code.immediateRunIneligible`](bgtaskscheduler/error/code/immediaterunineligible.md): Immediate run not eligible due to system conditions

The completion handler is called on an arbitrary queue.

> **Note**: The completion handler may be invoked on an arbitrary queue after an arbitrary amount of delay. Do not call this method from the main thread or performance-critical contexts.

This method replaces the deprecated [`submit(_:)`](bgtaskscheduler/submit(_:).md) method.

## Parameters

- `taskRequest`: The task request object representing the parameters of the background task to be scheduled.
- `completionHandler`: A block that is called when submission completes. The block receives an optional error parameter: - `nil` if the task was submitted successfully
- An `NSError` if submission failed


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/submittaskrequest(_:completionhandler:))*