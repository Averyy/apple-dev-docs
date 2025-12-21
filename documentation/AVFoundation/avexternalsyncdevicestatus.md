# AVExternalSyncDeviceStatus

**Framework**: AVFoundation  
**Kind**: enum

Connection state of an external sync device

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
enum AVExternalSyncDeviceStatus
```

## Topics

### Status values
- [AVExternalSyncDeviceStatus.activeSync](avexternalsyncdevicestatus/activesync.md)
  Indicates that the [`AVExternalSyncDevice`](avexternalsyncdevice.md) object is running and that the clock property on [`AVExternalSyncDevice`](avexternalsyncdevice.md) is calibrated to the external sync signal.
- [AVExternalSyncDeviceStatus.calibrating](avexternalsyncdevicestatus/calibrating.md)
  Indicates that the external sync signal is connected and that the AVExternalSyncDevice object is calibrating to follow.
- [AVExternalSyncDeviceStatus.freeRunSync](avexternalsyncdevicestatus/freerunsync.md)
  Indicates that the AVExternalSyncDevice was calibrated to follow the external sync, but the sync signal has been lost. The camera will continue to match the last signal it received, but sync is not guaranteed.
- [AVExternalSyncDeviceStatus.ready](avexternalsyncdevicestatus/ready.md)
  Indicates that a device supporting external sync is connected, but calibration has not started.
- [AVExternalSyncDeviceStatus.unavailable](avexternalsyncdevicestatus/unavailable.md)
  Indicates that external sync signal is not connected, or has transitioned to a state that is not recoverable.
### Initializers
- [init?(rawValue: Int)](avexternalsyncdevicestatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVExternalSyncDevice](avexternalsyncdevice.md)
  An external sync device connected to a host device that can be used to drive the timing of an internal component, such as a camera sensor.
- [protocol AVExternalSyncDeviceDelegate](avexternalsyncdevicedelegate.md)
  Defines an interface for delegates of [`AVCaptureDeviceInput`](avcapturedeviceinput.md) to respond to events that occur when connecting, calibrating, and disconnecting external sync devices.
- [AVExternalSyncDevice.DiscoverySession](avexternalsyncdevice/discoverysession.md)
  A means of discovering and monitoring connection / disconnection of external sync devices to the host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalsyncdevicestatus)*