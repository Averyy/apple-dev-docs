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
mutating func spawnUnlessCancelled(priority: TaskPriority? = nil, operation: @escaping @Sendable () async -> ChildTaskResult) -> Bool
```

Available when `ChildTaskResult` conforms to `Sendable`.

## See Also

### Deprecated
- [func add(priority: TaskPriority?, operation: () async -> ChildTaskResult) async -> Bool](./add%28priority,operation%29.md)
- [func async(priority: TaskPriority?, operation: () async -> ChildTaskResult)](./async%28priority,operation%29.md)
- [func asyncUnlessCancelled(priority: TaskPriority?, operation: () async -> ChildTaskResult) -> Bool](./asyncunlesscancelled%28priority,operation%29.md)
- [func spawn(priority: TaskPriority?, operation: () async -> ChildTaskResult)](./spawn%28priority,operation%29.md)
- [func waitForAll(isolation: isolated (any Actor)?) async](./waitforall%28isolation%29.md)
  Wait for all of the group’s remaining tasks to complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/taskgroup/spawnunlesscancelled(priority:operation:))*