# withTaskCancellationHandler(operation:onCancel:isolation:)

**Framework**: Swift  
**Kind**: func

Execute an operation with a cancellation handler that’s immediately invoked if the current task is canceled.

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
@backDeployed(before: macOS 15.0, iOS 18.0, watchOS 11.0, tvOS 18.0, visionOS 2.0)
func withTaskCancellationHandler<T>(operation: () async throws -> T, onCancel handler: () -> Void, isolation: isolated (any Actor)? = #isolation) async rethrows -> T
```

#### Discussion

This differs from the operation cooperatively checking for cancellation and reacting to it in that the cancellation handler is  and  invoked when the task is canceled. For example, even if the operation is running code that never checks for cancellation, a cancellation handler still runs and provides a chance to run some cleanup code:

```swift
await withTaskCancellationHandler {
  var sum = 0
  while condition {
    sum += 1
  }
  return sum
} onCancel: {
  // This onCancel closure might execute concurrently with the operation.
  condition.cancel()
}
```

##### Execution Order and Semantics

The `operation` closure is always invoked, even when the `withTaskCancellationHandler(operation:onCancel:)` method is called from a task that was already cancelled.

When `withTaskCancellationHandler(operation:onCancel:)` is used in a task that has already been cancelled, the cancellation handler will be executed immediately before the `operation` closure gets to execute.

This allows the cancellation handler to set some external “cancelled” flag that the operation may be  checking for in order to avoid performing any actual work once the operation gets to run.

The `operation` closure executes on the calling execution context, and doesn’t suspend or change execution context unless code contained within the closure does so. In other words, the potential suspension point of the `withTaskCancellationHandler(operation:onCancel:)` never suspends by itself before executing the operation.

If cancellation occurs while the operation is running, the cancellation handler executes  with the operation.

##### Cancellation Handlers and Locks

Cancellation handlers which acquire locks must take care to avoid deadlock. The cancellation handler may be invoked while holding internal locks associated with the task or other tasks.  Other operations on the task, such as resuming a continuation, may acquire these same internal locks. Therefore, if a cancellation handler must acquire a lock, other code should not cancel tasks or resume continuations while holding that lock.

## See Also

- [struct CancellationError](cancellationerror.md)
  An error that indicates a task was canceled.
- [func cancel()](task/cancel.md)
  Cancels this task.
- [var isCancelled: Bool](task/iscancelled-swift.property.md)
  A Boolean value that indicates whether the task should stop executing.
- [static var isCancelled: Bool](task/iscancelled-swift.type.property.md)
  A Boolean value that indicates whether the task should stop executing.
- [static func checkCancellation() throws](task/checkcancellation.md)
  Throws an error if the task was canceled.
- [func withTaskCancellationHandler<T>(handler: () -> Void, operation: () async throws -> T) async rethrows -> T](withtaskcancellationhandler(handler:operation:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withtaskcancellationhandler(operation:oncancel:isolation:))*