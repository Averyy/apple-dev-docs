# isFaceDrivenAutoFocusEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the device has face-driven autofocus enabled.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- tvOS 17.0+

## Declaration

```swift
var isFaceDrivenAutoFocusEnabled: Bool { get set }
```

#### Discussion

Face-driven auto focus takes a subject’s face into account when adjusting auto focus. For apps that link against iOS 15.4 or later, the value of this property defaults to [`true`](https://developer.apple.com/documentation/swift/true) for devices that support auto focus.

Before setting a value for this property, perform the following:

- Obtain exclusive access to the device by calling its [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) method.
- Set the value of the device’s [`automaticallyAdjustsFaceDrivenAutoFocusEnabled`](avcapturedevice/automaticallyadjustsfacedrivenautofocusenabled.md) property to [`false`](https://developer.apple.com/documentation/swift/false).

Attempting to set a value before performing these steps results in an exception.

When you finish configuring the device, unlock it by calling its [`unlockForConfiguration()`](avcapturedevice/unlockforconfiguration().md) method.

> ❗ **Important**:  Updating the state of this property doesn’t initiate a focus change. After setting a new value, set an appropriate [`focusMode`](avcapturedevice/focusmode-swift.property.md) to apply the change.

 Updating the state of this property doesn’t initiate a focus change. After setting a new value, set an appropriate [`focusMode`](avcapturedevice/focusmode-swift.property.md) to apply the change.

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
- [var automaticallyAdjustsFaceDrivenAutoFocusEnabled: Bool](avcapturedevice/automaticallyadjustsfacedrivenautofocusenabled.md)
  A Boolean value that indicates whether the device automatically adjusts face-driven autofocus.
- [var isAutoFocusRangeRestrictionSupported: Bool](avcapturedevice/isautofocusrangerestrictionsupported.md)
  A Boolean value that indicates whether the device supports focus range restrictions.
- [var autoFocusRangeRestriction: AVCaptureDevice.AutoFocusRangeRestriction](avcapturedevice/autofocusrangerestriction-swift.property.md)
  A value that controls the allowable range for automatic focusing.
- [AVCaptureDevice.AutoFocusRangeRestriction](avcapturedevice/autofocusrangerestriction-swift.enum.md)
  Constants to specify the autofocus range of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isfacedrivenautofocusenabled)*