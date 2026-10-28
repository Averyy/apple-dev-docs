# AVCaptureDevice.AutoFocusRangeRestriction

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants to specify the autofocus range of a capture device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
enum AutoFocusRangeRestriction
```

```c
enum AVCaptureAutoFocusRangeRestriction : NSInteger;
```

## Overview

If you expect to focus primarily on near or far objects, you can use the [`autoFocusRangeRestriction`](./autofocusrangerestriction-swift.property.md) property to provide a hint to the focusing system. This approach makes autofocus faster, more power efficient, and less error prone. A restriction prioritizes focusing at distances in the specified range, but doesn’t prevent focusing elsewhere if the device finds no focus point within that range.

## Topics

### Constants
- [AVCaptureDevice.AutoFocusRangeRestriction.none](./autofocusrangerestriction-swift.enum/none.md)
  The device attempts to focus on objects at any range.
- [AVCaptureDevice.AutoFocusRangeRestriction.near](./autofocusrangerestriction-swift.enum/near.md)
  The device primarily attempts to focus on subjects near the camera.
- [AVCaptureDevice.AutoFocusRangeRestriction.far](./autofocusrangerestriction-swift.enum/far.md)
  The device primarily attempts to focus on subjects far away from the camera.
### Initializers
- [init?(rawValue: Int)](./autofocusrangerestriction-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [var autoFocusRangeRestriction: AVCaptureDevice.AutoFocusRangeRestriction](./autofocusrangerestriction-swift.property.md)
  A value that controls the allowable range for automatic focusing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/autofocusrangerestriction-swift.enum)*