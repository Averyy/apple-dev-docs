# addImmediateTask(name:priority:executorPreference:operation:)

**Framework**: Swift  
**Kind**: method

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
mutating func addImmediateTask(name: String? = nil, priority: TaskPriority? = nil, executorPreference taskExecutor: consuming (any TaskExecutor)? = nil, operation: sending @escaping @isolated(any) () async throws -> ChildTaskResult)
```

#### Discussion

This function  the created task on the calling context. The task will continue executing on the caller’s context until it suspends, and after suspension will resume on the adequate executor. For a nonisolated operation this means running on the global concurrent pool, and on an isolated operation it means the appropriate executor of that isolation context.

As indicated by the lack of `async` on this method, this method does  suspend, and instead takes over the calling task’s (thread’s) execution in a synchronous manner.

Other than the execution semantics discussed above, the created task is semantically equivalent to its basic version which can be created using `ThrowingTaskGroup/addTask`.

## Parameters

- `name`: Human readable name of this task.
- `priority`: The priority of the operation task.   Omit this parameter or pass   to inherit the task group’s base priority.
- `taskExecutor`: The task executor that the child task should be started on and keep using.   Explicitly passing   as the executor preference is equivalent to   calling the   method without a preference, and effectively   means to inherit the outer context’s executor preference.   You can also pass the   global executor explicitly.
- `operation`: The operation to execute as part of the task group.

## See Also

- [func addTask(priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult)](throwingtaskgroup/addtask(priority:operation:).md)
  Adds a child task to the group.
- [func addTask(executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult)](throwingtaskgroup/addtask(executorpreference:priority:operation:).md)
  Adds a child task to the group.
- [func addTask(name: String?, priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult)](throwingtaskgroup/addtask(name:priority:operation:).md)
  Adds a child task to the group.
- [func addTask(name: String?, executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult)](throwingtaskgroup/addtask(name:executorpreference:priority:operation:).md)
  Adds a child task to the group.
- [func addTaskUnlessCancelled(priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult) -> Bool](throwingtaskgroup/addtaskunlesscancelled(priority:operation:).md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addTaskUnlessCancelled(name: String?, executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult) -> Bool](throwingtaskgroup/addtaskunlesscancelled(name:executorpreference:priority:operation:).md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addTaskUnlessCancelled(executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult) -> Bool](throwingtaskgroup/addtaskunlesscancelled(executorpreference:priority:operation:).md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addTaskUnlessCancelled(name: String?, priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult) -> Bool](throwingtaskgroup/addtaskunlesscancelled(name:priority:operation:).md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addImmediateTaskUnlessCancelled(name: String?, priority: TaskPriority?, executorPreference: consuming (any TaskExecutor)?, operation: sending () async throws -> ChildTaskResult) -> Bool](throwingtaskgroup/addimmediatetaskunlesscancelled(name:priority:executorpreference:operation:).md)
  Add a child task to the group and immediately start running it in the context of the calling thread/task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/addimmediatetask(name:priority:executorpreference:operation:))*