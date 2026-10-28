# addTaskUnlessCancelled(priority:operation:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

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
mutating func addTaskUnlessCancelled(priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async -> ChildTaskResult) -> Bool
```

Available when `ChildTaskResult` conforms to `Sendable`.

## Return Value

`true` if the child task was added to the group; otherwise `false`.

## Parameters

- `priority`: The priority of the operation task. Omit this parameter or pass `nil` to inherit the task group’s base priority.
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
- [func addImmediateTask(name: String?, priority: TaskPriority?, executorPreference: consuming (any TaskExecutor)?, operation: sending () async -> ChildTaskResult)](./addimmediatetask%28name,priority,executorpreference,operation%29.md)
  Add a child task to the group and immediately start running it in the context of the calling thread/task.
- [func addImmediateTaskUnlessCancelled(name: String?, priority: TaskPriority?, executorPreference: consuming (any TaskExecutor)?, operation: sending () async -> ChildTaskResult) -> Bool](./addimmediatetaskunlesscancelled%28name,priority,executorpreference,operation%29.md)
  Add a child task to the group and immediately start running it in the context of the calling thread/task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/taskgroup/addtaskunlesscancelled(priority:operation:))*