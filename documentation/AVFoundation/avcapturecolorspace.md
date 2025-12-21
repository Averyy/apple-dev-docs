# AVCaptureColorSpace

**Framework**: AVFoundation  
**Kind**: enum

An enumeration of color spaces a device can support.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
enum AVCaptureColorSpace
```

#### Overview

By default, a capture session automatically enables wide-gamut capture for supported devices and capture workflows.

## Topics

### Color spaces
- [AVCaptureColorSpace.sRGB](avcapturecolorspace/srgb.md)
  The standard RGB color space.
- [AVCaptureColorSpace.P3_D65](avcapturecolorspace/p3_d65.md)
  The P3 D65 wide color space that uses Illuminant D65 as the white point.
- [AVCaptureColorSpace.HLG_BT2020](avcapturecolorspace/hlg_bt2020.md)
  The BT.2020 wide color space that uses Illuminant D65 as the white point and Hybrid Log-Gamma (HLG) as the transfer function.
- [AVCaptureColorSpace.appleLog](avcapturecolorspace/applelog.md)
  The Apple Log Color space, which uses BT2020 as the color primaries, and an Apple-defined Log curve as a transfer function.
- [AVCaptureColorSpace.appleLog2](avcapturecolorspace/applelog2.md)
  The Apple Log 2 Color space, which uses Apple Gamut as the color primaries, and an Apple defined Log curve as a transfer function. When you set this as the active color space on an [`AVCaptureDevice`](avcapturedevice.md), any [`AVCapturePhotoOutput`](avcapturephotooutput.md) or [`AVCaptureStillImageOutput`](avcapturestillimageoutput.md) connected to the same [`AVCaptureDevice`](avcapturedevice.md) is made inactive (its [`isActive`](avcaptureconnection/isactive.md) property returns `false`).
### Initializers
- [init?(rawValue: Int)](avcapturecolorspace/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var activeColorSpace: AVCaptureColorSpace](avcapturedevice/activecolorspace.md)
  The currently active color space for capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturecolorspace)*