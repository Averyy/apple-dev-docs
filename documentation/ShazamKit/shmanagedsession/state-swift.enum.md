# SHManagedSession.State

**Framework**: ShazamKit  
**Kind**: enum  
**Role**: Enumeration

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
- [SHManagedSession.State.idle](./state-swift.enum/idle.md)
  The session isn’t recording or making a match attempt.
- [SHManagedSession.State.matching](./state-swift.enum/matching.md)
  The session is recording and making at least one match attempt.
- [SHManagedSession.State.prerecording](./state-swift.enum/prerecording.md)
  The session has the resources it needs for matching and is prerecording.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the session state
- [var state: SHManagedSession.State](./state-swift.property.md)
  The current state of the managed session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmanagedsession/state-swift.enum)*