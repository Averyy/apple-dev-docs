# isOwner

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the calling process owns the entity.

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
@preconcurrency var isOwner: Bool { get }
```

#### Discussion

The calling process owns the entity if the value is `true`.

## See Also

### Managing ownership
- [func requestOwnership(timeout: TimeInterval, (SynchronizationComponent.OwnershipTransferCompletionResult) -> Void)](./requestownership%28timeout,_%29.md)
  Requests ownership of the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hassynchronization/isowner)*