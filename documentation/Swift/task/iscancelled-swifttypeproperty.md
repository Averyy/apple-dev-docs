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

> **Note**: `checkCancellation()`

## See Also

- [struct CancellationError](cancellationerror.md)
  An error that indicates a task was canceled.
- [func cancel()](task/cancel.md)
  Cancels this task.
- [var isCancelled: Bool](task/iscancelled-swift.property.md)
  A Boolean value that indicates whether the task should stop executing.
- [static func checkCancellation() throws](task/checkcancellation.md)
  Throws an error if the task was canceled.
- [func withTaskCancellationHandler<T>(handler: () -> Void, operation: () async throws -> T) async rethrows -> T](withtaskcancellationhandler(handler:operation:).md)
- [func withTaskCancellationHandler<T>(operation: () async throws -> T, onCancel: () -> Void, isolation: isolated (any Actor)?) async rethrows -> T](withtaskcancellationhandler(operation:oncancel:isolation:).md)
  Execute an operation with a cancellation handler that’s immediately invoked if the current task is canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/iscancelled-swift.type.property)*