# addTaskUnlessCancelled(name:priority:operation:)

**Framework**: Swift  
**Kind**: method

Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.

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
mutating func addTaskUnlessCancelled(name: String?, priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async -> ChildTaskResult) -> Bool
```

#### Return Value

`true` if the child task was added to the group; otherwise `false`.

## Parameters

- `name`: Human readable name of this task.
- `priority`: The priority of the operation task.   Omit this parameter or pass   to inherit the task group’s base priority.
- `operation`: The operation to execute as part of the task group.

## See Also

- [func addTask(priority: TaskPriority?, operation: sending () async -> ChildTaskResult)](taskgroup/addtask(priority:operation:).md)
  Adds a child task to the group.
- [func addTask(name: String?, priority: TaskPriority?, operation: sending () async -> ChildTaskResult)](taskgroup/addtask(name:priority:operation:).md)
  Adds a child task to the group.
- [func addTask(executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> ChildTaskResult)](taskgroup/addtask(executorpreference:priority:operation:).md)
  Adds a child task to the group.
- [func addTask(name: String?, executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> ChildTaskResult)](taskgroup/addtask(name:executorpreference:priority:operation:).md)
  Adds a child task to the group.
- [func addTaskUnlessCancelled(name: String?, executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> ChildTaskResult) -> Bool](taskgroup/addtaskunlesscancelled(name:executorpreference:priority:operation:).md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addTaskUnlessCancelled(executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> ChildTaskResult) -> Bool](taskgroup/addtaskunlesscancelled(executorpreference:priority:operation:).md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addTaskUnlessCancelled(priority: TaskPriority?, operation: sending () async -> ChildTaskResult) -> Bool](taskgroup/addtaskunlesscancelled(priority:operation:).md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.
- [func addImmediateTask(name: String?, priority: TaskPriority?, executorPreference: consuming (any TaskExecutor)?, operation: sending () async -> ChildTaskResult)](taskgroup/addimmediatetask(name:priority:executorpreference:operation:).md)
  Add a child task to the group and immediately start running it in the context of the calling thread/task.
- [func addImmediateTaskUnlessCancelled(name: String?, priority: TaskPriority?, executorPreference: consuming (any TaskExecutor)?, operation: sending () async -> ChildTaskResult) -> Bool](taskgroup/addimmediatetaskunlesscancelled(name:priority:executorpreference:operation:).md)
  Add a child task to the group and immediately start running it in the context of the calling thread/task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/taskgroup/addtaskunlesscancelled(name:priority:operation:))*