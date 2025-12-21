# AVExternalSyncDeviceStatus.ready

**Framework**: AVFoundation  
**Kind**: case

Indicates that a device supporting external sync is connected, but calibration has not started.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
case ready
```

## See Also

- [AVExternalSyncDeviceStatus.activeSync](avexternalsyncdevicestatus/activesync.md)
  Indicates that the [`AVExternalSyncDevice`](avexternalsyncdevice.md) object is running and that the clock property on [`AVExternalSyncDevice`](avexternalsyncdevice.md) is calibrated to the external sync signal.
- [AVExternalSyncDeviceStatus.calibrating](avexternalsyncdevicestatus/calibrating.md)
  Indicates that the external sync signal is connected and that the AVExternalSyncDevice object is calibrating to follow.
- [AVExternalSyncDeviceStatus.freeRunSync](avexternalsyncdevicestatus/freerunsync.md)
  Indicates that the AVExternalSyncDevice was calibrated to follow the external sync, but the sync signal has been lost. The camera will continue to match the last signal it received, but sync is not guaranteed.
- [AVExternalSyncDeviceStatus.unavailable](avexternalsyncdevicestatus/unavailable.md)
  Indicates that external sync signal is not connected, or has transitioned to a state that is not recoverable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalsyncdevicestatus/ready)*