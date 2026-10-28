# isFaceDrivenAutoFocusEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, getter=isFaceDrivenAutoFocusEnabled) BOOL faceDrivenAutoFocusEnabled;
```

## Discussion

Face-driven auto focus takes a subject’s face into account when adjusting auto focus. For apps that link against iOS 15.4 or later, the value of this property defaults to [`true`](../../Swift/true.md) for devices that support auto focus.

Before setting a value for this property, perform the following:

- Obtain exclusive access to the device by calling its [`lockForConfiguration()`](./lockforconfiguration%28%29.md) method.
- Set the value of the device’s [`automaticallyAdjustsFaceDrivenAutoFocusEnabled`](./automaticallyadjustsfacedrivenautofocusenabled.md) property to [`false`](../../Swift/false.md).

Attempting to set a value before performing these steps results in an exception.

When you finish configuring the device, unlock it by calling its [`unlockForConfiguration()`](./unlockforconfiguration%28%29.md) method.

> ❗ **Important**:  Updating the state of this property doesn’t initiate a focus change. After setting a new value, set an appropriate [`focusMode`](./focusmode-swift.property.md) to apply the change.

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
- [var automaticallyAdjustsFaceDrivenAutoFocusEnabled: Bool](./automaticallyadjustsfacedrivenautofocusenabled.md)
  A Boolean value that indicates whether the device automatically adjusts face-driven autofocus.
- [var isAutoFocusRangeRestrictionSupported: Bool](./isautofocusrangerestrictionsupported.md)
  A Boolean value that indicates whether the device supports focus range restrictions.
- [var autoFocusRangeRestriction: AVCaptureDevice.AutoFocusRangeRestriction](./autofocusrangerestriction-swift.property.md)
  A value that controls the allowable range for automatic focusing.
- [AVCaptureDevice.AutoFocusRangeRestriction](./autofocusrangerestriction-swift.enum.md)
  Constants to specify the autofocus range of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isfacedrivenautofocusenabled)*