# requestOwnership(timeout:_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Requests ownership of the entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func requestOwnership(timeout: TimeInterval = 15, _ callback: @escaping (SynchronizationComponent.OwnershipTransferCompletionResult) -> Void)
```

#### Discussion

Requesting ownership isn’t guaranteed to succeed.

## Parameters

- `timeout`: A time in seconds to wait before giving up.
- `callback`: A closure that the method calls when the request completes or times out.

## See Also

### Managing ownership
- [var isOwner: Bool](./isowner.md)
  A Boolean that indicates whether the calling process owns the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hassynchronization/requestownership(timeout:_:))*