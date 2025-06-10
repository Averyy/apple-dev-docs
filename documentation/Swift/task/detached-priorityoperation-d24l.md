# detached(priority:operation:)

**Framework**: Swift  
**Kind**: method

Runs the given nonthrowing operation asynchronously as part of a new top-level task.

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
@discardableResult
static func detached(priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async -> Success) -> Task<Success, Failure>
```

#### Return Value

A reference to the task.

#### Discussion

Don’t use a detached task if it’s possible to model the operation using structured concurrency features like child tasks. Child tasks inherit the parent task’s priority and task-local storage, and canceling a parent task automatically cancels all of its child tasks. You need to handle these considerations manually with a detached task.

You need to keep a reference to the detached task if you want to cancel it by calling the `Task.cancel()` method. Discarding your reference to a detached task doesn’t implicitly cancel that task, it only makes it impossible for you to explicitly cancel the task.

## Parameters

- `priority`: The priority of the task.
- `operation`: The operation to perform.

## See Also

- [init(priority: TaskPriority?, operation: sending () async -> Success)](task/init(priority:operation:)-7f0zv.md)
  Runs the given nonthrowing operation asynchronously as part of a new top-level task on behalf of the current actor.
- [init(priority: TaskPriority?, operation: sending () async throws -> Success)](task/init(priority:operation:)-ntwf.md)
  Runs the given throwing operation asynchronously as part of a new top-level task on behalf of the current actor.
- [init(executorPreference: consuming (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> Success)](task/init(executorpreference:priority:operation:)-7zpzv.md)
  Runs the given nonthrowing operation asynchronously as part of a new top-level task on behalf of the current actor.
- [init(executorPreference: consuming (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> Success)](task/init(executorpreference:priority:operation:)-6o27o.md)
  Runs the given throwing operation asynchronously as part of a new top-level task on behalf of the current actor.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/detached(priority:operation:)-d24l)*