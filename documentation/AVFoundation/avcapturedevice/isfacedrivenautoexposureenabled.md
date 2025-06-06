# isFaceDrivenAutoExposureEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the device has face-driven autoexposure enabled.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- tvOS 17.0+

## Declaration

```swift
var isFaceDrivenAutoExposureEnabled: Bool { get set }
```

#### Discussion

Face-driven autoexposure takes a subject’s face into account when performing automatic exposure adjustments. Enabling this feature can better expose subjects with darker skin tones or those who are backlit. For apps that link against iOS 15.4 or later, the value of this property defaults to [`true`](https://developer.apple.com/documentation/swift/true) for devices that support autoexposure.

Before setting a value for this property, perform the following:

- Obtain exclusive access to the device by calling its [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) method.
- Set the value of the device’s [`automaticallyAdjustsFaceDrivenAutoExposureEnabled`](avcapturedevice/automaticallyadjustsfacedrivenautoexposureenabled.md) property to [`false`](https://developer.apple.com/documentation/swift/false).

Attempting to set a value before performing these steps results in an exception.

When you finish configuring the device, unlock it by calling its [`unlockForConfiguration()`](avcapturedevice/unlockforconfiguration().md) method.

> ❗ **Important**:  Updating the state of this property doesn’t initiate an exposure change. After setting a new value, set an appropriate [`exposureMode`](avcapturedevice/exposuremode-swift.property.md) to apply the change.

 Updating the state of this property doesn’t initiate an exposure change. After setting a new value, set an appropriate [`exposureMode`](avcapturedevice/exposuremode-swift.property.md) to apply the change.

## See Also

- [var automaticallyAdjustsFaceDrivenAutoExposureEnabled: Bool](avcapturedevice/automaticallyadjustsfacedrivenautoexposureenabled.md)
  A Boolean value that indicates whether the device automatically adjusts face-driven autoexposure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isfacedrivenautoexposureenabled)*