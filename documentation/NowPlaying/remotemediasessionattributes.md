# RemoteMediaSessionAttributes

**Framework**: Now Playing  
**Kind**: protocol

A type that represents attributes for remote sessions.

**Availability**:
- iOS 27.0+ (Beta)
- iOS App Extension 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
protocol RemoteMediaSessionAttributes : Decodable, Encodable
```

## Mentions

- [Publishing remote media sessions](publishing-remote-media-sessions.md)

#### Overview

Conform to this protocol to define the data that configures your remote sessions. Attributes identify sessions and communicate session state between your app and extension. The attributes must be encodable for transmission and uniquely identifiable.

Your host app’s [`RemoteMediaSession`](remotemediasession.md) and your [`RemoteMediaSessionExtension`](remotemediasessionextension.md) share the same attributes type: the host encodes it when starting or updating a session, and the extension decodes it to create or refresh a session.

## Topics

### Instance Properties
- [var id: String](remotemediasessionattributes/id.md)
  A stable, unique identifier for the session these attributes describe.

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)

## See Also

- [Publishing remote media sessions](publishing-remote-media-sessions.md)
  Show media from an external device on the Lock Screen and Control Center.
- [protocol RemoteMediaSessionRepresentable](remotemediasessionrepresentable.md)
  A session that plays remotely, potentially across multiple devices.
- [class RemoteMediaSession](remotemediasession.md)
  A session that manages remote media playback across devices.
- [protocol RemoteMediaSessionExtension](remotemediasessionextension.md)
  An app extension that provides remote media sessions.
- [class RemoteMediaSessionExtensionConfiguration](remotemediasessionextensionconfiguration.md)
  The configuration object for a remote playback extension.
- [enum RemoteMediaSessionError](remotemediasessionerror.md)
  Errors that can occur during remote session operations.
- [struct MediaDevice](mediadevice.md)
  A device that plays media in a remote session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/remotemediasessionattributes)*