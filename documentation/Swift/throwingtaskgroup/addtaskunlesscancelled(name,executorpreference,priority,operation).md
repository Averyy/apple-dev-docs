# addTaskUnlessCancelled(name:executorPreference:priority:operation:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.

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
mutating func addTaskUnlessCancelled(name: String?, executorPreference taskExecutor: (any TaskExecutor)? = nil, priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async throws -> ChildTaskResult) -> Bool
```

Available when `ChildTaskResult` conforms to `Sendable` and `Failure` conforms to `Error`.

## Return Value

`true` if the child task was added to the group; otherwise `false`.

## Discussion

This method doesn’t throw an error, even if the child task does. Instead, the corresponding call to `ThrowingTaskGroup.next()` rethrows that error.

## Parameters

- `name`: Human readable name of this task.
- `taskExecutor`: The task executor that the child task should be started on and keep using. Explicitly passing `nil` as the executor preference is equivalent to calling the `addTaskUnlessCancelled` method without a preference, and effectively means to inherit the outer context’s executor preference. You can also pass the [`globalConcurrentExecutor`](../globalconcurrentexecutor.md) global executor explicitly.
- `priority`: The priority of the operation task. Omit this parameter or pass `nil` to inherit the task group’s base priority.
- `operation`: The operation to execute as part of the task group.

## See Also

### Adding Tasks to a Throwing Task Group
- [func addTask(priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult)](./addtask%28priority,operation%29.md)
  Adds a child task to the group.
- [func addTask(executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult)](./addtask%28executorpreference,priority,operation%29.md)
  Adds a child task to the group.
- [func addTask(name: String?, priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult)](./addtask%28name,priority,operation%29.md)
  Adds a child task to the group.
- [func addTask(name: String?, executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult)](./addtask%28name,executorpreference,priority,operation%29.md)
  Adds a child task to the group.
- [func addTaskUnlessCancelled(priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult) -> Bool](./addtaskunlesscancelled%28priority,operation%29.md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addTaskUnlessCancelled(executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult) -> Bool](./addtaskunlesscancelled%28executorpreference,priority,operation%29.md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addTaskUnlessCancelled(name: String?, priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult) -> Bool](./addtaskunlesscancelled%28name,priority,operation%29.md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addImmediateTask(name: String?, priority: TaskPriority?, executorPreference: consuming (any TaskExecutor)?, operation: sending () async throws -> ChildTaskResult)](./addimmediatetask%28name,priority,executorpreference,operation%29.md)
  Add a child task to the group and immediately start running it in the context of the calling thread/task.
- [func addImmediateTaskUnlessCancelled(name: String?, priority: TaskPriority?, executorPreference: consuming (any TaskExecutor)?, operation: sending () async throws -> ChildTaskResult) -> Bool](./addimmediatetaskunlesscancelled%28name,priority,executorpreference,operation%29.md)
  Add a child task to the group and immediately start running it in the context of the calling thread/task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/addtaskunlesscancelled(name:executorpreference:priority:operation:))*