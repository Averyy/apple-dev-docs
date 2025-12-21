# AVExternalSyncDevice.DiscoverySession

**Framework**: AVFoundation  
**Kind**: class

A means of discovering and monitoring connection / disconnection of external sync devices to the host.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
class DiscoverySession
```

#### Overview

[`AVExternalSyncDevice.DiscoverySession`](avexternalsyncdevice/discoverysession.md) is a singleton that lists the external sync devices connected to the host. The client is expected to key-value observe the [`devices`](avexternalsyncdevice/discoverysession/devices.md) property for changes to the external sync devices list.

## Topics

### Accessing the shared instance
- [class var shared: AVExternalSyncDevice.DiscoverySession?](avexternalsyncdevice/discoverysession/shared.md)
  The singleton instance of the external sync source device discovery session.
- [class var isSupported: Bool](avexternalsyncdevice/discoverysession/issupported.md)
  Whether external sync devices are supported by this device.
### Finding devices
- [var devices: [AVExternalSyncDevice]](avexternalsyncdevice/discoverysession/devices.md)
  An array of external sync devices connected to this host.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVExternalSyncDevice](avexternalsyncdevice.md)
  An external sync device connected to a host device that can be used to drive the timing of an internal component, such as a camera sensor.
- [protocol AVExternalSyncDeviceDelegate](avexternalsyncdevicedelegate.md)
  Defines an interface for delegates of [`AVCaptureDeviceInput`](avcapturedeviceinput.md) to respond to events that occur when connecting, calibrating, and disconnecting external sync devices.
- [enum AVExternalSyncDeviceStatus](avexternalsyncdevicestatus.md)
  Connection state of an external sync device


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/discoverysession)*