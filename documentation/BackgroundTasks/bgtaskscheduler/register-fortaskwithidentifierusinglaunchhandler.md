# register(forTaskWithIdentifier:using:launchHandler:)

**Framework**: Background Tasks  
**Kind**: method

Register a launch handler for the task with the associated identifier that’s executed on the specified queue.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func register(forTaskWithIdentifier identifier: String, using queue: dispatch_queue_t?, launchHandler: @escaping (BGTask) -> Void) -> Bool
```

## Mentions

- [Performing long-running tasks on iOS and iPadOS](performing-long-running-tasks-on-ios-and-ipados.md)

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/Swift/true) if the launch handler was registered. Returns [`false`](https://developer.apple.com/documentation/Swift/false) if the identifier isn’t included in the [`BGTaskSchedulerPermittedIdentifiers`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/BGTaskSchedulerPermittedIdentifiers) `Info.plist`.

#### Discussion

Every identifier in the [`BGTaskSchedulerPermittedIdentifiers`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/BGTaskSchedulerPermittedIdentifiers) requires a handler. Registration of all launch handlers must be complete before the end of [`applicationDidFinishLaunching(_:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/applicationDidFinishLaunching(_:)).

> ❗ **Important**: Register each task identifier only once. The system kills the app on the second registration of the same task identifier.

## Parameters

- `identifier`: A string containing the identifier of the task.
- `queue`: A queue for executing the task. Pass   to use a default background queue.
- `launchHandler`: The system runs the block of code for the launch handler when it launches the app in the background. The block takes a single parameter, a   object used for assigning an expiration handler and for setting a completion status. The block has no return value.

## See Also

- [func submit(BGTaskRequest) throws](bgtaskscheduler/submit(_:).md)
  Submit a previously registered background task for execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/register(fortaskwithidentifier:using:launchhandler:))*