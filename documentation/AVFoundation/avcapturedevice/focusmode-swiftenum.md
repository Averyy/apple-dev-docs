# AVCaptureDevice.FocusMode

**Framework**: AVFoundation  
**Kind**: enum

Constants to specify the focus mode of a capture device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
enum FocusMode
```

## Topics

### Focus Modes
- [AVCaptureDevice.FocusMode.locked](avcapturedevice/focusmode-swift.enum/locked.md)
  A mode that locks device focus.
- [AVCaptureDevice.FocusMode.autoFocus](avcapturedevice/focusmode-swift.enum/autofocus.md)
  A mode that automatically adjusts the focus one time, and then locks focus.
- [AVCaptureDevice.FocusMode.continuousAutoFocus](avcapturedevice/focusmode-swift.enum/continuousautofocus.md)
  A mode that continuously monitors focus and autofocuses when necessary.
### Initializers
- [init?(rawValue: Int)](avcapturedevice/focusmode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func isFocusModeSupported(AVCaptureDevice.FocusMode) -> Bool](avcapturedevice/isfocusmodesupported(_:).md)
  Returns a Boolean value that indicates whether the device supports the specified focus mode.
- [var focusMode: AVCaptureDevice.FocusMode](avcapturedevice/focusmode-swift.property.md)
  The capture device’s focus mode.
- [var isSmoothAutoFocusSupported: Bool](avcapturedevice/issmoothautofocussupported.md)
  A Boolean value that indicates whether the device supports smooth autofocus.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/focusmode-swift.enum)*