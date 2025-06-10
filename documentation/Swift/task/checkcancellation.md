# checkCancellation()

**Framework**: Swift  
**Kind**: method

Throws an error if the task was canceled.

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
static func checkCancellation() throws
```

#### Discussion

The error is always an instance of `CancellationError`.

> **Note**: `isCancelled()`

## See Also

- [struct CancellationError](cancellationerror.md)
  An error that indicates a task was canceled.
- [func cancel()](task/cancel.md)
  Cancels this task.
- [var isCancelled: Bool](task/iscancelled-swift.property.md)
  A Boolean value that indicates whether the task should stop executing.
- [static var isCancelled: Bool](task/iscancelled-swift.type.property.md)
  A Boolean value that indicates whether the task should stop executing.
- [func withTaskCancellationHandler<T>(handler: () -> Void, operation: () async throws -> T) async rethrows -> T](withtaskcancellationhandler(handler:operation:).md)
- [func withTaskCancellationHandler<T>(operation: () async throws -> T, onCancel: () -> Void, isolation: isolated (any Actor)?) async rethrows -> T](withtaskcancellationhandler(operation:oncancel:isolation:).md)
  Execute an operation with a cancellation handler that’s immediately invoked if the current task is canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/checkcancellation())*