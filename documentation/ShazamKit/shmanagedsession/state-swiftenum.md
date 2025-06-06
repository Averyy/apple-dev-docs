# SHManagedSession.State

**Framework**: ShazamKit  
**Kind**: enum

The state of a managed session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@frozen
enum State
```

## Topics

### Getting session states
- [SHManagedSession.State.idle](shmanagedsession/state-swift.enum/idle.md)
  The session isn’t recording or making a match attempt.
- [SHManagedSession.State.matching](shmanagedsession/state-swift.enum/matching.md)
  The session is recording and making at least one match attempt.
- [SHManagedSession.State.prerecording](shmanagedsession/state-swift.enum/prerecording.md)
  The session has the resources it needs for matching and is prerecording.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var state: SHManagedSession.State](shmanagedsession/state-swift.property.md)
  The current state of the managed session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmanagedsession/state-swift.enum)*