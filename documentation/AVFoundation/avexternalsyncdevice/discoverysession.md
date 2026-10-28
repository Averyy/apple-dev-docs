# AVExternalSyncDevice.DiscoverySession

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVExternalSyncDeviceDiscoverySession : NSObject
```

## Overview

[`AVExternalSyncDevice.DiscoverySession`](./discoverysession.md) is a singleton that lists the external sync devices connected to the host. The client is expected to key-value observe the [`devices`](./discoverysession/devices.md) property for changes to the external sync devices list.

## Topics

### Accessing the shared instance
- [class var shared: AVExternalSyncDevice.DiscoverySession?](./discoverysession/shared.md)
  The singleton instance of the external sync source device discovery session.
- [class var isSupported: Bool](./discoverysession/issupported.md)
  Whether external sync devices are supported by this device.
### Finding devices
- [var devices: [AVExternalSyncDevice]](./discoverysession/devices.md)
  An array of external sync devices connected to this host.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### External synchronization
- [class AVExternalSyncDevice](../avexternalsyncdevice.md)
  An external sync device connected to a host device that can be used to drive the timing of an internal component, such as a camera sensor.
- [protocol AVExternalSyncDeviceDelegate](../avexternalsyncdevicedelegate.md)
  Defines an interface for delegates of [`AVCaptureDeviceInput`](../avcapturedeviceinput.md) to respond to events that occur when connecting, calibrating, and disconnecting external sync devices.
- [enum AVExternalSyncDeviceStatus](../avexternalsyncdevicestatus.md)
  Connection state of an external sync device


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/discoverysession)*