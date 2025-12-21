# detached(name:executorPreference:priority:operation:)

**Framework**: Swift  
**Kind**: method

Runs the given nonthrowing operation asynchronously as part of a new   top-level task.

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
static func detached(name: String? = nil, executorPreference taskExecutor: (any TaskExecutor)?, priority: TaskPriority? = nil, operation: sending @escaping () async -> Success) -> Task<Success, Never>
```

#### Return Value

A reference to the task.

#### Discussion

Don’t use a detached unstructured task if it’s possible to model the operation using structured concurrency features like child tasks. Child tasks inherit the parent task’s priority and task-local storage, and canceling a parent task automatically cancels all of its child tasks. You need to handle these considerations manually with a detached task.

You need to keep a reference to the task if you want to cancel it by calling the `Task.cancel()` method. Discarding your reference to a task doesn’t implicitly cancel that task, it only makes it impossible for you to explicitly cancel the task.

## Parameters

- `name`: Human readable name of the task.
- `taskExecutor`: The task executor that the child task should be started on and keep using.   Explicitly passing   as the executor preference is equivalent to no preference,   and effectively means to inherit the outer context’s executor preference.   You can also pass the   global executor explicitly.
- `priority`: The priority of the operation task.   Omit this parameter or pass   to inherit the enclosing context’s base priority.
- `operation`: The operation to perform.

## See Also

- [static func detached(name: String?, priority: TaskPriority?, operation: sending () async throws -> Success) -> Task<Success, any Error>](task/detached(name:priority:operation:)-795w1.md)
  Runs the given throwing operation asynchronously as part of a new   top-level task.
- [static func detached(name: String?, priority: TaskPriority?, operation: sending () async -> Success) -> Task<Success, Never>](task/detached(name:priority:operation:)-9xki7.md)
  Runs the given nonthrowing operation asynchronously as part of a new   top-level task.
- [static func detached(name: String?, executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> Success) -> Task<Success, any Error>](task/detached(name:executorpreference:priority:operation:)-6r16s.md)
  Runs the given throwing operation asynchronously as part of a new   top-level task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/detached(name:executorpreference:priority:operation:)-75ffe)*