# spawnUnlessCancelled(priority:operation:)

**Framework**: Swift  
**Kind**: method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+
- Unknown ?+ - Deprecated
- visionOS 1.0+

## Declaration

```swift
mutating func spawnUnlessCancelled(priority: TaskPriority? = nil, operation: @escaping () async -> ChildTaskResult) -> Bool
```

## See Also

- [func add(priority: TaskPriority?, operation: () async -> ChildTaskResult) async -> Bool](taskgroup/add(priority:operation:).md)
- [func async(priority: TaskPriority?, operation: () async -> ChildTaskResult)](taskgroup/async(priority:operation:).md)
- [func asyncUnlessCancelled(priority: TaskPriority?, operation: () async -> ChildTaskResult) -> Bool](taskgroup/asyncunlesscancelled(priority:operation:).md)
- [func spawn(priority: TaskPriority?, operation: () async -> ChildTaskResult)](taskgroup/spawn(priority:operation:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/taskgroup/spawnunlesscancelled(priority:operation:))*