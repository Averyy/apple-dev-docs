# spawnUnlessCancelled(priority:operation:)

**Framework**: Swift  
**Kind**: method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+
- Unknown ?+ - Deprecated
- tvOS 13.0+

## Declaration

```swift
mutating func spawnUnlessCancelled(priority: TaskPriority? = nil, operation: @escaping () async throws -> ChildTaskResult) -> Bool
```

## See Also

- [func add(priority: TaskPriority?, operation: () async throws -> ChildTaskResult) async -> Bool](throwingtaskgroup/add(priority:operation:).md)
- [func async(priority: TaskPriority?, operation: () async throws -> ChildTaskResult)](throwingtaskgroup/async(priority:operation:).md)
- [func asyncUnlessCancelled(priority: TaskPriority?, operation: () async throws -> ChildTaskResult) -> Bool](throwingtaskgroup/asyncunlesscancelled(priority:operation:).md)
- [func spawn(priority: TaskPriority?, operation: () async throws -> ChildTaskResult)](throwingtaskgroup/spawn(priority:operation:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/spawnunlesscancelled(priority:operation:))*