# init(name:executorPreference:priority:operation:)

**Framework**: Swift  
**Kind**: init

Runs the given throwing operation asynchronously as part of a new  top-level task.

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
init(name: String? = nil, executorPreference taskExecutor: (any TaskExecutor)?, priority: TaskPriority? = nil, operation: sending @escaping () async throws -> Success)
```

#### Return Value

A reference to the task.

#### Discussion

If the `operation` throws an error, it is caught by the `Task` and will be rethrown only when the task’s `value` is awaited. Take care to not accidentally dismiss errors by not awaiting on the task’s resulting value.

You need to keep a reference to the task if you want to cancel it by calling the `Task.cancel()` method. Discarding your reference to a task doesn’t implicitly cancel that task, it only makes it impossible for you to explicitly cancel the task.

## Parameters

- `name`: Human readable name of the task.
- `taskExecutor`: The task executor that the child task should be started on and keep using.   Explicitly passing   as the executor preference is equivalent to no preference,   and effectively means to inherit the outer context’s executor preference.   You can also pass the   global executor explicitly.
- `priority`: The priority of the operation task.
- `operation`: The operation to perform.

## See Also

- [init(name: String?, priority: TaskPriority?, operation: sending () async -> Success)](task/init(name:priority:operation:)-2dll5.md)
  Runs the given nonthrowing operation asynchronously as part of a new  top-level task.
- [init(name: String?, priority: TaskPriority?, operation: sending () async throws -> Success)](task/init(name:priority:operation:)-43wmk.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/init(name:executorpreference:priority:operation:)-59bfi)*