# RemoteMediaSessionExtensionConfiguration

**Framework**: Now Playing  
**Kind**: class

The configuration object for a remote playback extension.

**Availability**:
- iOS 27.0+ (Beta)
- iOS App Extension 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
final class RemoteMediaSessionExtensionConfiguration<Extension> where Extension : RemoteMediaSessionExtension
```

## Mentions

- [Publishing remote media sessions](publishing-remote-media-sessions.md)

#### Overview

This class manages the lifecycle of remote sessions within your app extension. It handles XPC communication, session registration, attribute updates, and automatic observation of session state changes.

Create an instance of this class in your extension’s `configuration` property:

```swift
@main
struct MyPlaybackExtension: RemoteMediaSessionExtension {
    var configuration: RemoteMediaSessionExtensionConfiguration<Self> {
        RemoteMediaSessionExtensionConfiguration(extension: self)
    }
}
```

## Topics

### Initializers
- [init(extension: Extension)](remotemediasessionextensionconfiguration/init(extension:).md)
  Creates a new configuration with the specified extension instance.

## Relationships

### Conforms To
- [AppExtensionConfiguration](../ExtensionFoundation/AppExtensionConfiguration.md)
- [Copyable](../Swift/Copyable.md)
- [Escapable](../Swift/Escapable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Publishing remote media sessions](publishing-remote-media-sessions.md)
  Show media from an external device on the Lock Screen and Control Center.
- [protocol RemoteMediaSessionRepresentable](remotemediasessionrepresentable.md)
  A session that plays remotely, potentially across multiple devices.
- [class RemoteMediaSession](remotemediasession.md)
  A session that manages remote media playback across devices.
- [protocol RemoteMediaSessionExtension](remotemediasessionextension.md)
  An app extension that provides remote media sessions.
- [protocol RemoteMediaSessionAttributes](remotemediasessionattributes.md)
  A type that represents attributes for remote sessions.
- [enum RemoteMediaSessionError](remotemediasessionerror.md)
  Errors that can occur during remote session operations.
- [struct MediaDevice](mediadevice.md)
  A device that plays media in a remote session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/remotemediasessionextensionconfiguration)*