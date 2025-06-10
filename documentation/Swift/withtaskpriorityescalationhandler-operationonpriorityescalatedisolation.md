# withTaskPriorityEscalationHandler(operation:onPriorityEscalated:isolation:)

**Framework**: Swift  
**Kind**: func

Runs the passed `operation` while registering a task priority escalation handler. The handler will be triggered concurrently to the current task if the current is subject to priority escalation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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

- [init(priority: TaskPriority?, operation: sending () async -> Success)](task/init(priority:operation:)-7f0zv.md)
  Runs the given nonthrowing operation asynchronously as part of a new top-level task on behalf of the current actor.
- [init(priority: TaskPriority?, operation: sending () async throws -> Success)](task/init(priority:operation:)-ntwf.md)
  Runs the given throwing operation asynchronously as part of a new top-level task on behalf of the current actor.
- [init(executorPreference: consuming (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> Success)](task/init(executorpreference:priority:operation:)-7zpzv.md)
  Runs the given nonthrowing operation asynchronously as part of a new top-level task on behalf of the current actor.
- [init(executorPreference: consuming (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> Success)](task/init(executorpreference:priority:operation:)-6o27o.md)
  Runs the given throwing operation asynchronously as part of a new top-level task on behalf of the current actor.
- [static func detached(priority: TaskPriority?, operation: sending () async -> Success) -> Task<Success, Failure>](task/detached(priority:operation:)-d24l.md)
  Runs the given nonthrowing operation asynchronously as part of a new top-level task.
- [static func detached(priority: TaskPriority?, operation: sending () async throws -> Success) -> Task<Success, Failure>](task/detached(priority:operation:)-1g00u.md)
  Runs the given throwing operation asynchronously as part of a new top-level task.
- [static func detached(executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> Success) -> Task<Success, Failure>](task/detached(executorpreference:priority:operation:)-1y7ms.md)
  Runs the given nonthrowing operation asynchronously as part of a new top-level task.
- [static func detached(executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> Success) -> Task<Success, Failure>](task/detached(executorpreference:priority:operation:)-7vnfx.md)
  Runs the given throwing operation asynchronously as part of a new top-level task.
- [static var currentPriority: TaskPriority](task/currentpriority.md)
  The current task’s priority.
- [static var basePriority: TaskPriority?](task/basepriority.md)
  The current task’s base priority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withtaskpriorityescalationhandler(operation:onpriorityescalated:isolation:))*