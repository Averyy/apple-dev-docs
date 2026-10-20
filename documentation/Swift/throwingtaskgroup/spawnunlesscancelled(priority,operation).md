# spawnUnlessCancelled(priority:operation:)

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

## Declaration

```swift
mutating func spawnUnlessCancelled(priority: TaskPriority? = nil, operation: @escaping @Sendable () async throws -> ChildTaskResult) -> Bool
```

Available when `ChildTaskResult` conforms to `Sendable` and `Failure` conforms to `Error`.

## See Also

### Deprecated
- [func add(priority: TaskPriority?, operation: () async throws -> ChildTaskResult) async -> Bool](./add%28priority,operation%29.md)
- [func async(priority: TaskPriority?, operation: () async throws -> ChildTaskResult)](./async%28priority,operation%29.md)
- [func asyncUnlessCancelled(priority: TaskPriority?, operation: () async throws -> ChildTaskResult) -> Bool](./asyncunlesscancelled%28priority,operation%29.md)
- [func nextResult(isolation: isolated (any Actor)?) async -> Result<ChildTaskResult, Failure>?](./nextresult%28isolation%29.md)
- [func spawn(priority: TaskPriority?, operation: () async throws -> ChildTaskResult)](./spawn%28priority,operation%29.md)
- [func waitForAll(isolation: isolated (any Actor)?) async throws](./waitforall%28isolation%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/spawnunlesscancelled(priority:operation:))*