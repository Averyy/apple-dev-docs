# MediaSessionError

**Framework**: Now Playing  
**Kind**: enum

Errors that can occur during local session operations.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum MediaSessionError
```

## Topics

### Enumeration Cases
- [MediaSessionError.internalFailure](mediasessionerror/internalfailure.md)
  An internal system error occurred.
- [MediaSessionError.invalidState](mediasessionerror/invalidstate.md)
  The operation is not supported in the current state.
- [MediaSessionError.sessionInvalidated](mediasessionerror/sessioninvalidated.md)
  The session is already invalidated.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Publishing media sessions](publishing-media-sessions.md)
  Show your app’s media on the Lock Screen and Control Center.
- [protocol MediaSessionRepresentable](mediasessionrepresentable.md)
  A protocol that provides content metadata, playback state, and commands for a Now Playing session.
- [class MediaSession](mediasession.md)
  A local Now Playing session that publishes metadata and commands to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediasessionerror)*