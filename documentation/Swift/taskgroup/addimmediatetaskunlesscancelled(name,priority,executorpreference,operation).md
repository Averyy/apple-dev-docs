# addImmediateTaskUnlessCancelled(name:priority:executorPreference:operation:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Add a child task to the group and immediately start running it in the context of the calling thread/task.

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
mutating func addImmediateTaskUnlessCancelled(name: String? = nil, priority: TaskPriority? = nil, executorPreference taskExecutor: consuming (any TaskExecutor)? = nil, operation: sending @escaping @isolated(any) () async -> ChildTaskResult) -> Bool
```

Available when `ChildTaskResult` conforms to `Sendable`.

#### Return Value

`true` if the child task was added to the group; otherwise `false`.

#### Discussion

This function *starts* the created task on the calling context. The task will continue executing on the caller’s context until it suspends, and after suspension will resume on the adequate executor. For a nonisolated operation this means running on the global concurrent pool, and on an isolated operation it means the appropriate executor of that isolation context.

As indicated by the lack of `async` on this method, this method does *not* suspend, and instead takes over the calling task’s (thread’s) execution in a synchronous manner.

Other than the execution semantics discussed above, the created task is semantically equivalent to its basic version which can be created using [`addTask(priority:operation:)`](./addtask%28priority,operation%29.md).

## Parameters

- `name`: Human readable name of this task.
- `priority`: The priority of the operation task. Omit this parameter or pass `nil` to inherit the task group’s base priority.
- `taskExecutor`: The task executor that the child task should be started on and keep using. Explicitly passing `nil` as the executor preference is equivalent to calling the `addImmediateTaskUnlessCancelled` method without a preference, and effectively means to inherit the outer context’s executor preference. You can also pass the [`globalConcurrentExecutor`](../globalconcurrentexecutor.md) global executor explicitly.
- `operation`: The operation to execute as part of the task group.

## See Also

### Adding Tasks to a Task Group
- [func addTask(priority: TaskPriority?, operation: sending () async -> ChildTaskResult)](./addtask%28priority,operation%29.md)
  Adds a child task to the group.
- [func addTask(name: String?, priority: TaskPriority?, operation: sending () async -> ChildTaskResult)](./addtask%28name,priority,operation%29.md)
  Adds a child task to the group.
- [func addTask(executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> ChildTaskResult)](./addtask%28executorpreference,priority,operation%29.md)
  Adds a child task to the group.
- [func addTask(name: String?, executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> ChildTaskResult)](./addtask%28name,executorpreference,priority,operation%29.md)
  Adds a child task to the group.
- [func addTaskUnlessCancelled(name: String?, executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> ChildTaskResult) -> Bool](./addtaskunlesscancelled%28name,executorpreference,priority,operation%29.md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addTaskUnlessCancelled(executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> ChildTaskResult) -> Bool](./addtaskunlesscancelled%28executorpreference,priority,operation%29.md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addTaskUnlessCancelled(name: String?, priority: TaskPriority?, operation: sending () async -> ChildTaskResult) -> Bool](./addtaskunlesscancelled%28name,priority,operation%29.md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addTaskUnlessCancelled(priority: TaskPriority?, operation: sending () async -> ChildTaskResult) -> Bool](./addtaskunlesscancelled%28priority,operation%29.md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addImmediateTask(name: String?, priority: TaskPriority?, executorPreference: consuming (any TaskExecutor)?, operation: sending () async -> ChildTaskResult)](./addimmediatetask%28name,priority,executorpreference,operation%29.md)
  Add a child task to the group and immediately start running it in the context of the calling thread/task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/taskgroup/addimmediatetaskunlesscancelled(name:priority:executorpreference:operation:))*