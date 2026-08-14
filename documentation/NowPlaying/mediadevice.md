# MediaDevice

**Framework**: Now Playing  
**Kind**: struct

A device that plays media in a remote session.

**Availability**:
- iOS 27.0+ (Beta)
- iOS App Extension 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct MediaDevice
```

## Mentions

- [Publishing remote media sessions](publishing-remote-media-sessions.md)

#### Overview

Use this type to represent playback devices in your remote sessions.

The system displays device information including the name, type, and volume level in the Now Playing interface.

For more information, see [`Publishing remote media sessions`](publishing-remote-media-sessions.md)

## Topics

### Structures
- [MediaDevice.Capability](mediadevice/capability.md)
  The control capabilities of a device.
### Initializers
- [init(id: String, name: String, type: MediaDevice.DeviceType, capabilities: [MediaDevice.Capability])](mediadevice/init(id:name:type:capabilities:).md)
  Creates a media device with the specified identifier, name, type, and capabilities.
### Instance Properties
- [let capabilities: [MediaDevice.Capability]](mediadevice/capabilities.md)
  The control capabilities this device supports.
- [let id: String](mediadevice/id.md)
  The unique identifier for this device.
- [let name: String](mediadevice/name.md)
  The human-readable name of the device.
- [let type: MediaDevice.DeviceType](mediadevice/type.md)
  The type of device.
### Enumerations
- [MediaDevice.DeviceType](mediadevice/devicetype.md)
  The type of device that plays media.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

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
- [protocol RemoteMediaSessionAttributes](remotemediasessionattributes.md)
  A type that represents attributes for remote sessions.
- [enum RemoteMediaSessionError](remotemediasessionerror.md)
  Errors that can occur during remote session operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediadevice)*