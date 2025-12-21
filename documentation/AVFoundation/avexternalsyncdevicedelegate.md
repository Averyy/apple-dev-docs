# AVExternalSyncDeviceDelegate

**Framework**: AVFoundation  
**Kind**: protocol

Defines an interface for delegates of [`AVCaptureDeviceInput`](avcapturedeviceinput.md) to respond to events that occur when connecting, calibrating, and disconnecting external sync devices.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
protocol AVExternalSyncDeviceDelegate : NSObjectProtocol
```

## Topics

### Responding to device events
- [func externalSyncDevice(AVExternalSyncDevice, failedWithError: (any Error)?)](avexternalsyncdevicedelegate/externalsyncdevice(_:failedwitherror:).md)
- [func externalSyncDeviceStatusDidChange(AVExternalSyncDevice)](avexternalsyncdevicedelegate/externalsyncdevicestatusdidchange(_:).md)
  Informs your delegate when the external sync device status has changed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVExternalSyncDevice](avexternalsyncdevice.md)
  An external sync device connected to a host device that can be used to drive the timing of an internal component, such as a camera sensor.
- [enum AVExternalSyncDeviceStatus](avexternalsyncdevicestatus.md)
  Connection state of an external sync device
- [AVExternalSyncDevice.DiscoverySession](avexternalsyncdevice/discoverysession.md)
  A means of discovering and monitoring connection / disconnection of external sync devices to the host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalsyncdevicedelegate)*