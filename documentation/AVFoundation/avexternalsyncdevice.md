# AVExternalSyncDevice

**Framework**: AVFoundation  
**Kind**: class

An external sync device connected to a host device that can be used to drive the timing of an internal component, such as a camera sensor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
class AVExternalSyncDevice
```

#### Overview

Each instance of [`AVExternalSyncDevice`](avexternalsyncdevice.md) corresponds to a physical external device that can drive an internal component, like a camera readout. You cannot create instances of [`AVExternalSyncDevice`](avexternalsyncdevice.md). Instead, you obtain an array of all currently available external sync devices using [`AVExternalSyncDevice.DiscoverySession`](avexternalsyncdevice/discoverysession.md).

## Topics

### Finding and monitoring devices
- [AVExternalSyncDevice.DiscoverySession](avexternalsyncdevice/discoverysession.md)
  A means of discovering and monitoring connection / disconnection of external sync devices to the host.
### Inspecting a device
- [var clock: CMClock?](avexternalsyncdevice/clock.md)
  A clock representing the source of time from the external sync device.
- [var productID: UInt32](avexternalsyncdevice/productid.md)
  The USB product identifier associated with the external sync device.
- [var signalCompensationDelay: CMTime](avexternalsyncdevice/signalcompensationdelay.md)
  Delay to wait before starting the frame capture.
- [var status: AVExternalSyncDeviceStatus](avexternalsyncdevice/status.md)
  The status of the externally connected device.
- [var uuid: UUID](avexternalsyncdevice/uuid.md)
  A unique identifier for an external sync device.
- [var vendorID: UInt32](avexternalsyncdevice/vendorid.md)
  The USB vendor identifier associated with the external sync device.

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

- [protocol AVExternalSyncDeviceDelegate](avexternalsyncdevicedelegate.md)
  Defines an interface for delegates of [`AVCaptureDeviceInput`](avcapturedeviceinput.md) to respond to events that occur when connecting, calibrating, and disconnecting external sync devices.
- [enum AVExternalSyncDeviceStatus](avexternalsyncdevicestatus.md)
  Connection state of an external sync device
- [AVExternalSyncDevice.DiscoverySession](avexternalsyncdevice/discoverysession.md)
  A means of discovering and monitoring connection / disconnection of external sync devices to the host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice)*