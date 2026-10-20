# async(priority:operation:)

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

## Declaration

```swift
mutating func async(priority: TaskPriority? = nil, operation: @escaping @Sendable () async -> ChildTaskResult)
```

## See Also

- [func add(priority: TaskPriority?, operation: () async -> ChildTaskResult) async -> Bool](taskgroup/add(priority:operation:).md)
- [func asyncUnlessCancelled(priority: TaskPriority?, operation: () async -> ChildTaskResult) -> Bool](taskgroup/asyncunlesscancelled(priority:operation:).md)
- [func spawn(priority: TaskPriority?, operation: () async -> ChildTaskResult)](taskgroup/spawn(priority:operation:).md)
- [func spawnUnlessCancelled(priority: TaskPriority?, operation: () async -> ChildTaskResult) -> Bool](taskgroup/spawnunlesscancelled(priority:operation:).md)
- [func waitForAll(isolation: isolated (any Actor)?) async](taskgroup/waitforall(isolation:).md)
  Wait for all of the group’s remaining tasks to complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/taskgroup/async(priority:operation:))*