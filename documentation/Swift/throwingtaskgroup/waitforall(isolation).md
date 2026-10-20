# waitForAll(isolation:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

> **Deprecated**: Replaced by nonisolated(nonsending) overload

## Declaration

```swift
mutating func waitForAll(isolation: isolated (any Actor)? = #isolation) async throws
```

## See Also

### Deprecated
- [func add(priority: TaskPriority?, operation: () async throws -> ChildTaskResult) async -> Bool](./add%28priority,operation%29.md)
- [func async(priority: TaskPriority?, operation: () async throws -> ChildTaskResult)](./async%28priority,operation%29.md)
- [func asyncUnlessCancelled(priority: TaskPriority?, operation: () async throws -> ChildTaskResult) -> Bool](./asyncunlesscancelled%28priority,operation%29.md)
- [func nextResult(isolation: isolated (any Actor)?) async -> Result<ChildTaskResult, Failure>?](./nextresult%28isolation%29.md)
- [func spawn(priority: TaskPriority?, operation: () async throws -> ChildTaskResult)](./spawn%28priority,operation%29.md)
- [func spawnUnlessCancelled(priority: TaskPriority?, operation: () async throws -> ChildTaskResult) -> Bool](./spawnunlesscancelled%28priority,operation%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/waitforall(isolation:))*