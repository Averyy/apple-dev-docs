# detach(priority:operation:)

**Framework**: Swift  
**Kind**: func  
**Role**: Function

Deprecated, available only for source compatibility reasons.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

> **Deprecated**: `detach` was replaced by `Task.detached` and will be removed shortly.

## Declaration

```swift
@discardableResult
func detach<Success>(priority: TaskPriority? = nil, operation: @escaping @isolated(any) @Sendable () async -> Success) -> Task<Success, Never> where Success : Sendable
```

## See Also

### Deprecated Functions
- [func async<Success>(priority: TaskPriority?, operation: () async throws -> Success) -> Task<Success, any Error>](./async%28priority,operation%29-2y0dc.md)
  Deprecated, available only for source compatibility reasons.
- [func async<Success>(priority: TaskPriority?, operation: () async -> Success) -> Task<Success, Never>](./async%28priority,operation%29-684z0.md)
  Deprecated, available only for source compatibility reasons.
- [func asyncDetached<Success>(priority: TaskPriority?, operation: () async -> Success) -> Task<Success, Never>](./asyncdetached%28priority,operation%29-6wbk6.md)
  Deprecated, available only for source compatibility reasons.
- [func asyncDetached<Success>(priority: TaskPriority?, operation: () async throws -> Success) -> Task<Success, any Error>](./asyncdetached%28priority,operation%29-79mp7.md)
  Deprecated, available only for source compatibility reasons.
- [func asyncDetached<Success>(priority: TaskPriority?, operation: () async throws -> Success) -> Task<Success, any Error>](./asyncdetached%28priority,operation%29-79mp7.md)
  Deprecated, available only for source compatibility reasons.
- [func detach<Success>(priority: TaskPriority?, operation: () async throws -> Success) -> Task<Success, any Error>](./detach%28priority,operation%29-2h9ty.md)
  Deprecated, available only for source compatibility reasons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/detach(priority:operation:)-4948v)*