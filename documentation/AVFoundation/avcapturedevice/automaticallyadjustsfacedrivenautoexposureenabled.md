# automaticallyAdjustsFaceDrivenAutoExposureEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the device automatically adjusts face-driven autoexposure.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- tvOS 17.0+

## Declaration

```swift
var automaticallyAdjustsFaceDrivenAutoExposureEnabled: Bool { get set }
```

#### Discussion

The value of this property defaults to [`true`](https://developer.apple.com/documentation/Swift/true) for devices that support autoexposure. If your app requires explicitly setting the state of [`isFaceDrivenAutoExposureEnabled`](avcapturedevice/isfacedrivenautoexposureenabled.md), set this value to [`false`](https://developer.apple.com/documentation/Swift/false).

To set this property value, you must call the device’s [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) method to obtain exclusive access to configure it. Otherwise, attempting to set a value raises an exception. When you finish configuring the device, call [`unlockForConfiguration()`](avcapturedevice/unlockforconfiguration().md) to release the lock.

## See Also

- [var isFaceDrivenAutoExposureEnabled: Bool](avcapturedevice/isfacedrivenautoexposureenabled.md)
  A Boolean value that indicates whether the device has face-driven autoexposure enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/automaticallyadjustsfacedrivenautoexposureenabled)*