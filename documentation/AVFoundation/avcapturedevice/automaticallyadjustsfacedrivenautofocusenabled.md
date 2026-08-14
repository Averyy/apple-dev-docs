# automaticallyAdjustsFaceDrivenAutoFocusEnabled

**Framework**: AVFoundation  
**Kind**: property

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

#### Discussion

The value of this property defaults to [`true`](https://developer.apple.com/documentation/swift/true) for devices that support auto focus. If your app requires explicitly setting the state of [`isFaceDrivenAutoFocusEnabled`](avcapturedevice/isfacedrivenautofocusenabled.md), set this value to [`false`](https://developer.apple.com/documentation/swift/false).

To set this property value, you must call the device’s [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) method to obtain exclusive access to configure it. Otherwise, attempting to set a value raises an exception. When you finish configuring the device, call [`unlockForConfiguration()`](avcapturedevice/unlockforconfiguration().md) to release the lock.

## See Also

- [func isFocusModeSupported(AVCaptureDevice.FocusMode) -> Bool](avcapturedevice/isfocusmodesupported(_:).md)
  Returns a Boolean value that indicates whether the device supports the specified focus mode.
- [var focusMode: AVCaptureDevice.FocusMode](avcapturedevice/focusmode-swift.property.md)
  The capture device’s focus mode.
- [AVCaptureDevice.FocusMode](avcapturedevice/focusmode-swift.enum.md)
  Constants to specify the focus mode of a capture device.
- [var isSmoothAutoFocusSupported: Bool](avcapturedevice/issmoothautofocussupported.md)
  A Boolean value that indicates whether the device supports smooth autofocus.
- [var isSmoothAutoFocusEnabled: Bool](avcapturedevice/issmoothautofocusenabled.md)
  A Boolean value that indicates whether smooth autofocus is in an enabled state on the device.
- [var isFaceDrivenAutoFocusEnabled: Bool](avcapturedevice/isfacedrivenautofocusenabled.md)
  A Boolean value that indicates whether the device has face-driven autofocus enabled.
- [var isAutoFocusRangeRestrictionSupported: Bool](avcapturedevice/isautofocusrangerestrictionsupported.md)
  A Boolean value that indicates whether the device supports focus range restrictions.
- [var autoFocusRangeRestriction: AVCaptureDevice.AutoFocusRangeRestriction](avcapturedevice/autofocusrangerestriction-swift.property.md)
  A value that controls the allowable range for automatic focusing.
- [AVCaptureDevice.AutoFocusRangeRestriction](avcapturedevice/autofocusrangerestriction-swift.enum.md)
  Constants to specify the autofocus range of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/automaticallyadjustsfacedrivenautofocusenabled)*