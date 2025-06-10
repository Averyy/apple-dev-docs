# addTask(name:executorPreference:priority:operation:)

**Framework**: Swift  
**Kind**: method

Adds a child task to the group.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
mutating func addTask(name: String?, executorPreference taskExecutor: (any TaskExecutor)? = nil, priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async throws -> ChildTaskResult)
```

#### Discussion

This method doesn’t throw an error, even if the child task does. Instead, the corresponding call to `ThrowingTaskGroup.next()` rethrows that error.

## Parameters

- `name`: Human readable name of this task.
- `taskExecutor`: 
- `priority`: The priority of the operation task.   Omit this parameter or pass   to inherit the task group’s base priority.   Omit this parameter or pass    to set the child task’s priority to the priority of the group.
- `operation`: The operation to execute as part of the task group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/addtask(name:executorpreference:priority:operation:))*