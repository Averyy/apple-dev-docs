# addTaskUnlessCancelled(executorPreference:priority:operation:)

**Framework**: Swift  
**Kind**: method

Adds a child task to the group and enqueue it on the specified executor, unless the group has been canceled.

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
mutating func addTaskUnlessCancelled(executorPreference taskExecutor: (any TaskExecutor)?, priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async throws -> ChildTaskResult) -> Bool
```

#### Return Value

`true` if the child task was added to the group; otherwise `false`.

## Parameters

- `taskExecutor`: The task executor that the child task should be started on and keep using.
- `priority`: The priority of the operation task.   Omit this parameter or pass    to set the child task’s priority to the priority of the group.
- `operation`: The operation to execute as part of the task group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/addtaskunlesscancelled(executorpreference:priority:operation:))*