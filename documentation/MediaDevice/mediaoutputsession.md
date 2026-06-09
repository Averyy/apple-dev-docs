# MediaOutputSession

**Framework**: Media Device  
**Kind**: class

Represents a media output session for playing content on a remote device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final class MediaOutputSession
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

#### Overview

Instances of this class are provided by the system when a [`MediaDeviceExtension`](mediadeviceextension.md) receives activation or playback requests. Use the session to associate device activations, playback events, and data communication with a specific media output context.

## Topics

### Instance Properties
- [let id: String](mediaoutputsession/id.md)
  A unique identifier for this session.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class MediaDeviceRoutingManager](mediadeviceroutingmanager.md)
  An object used by a [`MediaDeviceExtension`](mediadeviceextension.md) to report device discovery, state changes, and playback events back to the system.
- [protocol RealtimeSampleHandling](realtimesamplehandling.md)
  A protocol that extends a media device extension to support realtime sample delivery.
- [struct MediaDeviceError](mediadeviceerror.md)
  An error returned by MediaDeviceExtension operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediaoutputsession)*