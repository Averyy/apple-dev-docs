# init(name:priority:operation:)

**Framework**: Swift  
**Kind**: init

Runs the given nonthrowing operation asynchronously as part of a new  top-level task.

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
init(name: String? = nil, priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async -> Success)
```

#### Return Value

A reference to the task.

#### Discussion

You need to keep a reference to the task if you want to cancel it by calling the `Task.cancel()` method. Discarding your reference to a task doesn’t implicitly cancel that task, it only makes it impossible for you to explicitly cancel the task.

## Parameters

- `name`: Human readable name of the task.
- `priority`: The priority of the operation task.
- `operation`: The operation to perform.

## See Also

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
- [func withTaskPriorityEscalationHandler<T, E>(operation: () async throws(E) -> T, onPriorityEscalated: (TaskPriority, TaskPriority) -> Void, isolation: isolated (any Actor)?) async throws(E) -> T](withtaskpriorityescalationhandler(operation:onpriorityescalated:isolation:).md)
  Runs the passed `operation` while registering a task priority escalation handler. The handler will be triggered concurrently to the current task if the current is subject to priority escalation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/init(name:priority:operation:)-2dll5)*