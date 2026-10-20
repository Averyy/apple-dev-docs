# automaticallyAdjustsFaceDrivenAutoFocusEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the device automatically adjusts face-driven autofocus.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- tvOS 17.0+

## Declaration

```swift
var automaticallyAdjustsFaceDrivenAutoFocusEnabled: Bool { get set }
```

```objc
@property (nonatomic) BOOL automaticallyAdjustsFaceDrivenAutoFocusEnabled;
```

#### Discussion

The value of this property defaults to [`true`](../../Swift/true.md) for devices that support auto focus. If your app requires explicitly setting the state of [`isFaceDrivenAutoFocusEnabled`](./isfacedrivenautofocusenabled.md), set this value to [`false`](../../Swift/false.md).

To set this property value, you must call the device’s [`lockForConfiguration()`](./lockforconfiguration%28%29.md) method to obtain exclusive access to configure it. Otherwise, attempting to set a value raises an exception. When you finish configuring the device, call [`unlockForConfiguration()`](./unlockforconfiguration%28%29.md) to release the lock.

## See Also

### Configuring automatic focus
- [func isFocusModeSupported(AVCaptureDevice.FocusMode) -> Bool](./isfocusmodesupported%28_%29.md)
  Returns a Boolean value that indicates whether the device supports the specified focus mode.
- [var focusMode: AVCaptureDevice.FocusMode](./focusmode-swift.property.md)
  The capture device’s focus mode.
- [AVCaptureDevice.FocusMode](./focusmode-swift.enum.md)
  Constants to specify the focus mode of a capture device.
- [var isSmoothAutoFocusSupported: Bool](./issmoothautofocussupported.md)
  A Boolean value that indicates whether the device supports smooth autofocus.
- [var isSmoothAutoFocusEnabled: Bool](./issmoothautofocusenabled.md)
  A Boolean value that indicates whether smooth autofocus is in an enabled state on the device.
- [var isFaceDrivenAutoFocusEnabled: Bool](./isfacedrivenautofocusenabled.md)
  A Boolean value that indicates whether the device has face-driven autofocus enabled.
- [var isAutoFocusRangeRestrictionSupported: Bool](./isautofocusrangerestrictionsupported.md)
  A Boolean value that indicates whether the device supports focus range restrictions.
- [var autoFocusRangeRestriction: AVCaptureDevice.AutoFocusRangeRestriction](./autofocusrangerestriction-swift.property.md)
  A value that controls the allowable range for automatic focusing.
- [AVCaptureDevice.AutoFocusRangeRestriction](./autofocusrangerestriction-swift.enum.md)
  Constants to specify the autofocus range of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/automaticallyadjustsfacedrivenautofocusenabled)*