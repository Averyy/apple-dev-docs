# autoFocusRangeRestriction

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A value that controls the allowable range for automatic focusing.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var autoFocusRangeRestriction: AVCaptureDevice.AutoFocusRangeRestriction { get set }
```

```objc
@property (nonatomic) AVCaptureAutoFocusRangeRestriction autoFocusRangeRestriction;
```

#### Discussion

By default, a device capable of hardware focusing attempts to focus on objects at any distance. If you expect to focus primarily on near or far objects, set a range restriction to increase the speed and reduce the power consumption of automatic focusing, and to reduce the chance of focusing ambiguities.

Before changing the value of this property, you must call [`lockForConfiguration()`](./lockforconfiguration%28%29.md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [`unlockForConfiguration()`](./unlockforconfiguration%28%29.md) to release the lock and allow other devices to configure the settings.

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
- [var automaticallyAdjustsFaceDrivenAutoFocusEnabled: Bool](./automaticallyadjustsfacedrivenautofocusenabled.md)
  A Boolean value that indicates whether the device automatically adjusts face-driven autofocus.
- [var isAutoFocusRangeRestrictionSupported: Bool](./isautofocusrangerestrictionsupported.md)
  A Boolean value that indicates whether the device supports focus range restrictions.
- [AVCaptureDevice.AutoFocusRangeRestriction](./autofocusrangerestriction-swift.enum.md)
  Constants to specify the autofocus range of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/autofocusrangerestriction-swift.property)*