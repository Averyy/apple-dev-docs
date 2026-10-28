# automaticallyAdjustsFaceDrivenAutoExposureEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) BOOL automaticallyAdjustsFaceDrivenAutoExposureEnabled;
```

## Discussion

The value of this property defaults to [`true`](../../Swift/true.md) for devices that support autoexposure. If your app requires explicitly setting the state of [`isFaceDrivenAutoExposureEnabled`](./isfacedrivenautoexposureenabled.md), set this value to [`false`](../../Swift/false.md).

To set this property value, you must call the device’s [`lockForConfiguration()`](./lockforconfiguration%28%29.md) method to obtain exclusive access to configure it. Otherwise, attempting to set a value raises an exception. When you finish configuring the device, call [`unlockForConfiguration()`](./unlockforconfiguration%28%29.md) to release the lock.

## See Also

### Configuring face-driven automatic exposure
- [var isFaceDrivenAutoExposureEnabled: Bool](./isfacedrivenautoexposureenabled.md)
  A Boolean value that indicates whether the device has face-driven autoexposure enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/automaticallyadjustsfacedrivenautoexposureenabled)*