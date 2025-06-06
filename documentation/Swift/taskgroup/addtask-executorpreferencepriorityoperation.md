# addTask(executorPreference:priority:operation:)

**Framework**: Swift  
**Kind**: method

Adds a child task to the group and enqueue it on the specified executor.

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
mutating func addTask(executorPreference taskExecutor: (any TaskExecutor)?, priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async -> ChildTaskResult)
```

## Parameters

- `taskExecutor`: The task executor that the child task should be started on and keep using.   Explicitly passing   as the executor preference is equivalent to   calling the   method without a preference, and effectively   means to inherit the outer context’s executor preference.
- `priority`: The priority of the operation task.   Omit this parameter or pass    to set the child task’s priority to the priority of the group.
- `operation`: The operation to execute as part of the task group.

## See Also

- [func addTaskUnlessCancelled(executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> ChildTaskResult) -> Bool](taskgroup/addtaskunlesscancelled(executorpreference:priority:operation:).md)
  Adds a child task to the group and enqueue it on the specified executor, unless the group has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/taskgroup/addtask(executorpreference:priority:operation:))*