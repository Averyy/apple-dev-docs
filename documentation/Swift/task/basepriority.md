# basePriority

**Framework**: Swift  
**Kind**: property

The current task’s base priority.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static var basePriority: TaskPriority? { get }
```

#### Discussion

If you access this property outside of any task, this returns nil

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
- [func withTaskPriorityEscalationHandler<T, E>(operation: () async throws(E) -> T, onPriorityEscalated: (TaskPriority, TaskPriority) -> Void, isolation: isolated (any Actor)?) async throws(E) -> T](withtaskpriorityescalationhandler(operation:onpriorityescalated:isolation:).md)
  Runs the passed `operation` while registering a task priority escalation handler. The handler will be triggered concurrently to the current task if the current is subject to priority escalation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/basepriority)*