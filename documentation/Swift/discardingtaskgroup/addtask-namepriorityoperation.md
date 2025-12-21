# addTask(name:priority:operation:)

**Framework**: Swift  
**Kind**: method

Adds a child task to the group.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
mutating func addTask(name: String?, priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async -> Void)
```

## Parameters

- `name`: Human readable name of this task.
- `priority`: The priority of the operation task.   Omit this parameter or pass   to inherit the task group’s base priority.
- `operation`: The operation to execute as part of the task group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/discardingtaskgroup/addtask(name:priority:operation:))*