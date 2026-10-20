# isCancelled

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

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
var isCancelled: Bool { get }
```

Available when `Success` conforms to `Sendable` and `Failure` conforms to `Error`.

#### Discussion

After the value of this property becomes `true`, it remains `true` indefinitely. There is no way to uncancel a task.

This property returns the actual cancellation state of the task, regardless of whether a cancellation shield is active. Use [`isCancelled`](./iscancelled-swift.type.property.md) (the static property) if you need cancellation checking that respects active shields.

##### Instance property isCancelled ignores Task Cancellation Shields

The instance property [`isCancelled`](./iscancelled-swift.property.md) is not contextual and therefore does not respect cancellation shields. If a task was cancelled and is executing with an active cancellation shield, these properties will return the *actual* cancellation status of the specific task.

Prefer using [`isCancelled`](./iscancelled-swift.type.property.md) (the static property) in most situations when checking the cancellation status from inside the task.

> **See Also**: ```Task/isCancelled-type.property``

> **See Also**: [`checkCancellation()`](./checkcancellation%28%29.md)

> **See Also**: [`hasActiveCancellationShield`](./hasactivecancellationshield.md)

> **See Also**: `withTaskCancellationShield(operation:)-(()->Value)`

## See Also

### Canceling Tasks
- [struct CancellationError](../cancellationerror.md)
  An error that indicates a task was canceled.
- [func cancel()](./cancel%28%29.md)
  Cancels this task.
- [static var isCancelled: Bool](./iscancelled-swift.type.property.md)
  A Boolean value that indicates whether the task should stop executing.
- [static func checkCancellation() throws](./checkcancellation%28%29.md)
  Throws an error if the task was canceled.
- [func withTaskCancellationHandler<Return, Failure>(operation: nonisolated(nonsending) () async throws(Failure) -> Return, onCancel: sending () -> Void) async throws(Failure) -> Return](../withtaskcancellationhandler%28operation,oncancel%29.md)
  Execute an operation with a cancellation handler that’s immediately invoked if the current task is canceled.
- [func withTaskCancellationHandler<T>(operation: () async throws -> T, onCancel: () -> Void, isolation: isolated (any Actor)?) async rethrows -> T](../withtaskcancellationhandler%28operation,oncancel,isolation%29.md)
  Execute an operation with a cancellation handler that’s immediately invoked if the current task is canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/iscancelled-swift.property)*