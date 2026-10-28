# register(forTaskWithIdentifier:using:launchHandler:)

**Framework**: Background Tasks  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) registerForTaskWithIdentifier:(NSString *) identifier usingQueue:(dispatch_queue_t) queue launchHandler:(void (^)(BGTask *task)) launchHandler;
```

## Mentions

- [Performing long-running tasks on iOS and iPadOS](../performing-long-running-tasks-on-ios-and-ipados.md)

## Return value

Returns [`true`](../../Swift/true.md) if the launch handler was registered. Returns [`false`](../../Swift/false.md) if the identifier isn’t included in the [`BGTaskSchedulerPermittedIdentifiers`](../../BundleResources/information-property-list/bgtaskschedulerpermittedidentifiers.md) `Info.plist`.

## Discussion

Every identifier in the [`BGTaskSchedulerPermittedIdentifiers`](../../BundleResources/information-property-list/bgtaskschedulerpermittedidentifiers.md) requires a handler. Registration of all launch handlers must be complete before the end of [`applicationDidFinishLaunching(_:)`](../../UIKit/uiapplicationdelegate/applicationdidfinishlaunching%28_%29.md).

> ❗ **Important**: Register each task identifier only once. The system kills the app on the second registration of the same task identifier.

## Parameters

- `identifier`: A string containing the identifier of the task.
- `queue`: A queue for executing the task. Pass `nil` to use a default background queue.
- `launchHandler`: The system runs the block of code for the launch handler when it launches the app in the background. The block takes a single parameter, a [`BGTask`](../bgtask.md) object used for assigning an expiration handler and for setting a completion status. The block has no return value.

## See Also

### Scheduling a task
- [func submit(BGTaskRequest) throws](./submit%28_%29.md)
  Submit a previously registered background task for execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/register(fortaskwithidentifier:using:launchhandler:))*