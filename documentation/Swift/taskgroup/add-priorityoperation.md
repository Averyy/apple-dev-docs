# add(priority:operation:)

**Framework**: Swift  
**Kind**: method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
mutating func add(priority: TaskPriority? = nil, operation: @escaping () async -> ChildTaskResult) async -> Bool
```

## See Also

- [func async(priority: TaskPriority?, operation: () async -> ChildTaskResult)](taskgroup/async(priority:operation:).md)
- [func asyncUnlessCancelled(priority: TaskPriority?, operation: () async -> ChildTaskResult) -> Bool](taskgroup/asyncunlesscancelled(priority:operation:).md)
- [func spawn(priority: TaskPriority?, operation: () async -> ChildTaskResult)](taskgroup/spawn(priority:operation:).md)
- [func spawnUnlessCancelled(priority: TaskPriority?, operation: () async -> ChildTaskResult) -> Bool](taskgroup/spawnunlesscancelled(priority:operation:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/taskgroup/add(priority:operation:))*