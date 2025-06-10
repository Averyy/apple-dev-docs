# isOwner

**Framework**: RealityKit  
**Kind**: property

A Boolean that indicates whether the calling process owns the entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var isOwner: Bool { get }
```

#### Discussion

The calling process owns the entity if the value is `true`.

## See Also

- [func requestOwnership(timeout: TimeInterval, (SynchronizationComponent.OwnershipTransferCompletionResult) -> Void)](hassynchronization/requestownership(timeout:_:).md)
  Requests ownership of the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hassynchronization/isowner)*