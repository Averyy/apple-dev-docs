# detach(priority:operation:)

**Framework**: Swift  
**Kind**: func

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
@discardableResult
func detach<T>(priority: TaskPriority? = nil, operation: @escaping () async throws -> T) -> Task<T, any Error> where T : Sendable
```

## See Also

- [func async<T>(priority: TaskPriority?, operation: () async -> T) -> Task<T, Never>](async(priority:operation:)-6nw1p.md)
- [func async<T>(priority: TaskPriority?, operation: () async throws -> T) -> Task<T, any Error>](async(priority:operation:)-6ud0e.md)
- [func asyncDetached<T>(priority: TaskPriority?, operation: () async -> T) -> Task<T, Never>](asyncdetached(priority:operation:)-3np0.md)
- [func asyncDetached<T>(priority: TaskPriority?, operation: () async throws -> T) -> Task<T, any Error>](asyncdetached(priority:operation:)-493is.md)
- [func detach<T>(priority: TaskPriority?, operation: () async -> T) -> Task<T, Never>](detach(priority:operation:)-1z4ju.md)
- [func detach<T>(priority: TaskPriority?, operation: () async -> T) -> Task<T, Never>](detach(priority:operation:)-1z4ju.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/detach(priority:operation:)-4lt3t)*