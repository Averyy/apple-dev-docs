# automaticallyConfiguresCaptureDeviceForWideColor

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that specifies whether the session should automatically use wide-gamut color where available.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var automaticallyConfiguresCaptureDeviceForWideColor: Bool { get set }
```

#### Discussion

All devices and formats support capture in the sRGB color space. Some devices and formats can also capture in the P3 color space, which includes a much wider gamut of colors. Wide-gamut capture is appropriate for only certain capture workflows, so this property controls automatic configuration for those workflows.

When this property is [`true`](https://developer.apple.com/documentation/Swift/true) (the default), and your session configuration is appropriate for wide-gamut capture:

- If you use a session preset other than [`inputPriority`](avcapturesession/preset/inputpriority.md), the session automatically sets the device’s [`activeFormat`](avcapturedevice/activeformat.md) property to one that supports wide-gamut capture, and sets the device’s [`activeColorSpace`](avcapturedevice/activecolorspace.md) property to a wide-gamut color space.
- If you manually choose a capture format (thereby setting the session to input priority), the session automatically sets the device’s [`activeColorSpace`](avcapturedevice/activecolorspace.md) property to a wide-gamut color space only if your chosen format supports wide-gamut capture.

For information about which devices and session configurations automatically enable wide-gamut capture, see Wide-Gamut Capture in [`iOS Device Compatibility Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DeviceInformation/Reference/iOSDeviceCompatibility/Introduction/Introduction.html#//apple_ref/doc/uid/TP40013599).

> **Note**:  When this property is [`true`](https://developer.apple.com/documentation/Swift/true), and your session configuration isn’t appropriate for wide-gamut capture, session presets other than [`inputPriority`](avcapturesession/preset/inputpriority.md) may choose a capture format that doesn’t support wide-gamut capture.

Set this property to [`false`](https://developer.apple.com/documentation/Swift/false) if you want to directly change the value of the capture device’s [`activeColorSpace`](avcapturedevice/activecolorspace.md) property (regardless of whether you configure your device with a session preset or by directly setting a capture format).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/automaticallyconfigurescapturedeviceforwidecolor)*