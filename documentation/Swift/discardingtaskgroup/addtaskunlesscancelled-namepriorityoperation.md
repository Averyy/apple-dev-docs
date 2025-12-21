# addTaskUnlessCancelled(name:priority:operation:)

**Framework**: Swift  
**Kind**: method

Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.

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
mutating func addTaskUnlessCancelled(name: String?, priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async -> Void) -> Bool
```

#### Return Value

`true` if the child task was added to the group; otherwise `false`.

## Parameters

- `name`: Human readable name of this task.
- `priority`: The priority of the operation task.   Omit this parameter or pass   to inherit the task group’s base priority.
- `operation`: The operation to execute as part of the task group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/discardingtaskgroup/addtaskunlesscancelled(name:priority:operation:))*