# cancel()

**Framework**: Swift  
**Kind**: method

Cancels this task.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func cancel()
```

#### Discussion

Cancelling a task has three primary effects:

- It flags the task as canceled.
- It causes any active cancellation handlers on the task to run, once.
- It cancels any child tasks and task groups of the task, including those created in the future. If those tasks have cancellation handlers, they also are triggered.

Task cancellation is cooperative and idempotent.

Cancelling a task does not automatically cause arbitrary functions on the task to stop running or throw errors. A function  choose to react to cancellation by ending its work early, and it is conventional to signal that to callers by throwing `CancellationError`. However, a function that doesn’t specifically check for cancellation will run to completion normally, even if the task it is running on is canceled. However, that function might still end early if it calls other code that handles cancellation by throwing and that function doesn’t handle the error.

It’s safe to cancel a task from any task or thread. It’s safe for multiple tasks or threads to cancel the same task at the same time. Cancelling a task that has already been canceled has no additional effect.

`cancel` may need to acquire locks and synchronously run arbitrary cancellation-handler code associated with the canceled task. To reduce the risk of deadlock, it is recommended that callers release any locks they might be holding before they call cancel.

If the task has already run past the last point where it could have performed a cancellation check, cancelling it may have no observable effects.

> **Note**: `Task.checkCancellation()`

> **Note**: `withTaskCancellationHandler(operation:onCancel:isolation:)`

## See Also

- [struct CancellationError](cancellationerror.md)
  An error that indicates a task was canceled.
- [var isCancelled: Bool](task/iscancelled-swift.property.md)
  A Boolean value that indicates whether the task should stop executing.
- [static var isCancelled: Bool](task/iscancelled-swift.type.property.md)
  A Boolean value that indicates whether the task should stop executing.
- [static func checkCancellation() throws](task/checkcancellation.md)
  Throws an error if the task was canceled.
- [func withTaskCancellationHandler<T>(handler: () -> Void, operation: () async throws -> T) async rethrows -> T](withtaskcancellationhandler(handler:operation:).md)
- [func withTaskCancellationHandler<T>(operation: () async throws -> T, onCancel: () -> Void, isolation: isolated (any Actor)?) async rethrows -> T](withtaskcancellationhandler(operation:oncancel:isolation:).md)
  Execute an operation with a cancellation handler that’s immediately invoked if the current task is canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/cancel())*