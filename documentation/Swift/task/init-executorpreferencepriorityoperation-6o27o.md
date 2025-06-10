# init(executorPreference:priority:operation:)

**Framework**: Swift  
**Kind**: init

Runs the given throwing operation asynchronously as part of a new top-level task on behalf of the current actor.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@discardableResult
init(executorPreference taskExecutor: consuming (any TaskExecutor)?, priority: TaskPriority? = nil, operation: sending @escaping () async throws -> Success)
```

#### Discussion

Use this function when creating asynchronous work that operates on behalf of the synchronous function that calls it. Like `Task.detached(priority:operation:)`, this function creates a separate, top-level task. Unlike `detach(priority:operation:)`, the task created by `Task.init(priority:operation:)` inherits the priority and actor context of the caller, so the operation is treated more like an asynchronous extension to the synchronous operation.

You need to keep a reference to the task if you want to cancel it by calling the `Task.cancel()` method. Discarding your reference to a detached task doesn’t implicitly cancel that task, it only makes it impossible for you to explicitly cancel the task.

> **Note**: `withTaskExecutorPreference(_:operation:)`

## Parameters

- `taskExecutor`: The preferred task executor for this task,   and any child tasks created by it. Explicitly passing   is   interpreted as “no preference”.
- `priority`: The priority of the task.   Pass   to use the priority from  .
- `operation`: The operation to perform.

## See Also

- [init(priority: TaskPriority?, operation: sending () async -> Success)](task/init(priority:operation:)-7f0zv.md)
  Runs the given nonthrowing operation asynchronously as part of a new top-level task on behalf of the current actor.
- [init(priority: TaskPriority?, operation: sending () async throws -> Success)](task/init(priority:operation:)-ntwf.md)
  Runs the given throwing operation asynchronously as part of a new top-level task on behalf of the current actor.
- [init(executorPreference: consuming (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> Success)](task/init(executorpreference:priority:operation:)-7zpzv.md)
  Runs the given nonthrowing operation asynchronously as part of a new top-level task on behalf of the current actor.
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
- [func withTaskPriorityEscalationHandler<T, E>(operation: () async throws(E) -> T, onPriorityEscalated: (TaskPriority, TaskPriority) -> Void, isolation: isolated (any Actor)?) async throws(E) -> T](withtaskpriorityescalationhandler(operation:onpriorityescalated:isolation:).md)
  Runs the passed `operation` while registering a task priority escalation handler. The handler will be triggered concurrently to the current task if the current is subject to priority escalation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/init(executorpreference:priority:operation:)-6o27o)*