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

## Declaration

```swift
mutating func add(priority: TaskPriority? = nil, operation: @escaping @Sendable () async throws -> ChildTaskResult) async -> Bool
```

## See Also

- [func async(priority: TaskPriority?, operation: () async throws -> ChildTaskResult)](throwingtaskgroup/async(priority:operation:).md)
- [func asyncUnlessCancelled(priority: TaskPriority?, operation: () async throws -> ChildTaskResult) -> Bool](throwingtaskgroup/asyncunlesscancelled(priority:operation:).md)
- [func nextResult(isolation: isolated (any Actor)?) async -> Result<ChildTaskResult, Failure>?](throwingtaskgroup/nextresult(isolation:).md)
- [func spawn(priority: TaskPriority?, operation: () async throws -> ChildTaskResult)](throwingtaskgroup/spawn(priority:operation:).md)
- [func spawnUnlessCancelled(priority: TaskPriority?, operation: () async throws -> ChildTaskResult) -> Bool](throwingtaskgroup/spawnunlesscancelled(priority:operation:).md)
- [func waitForAll(isolation: isolated (any Actor)?) async throws](throwingtaskgroup/waitforall(isolation:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/add(priority:operation:))*