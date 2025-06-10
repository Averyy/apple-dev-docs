# addTaskUnlessCancelled(priority:operation:)

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
mutating func addTaskUnlessCancelled(priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async throws -> ChildTaskResult) -> Bool
```

#### Return Value

`true` if the child task was added to the group; otherwise `false`.

#### Discussion

This method doesn’t throw an error, even if the child task does. Instead, the corresponding call to `ThrowingTaskGroup.next()` rethrows that error.

## Parameters

- `priority`: The priority of the operation task.   Omit this parameter or pass   to inherit the task group’s base priority.   Omit this parameter or pass    to set the child task’s priority to the priority of the group.
- `operation`: The operation to execute as part of the task group.

## See Also

- [func addTask(priority: TaskPriority?, operation: sending () async throws -> ChildTaskResult)](throwingtaskgroup/addtask(priority:operation:).md)
  Adds a child task to the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/addtaskunlesscancelled(priority:operation:))*