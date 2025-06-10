# addTaskUnlessCancelled(executorPreference:priority:operation:)

**Framework**: Swift  
**Kind**: method

Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.

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
mutating func addTaskUnlessCancelled(executorPreference taskExecutor: (any TaskExecutor)? = nil, priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async -> Void) -> Bool
```

#### Return Value

`true` if the child task was added to the group; otherwise `false`.

## Parameters

- `taskExecutor`: 
- `priority`: The priority of the operation task.   Omit this parameter or pass   to inherit the task group’s base priority.   Omit this parameter or pass    to set the child task’s priority to the priority of the group.
- `operation`: The operation to execute as part of the task group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/discardingtaskgroup/addtaskunlesscancelled(executorpreference:priority:operation:))*