# isCancelled

**Framework**: Swift  
**Kind**: property

A Boolean value that indicates whether the task should stop executing.

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
static var isCancelled: Bool { get }
```

#### Discussion

After the value of this property becomes `true`, it remains `true` indefinitely. There is no way to uncancel a task.

##### Interaction with Task Cancellation Shields

Cancellation may be suppressed by an active task cancellation shield (`withTaskCancellationShield(operation:)-(()->Value)`), which may cause `isCancelled` to return `false` even though the task has been cancelled externally.

> **Note**: [`checkCancellation()`](task/checkcancellation().md)

> **Note**: `withTaskCancellationShield(operation:)-(()->Value)`

## See Also

- [struct CancellationError](cancellationerror.md)
  An error that indicates a task was canceled.
- [func cancel()](task/cancel.md)
  Cancels this task.
- [var isCancelled: Bool](task/iscancelled-swift.property.md)
  A Boolean value that indicates whether the task should stop executing.
- [static func checkCancellation() throws](task/checkcancellation.md)
  Throws an error if the task was canceled.
- [func withTaskCancellationHandler<Return, Failure>(operation: nonisolated(nonsending) () async throws(Failure) -> Return, onCancel: sending () -> Void) async throws(Failure) -> Return](withtaskcancellationhandler(operation:oncancel:).md)
  Execute an operation with a cancellation handler that’s immediately invoked if the current task is canceled.
- [func withTaskCancellationHandler<T>(operation: () async throws -> T, onCancel: () -> Void, isolation: isolated (any Actor)?) async rethrows -> T](withtaskcancellationhandler(operation:oncancel:isolation:).md)
  Execute an operation with a cancellation handler that’s immediately invoked if the current task is canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/iscancelled-swift.type.property)*