# isSmoothAutoFocusSupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the device supports smooth autofocus.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isSmoothAutoFocusSupported: Bool { get }
```

#### Discussion

The smooth focusing mode is available only on compatible devices. If this property’s value is [`false`](https://developer.apple.com/documentation/swift/false), setting the value of [`isSmoothAutoFocusEnabled`](avcapturedevice/issmoothautofocusenabled.md) to [`true`](https://developer.apple.com/documentation/swift/true) raises an exception.

## See Also

- [func isFocusModeSupported(AVCaptureDevice.FocusMode) -> Bool](avcapturedevice/isfocusmodesupported(_:).md)
  Returns a Boolean value that indicates whether the device supports the specified focus mode.
- [var focusMode: AVCaptureDevice.FocusMode](avcapturedevice/focusmode-swift.property.md)
  The capture device’s focus mode.
- [AVCaptureDevice.FocusMode](avcapturedevice/focusmode-swift.enum.md)
  Constants to specify the focus mode of a capture device.
- [var isSmoothAutoFocusEnabled: Bool](avcapturedevice/issmoothautofocusenabled.md)
  A Boolean value that indicates whether smooth autofocus is in an enabled state on the device.
- [var isFaceDrivenAutoFocusEnabled: Bool](avcapturedevice/isfacedrivenautofocusenabled.md)
  A Boolean value that indicates whether the device has face-driven autofocus enabled.
- [var automaticallyAdjustsFaceDrivenAutoFocusEnabled: Bool](avcapturedevice/automaticallyadjustsfacedrivenautofocusenabled.md)
  A Boolean value that indicates whether the device automatically adjusts face-driven autofocus.
- [var isAutoFocusRangeRestrictionSupported: Bool](avcapturedevice/isautofocusrangerestrictionsupported.md)
  A Boolean value that indicates whether the device supports focus range restrictions.
- [var autoFocusRangeRestriction: AVCaptureDevice.AutoFocusRangeRestriction](avcapturedevice/autofocusrangerestriction-swift.property.md)
  A value that controls the allowable range for automatic focusing.
- [AVCaptureDevice.AutoFocusRangeRestriction](avcapturedevice/autofocusrangerestriction-swift.enum.md)
  Constants to specify the autofocus range of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/issmoothautofocussupported)*