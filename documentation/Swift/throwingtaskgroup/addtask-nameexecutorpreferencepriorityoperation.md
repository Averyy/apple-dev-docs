# addTask(name:executorPreference:priority:operation:)

**Framework**: Swift  
**Kind**: method

Adds a child task to the group.

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
mutating func addTask(name: String?, executorPreference taskExecutor: (any TaskExecutor)? = nil, priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async throws -> ChildTaskResult)
```

#### Discussion

This method doesn’t throw an error, even if the child task does. Instead, the corresponding call to `ThrowingTaskGroup.next()` rethrows that error.

## Parameters

- `name`: Human readable name of this task.
- `taskExecutor`: The task executor that the child task should be started on and keep using.   Explicitly passing   as the executor preference is equivalent to   calling the   method without a preference, and effectively   means to inherit the outer context’s executor preference.   You can also pass the   global executor explicitly.
- `priority`: The priority of the operation task.   Omit this parameter or pass   to inherit the task group’s base priority.
- `operation`: The operation to execute as part of the task group.

## See Also

- [func addTask(priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult)](throwingtaskgroup/addtask(priority:operation:).md)
  Adds a child task to the group.
- [func addTask(executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult)](throwingtaskgroup/addtask(executorpreference:priority:operation:).md)
  Adds a child task to the group.
- [func addTask(name: String?, priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult)](throwingtaskgroup/addtask(name:priority:operation:).md)
  Adds a child task to the group.
- [func addTaskUnlessCancelled(priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult) -> Bool](throwingtaskgroup/addtaskunlesscancelled(priority:operation:).md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addTaskUnlessCancelled(name: String?, executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult) -> Bool](throwingtaskgroup/addtaskunlesscancelled(name:executorpreference:priority:operation:).md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addTaskUnlessCancelled(executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult) -> Bool](throwingtaskgroup/addtaskunlesscancelled(executorpreference:priority:operation:).md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addTaskUnlessCancelled(name: String?, priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult) -> Bool](throwingtaskgroup/addtaskunlesscancelled(name:priority:operation:).md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addImmediateTask(name: String?, priority: TaskPriority?, executorPreference: consuming (any TaskExecutor)?, operation: sending () async throws -> ChildTaskResult)](throwingtaskgroup/addimmediatetask(name:priority:executorpreference:operation:).md)
  Add a child task to the group and immediately start running it in the context of the calling thread/task.
- [func addImmediateTaskUnlessCancelled(name: String?, priority: TaskPriority?, executorPreference: consuming (any TaskExecutor)?, operation: sending () async throws -> ChildTaskResult) -> Bool](throwingtaskgroup/addimmediatetaskunlesscancelled(name:priority:executorpreference:operation:).md)
  Add a child task to the group and immediately start running it in the context of the calling thread/task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/addtask(name:executorpreference:priority:operation:))*