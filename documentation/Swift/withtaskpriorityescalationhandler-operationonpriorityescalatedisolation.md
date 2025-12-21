# withTaskPriorityEscalationHandler(operation:onPriorityEscalated:isolation:)

**Framework**: Swift  
**Kind**: func

Runs the passed `operation` while registering a task priority escalation handler. The handler will be triggered concurrently to the current task if the current is subject to priority escalation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func withTaskPriorityEscalationHandler<T, E>(operation: () async throws(E) -> T, onPriorityEscalated handler: (TaskPriority, TaskPriority) -> Void, isolation: isolated (any Actor)? = #isolation) async throws(E) -> T where E : Error
```

#### Return Value

The value returned by `operation`

#### Discussion

The handler may perform additional actions upon priority escalation, but cannot influence how the escalation influences the task, i.e. the task’s priority will be escalated regardless of actions performed in the handler.

The handler will only trigger if a priority escalation occurs while the operation is in progress.

If multiple task escalation handlers are nester they will all be triggered.

Task escalation propagates through structured concurrency child-tasks.

> **Note**: When the `operation` throws an error

## Parameters

- `operation`: The operation during which to listen for priority escalation
- `handler`: Handler to invoke, concurrently to  ,   when priority escalation happens

## See Also

- [init(name: String?, priority: TaskPriority?, operation: sending () async -> Success)](task/init(name:priority:operation:)-2dll5.md)
  Runs the given nonthrowing operation asynchronously as part of a new  top-level task.
- [init(name: String?, priority: TaskPriority?, operation: sending () async throws -> Success)](task/init(name:priority:operation:)-43wmk.md)
  Runs the given throwing operation asynchronously as part of a new  top-level task.
- [init(name: String?, executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> Success)](task/init(name:executorpreference:priority:operation:)-59bfi.md)
  Runs the given throwing operation asynchronously as part of a new  top-level task.
- [init(name: String?, executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> Success)](task/init(name:executorpreference:priority:operation:)-81pay.md)
  Runs the given nonthrowing operation asynchronously as part of a new  top-level task.
- [static var currentPriority: TaskPriority](task/currentpriority.md)
  The current task’s priority.
- [static var basePriority: TaskPriority?](task/basepriority.md)
  The current task’s base priority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withtaskpriorityescalationhandler(operation:onpriorityescalated:isolation:))*