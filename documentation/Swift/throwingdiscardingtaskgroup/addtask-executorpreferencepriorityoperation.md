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
mutating func addTask(executorPreference taskExecutor: (any TaskExecutor)? = nil, priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async throws -> Void)
```

#### Discussion

This method doesn’t throw an error, even if the child task does. Instead, the corresponding call to `ThrowingTaskGroup.next()` rethrows that error.

## Parameters

- `taskExecutor`: The task executor that the child task should be started on and keep using.   Explicitly passing   as the executor preference is equivalent to   calling the   method without a preference, and effectively   means to inherit the outer context’s executor preference.   You can also pass the   global executor explicitly.
- `priority`: The priority of the operation task.   Omit this parameter or pass   to inherit the task group’s base priority.
- `operation`: The operation to execute as part of the task group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingdiscardingtaskgroup/addtask(executorpreference:priority:operation:))*