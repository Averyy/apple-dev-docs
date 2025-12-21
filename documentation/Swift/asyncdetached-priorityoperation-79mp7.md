# asyncDetached(priority:operation:)

**Framework**: Swift  
**Kind**: func

Deprecated, available only for source compatibility reasons.

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
@discardableResult
func asyncDetached<Success>(priority: TaskPriority? = nil, operation: @escaping @isolated(any) () async throws -> Success) -> Task<Success, any Error> where Success : Sendable
```

## See Also

- [func async<Success>(priority: TaskPriority?, operation: () async throws -> Success) -> Task<Success, any Error>](async(priority:operation:)-2y0dc.md)
  Deprecated, available only for source compatibility reasons.
- [func async<Success>(priority: TaskPriority?, operation: () async -> Success) -> Task<Success, Never>](async(priority:operation:)-684z0.md)
  Deprecated, available only for source compatibility reasons.
- [func asyncDetached<Success>(priority: TaskPriority?, operation: () async -> Success) -> Task<Success, Never>](asyncdetached(priority:operation:)-6wbk6.md)
  Deprecated, available only for source compatibility reasons.
- [func detach<Success>(priority: TaskPriority?, operation: () async throws -> Success) -> Task<Success, any Error>](detach(priority:operation:)-2h9ty.md)
  Deprecated, available only for source compatibility reasons.
- [func detach<Success>(priority: TaskPriority?, operation: () async -> Success) -> Task<Success, Never>](detach(priority:operation:)-4948v.md)
  Deprecated, available only for source compatibility reasons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncdetached(priority:operation:)-79mp7)*