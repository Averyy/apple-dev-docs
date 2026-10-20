# RemoteMediaSessionError

**Framework**: Now Playing  
**Kind**: enum  
**Role**: Enumeration

Errors that can occur during remote session operations.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
enum RemoteMediaSessionError
```

## Topics

### Enumeration Cases
- [RemoteMediaSessionError.internalFailure](./remotemediasessionerror/internalfailure.md)
  An internal system error occurred.
- [RemoteMediaSessionError.invalidAttributes](./remotemediasessionerror/invalidattributes.md)
  The given attributes argument does not match the current session.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Error](../Swift/error.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Remote sessions
- [Publishing remote media sessions](./publishing-remote-media-sessions.md)
  Show media from an external device on the Lock Screen and Control Center.
- [protocol RemoteMediaSessionRepresentable](./remotemediasessionrepresentable.md)
  A session that plays remotely, potentially across multiple devices.
- [class RemoteMediaSession](./remotemediasession.md)
  A session that manages remote media playback across devices.
- [protocol RemoteMediaSessionExtension](./remotemediasessionextension.md)
  An app extension that provides remote media sessions.
- [class RemoteMediaSessionExtensionConfiguration](./remotemediasessionextensionconfiguration.md)
  The configuration object for a remote playback extension.
- [protocol RemoteMediaSessionAttributes](./remotemediasessionattributes.md)
  A type that represents attributes for remote sessions.
- [struct MediaDevice](./mediadevice.md)
  A device that plays media in a remote session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/remotemediasessionerror)*