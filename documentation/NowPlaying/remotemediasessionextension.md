# RemoteMediaSessionExtension

**Framework**: Now Playing  
**Kind**: protocol

An app extension that provides remote media sessions.

**Availability**:
- iOS 27.0+ (Beta)
- iOS App Extension 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
protocol RemoteMediaSessionExtension<Attributes> : AppExtension
```

## Mentions

- [Publishing remote media sessions](publishing-remote-media-sessions.md)

#### Overview

Implement this protocol in your app extension to handle remote playback sessions.

For more information, see [`Publishing remote media sessions`](publishing-remote-media-sessions.md)

The following example shows a basic extension implementation:

```swift
@main
struct MyPlaybackExtension: RemoteMediaSessionExtension {
    var configuration: RemoteMediaSessionExtensionConfiguration<Self> {
        RemoteMediaSessionExtensionConfiguration(extension: self)
    }

    func session(_ attributes: MySessionAttributes) async throws -> MySession {
        return MySession(attributes: attributes)
    }
}
```

## Topics

### Associated Types
- [associatedtype Attributes](remotemediasessionextension/attributes.md)
  The type that represents attributes for your remote sessions.
- [associatedtype Session : RemoteMediaSessionRepresentable](remotemediasessionextension/session.md)
  The type of session this extension creates.
### Instance Methods
- [func session(Self.Attributes) async throws -> Self.Session](remotemediasessionextension/session(_:).md)
  Creates a session configured with the specified attributes.

## Relationships

### Inherits From
- [AppExtension](../extensionfoundation/appextension.md)

## See Also

- [Publishing remote media sessions](publishing-remote-media-sessions.md)
  Show media from an external device on the Lock Screen and Control Center.
- [protocol RemoteMediaSessionRepresentable](remotemediasessionrepresentable.md)
  A session that plays remotely, potentially across multiple devices.
- [class RemoteMediaSession](remotemediasession.md)
  A session that manages remote media playback across devices.
- [class RemoteMediaSessionExtensionConfiguration](remotemediasessionextensionconfiguration.md)
  The configuration object for a remote playback extension.
- [protocol RemoteMediaSessionAttributes](remotemediasessionattributes.md)
  A type that represents attributes for remote sessions.
- [enum RemoteMediaSessionError](remotemediasessionerror.md)
  Errors that can occur during remote session operations.
- [struct MediaDevice](mediadevice.md)
  A device that plays media in a remote session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/remotemediasessionextension)*