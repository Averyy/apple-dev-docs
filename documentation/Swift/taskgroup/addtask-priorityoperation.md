# addTask(priority:operation:)

**Framework**: Swift  
**Kind**: method

Adds a child task to the group.

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
mutating func addTask(priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async -> ChildTaskResult)
```

## Parameters

- `priority`: The priority of the operation task.   Omit this parameter or pass   to inherit the task group’s base priority.   Omit this parameter or pass    to set the child task’s priority to the priority of the group.
- `operation`: The operation to execute as part of the task group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/taskgroup/addtask(priority:operation:))*