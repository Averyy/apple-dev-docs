# addTask(executorPreference:priority:operation:)

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
mutating func addTask(executorPreference taskExecutor: (any TaskExecutor)? = nil, priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async -> ChildTaskResult)
```

## Parameters

- `taskExecutor`: 
- `priority`: The priority of the operation task.   Omit this parameter or pass   to inherit the task group’s base priority.   Omit this parameter or pass    to set the child task’s priority to the priority of the group.
- `operation`: The operation to execute as part of the task group.

## See Also

- [func addTaskUnlessCancelled(executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> ChildTaskResult) -> Bool](taskgroup/addtaskunlesscancelled(executorpreference:priority:operation:).md)
  Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/taskgroup/addtask(executorpreference:priority:operation:))*