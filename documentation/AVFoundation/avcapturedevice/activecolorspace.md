# activeColorSpace

**Framework**: AVFoundation  
**Kind**: property

The currently active color space for capture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
var activeColorSpace: AVCaptureColorSpace { get set }
```

#### Discussion

All devices and formats support capture in the sRGB color space. Some devices and formats can also capture in the P3 color space, which includes a much wider gamut of colors than the sRGB color space. By default, a capture session automatically enables wide-gamut capture for supported devices and capture workflows—for details, see the [`automaticallyConfiguresCaptureDeviceForWideColor`](avcapturesession/automaticallyconfigurescapturedeviceforwidecolor.md) of your capture session. To instead set the color space manually, disable that [`AVCaptureSession`](avcapturesession.md) property before setting the active color space.

For best results, choose a color space before calling [`startRunning()`](avcapturesession/startrunning().md) on your capture session. Changing this property while a capture session is running requires a disruptive reconfiguration of the capture render pipeline—movie captures in progress ends immediately, unfulfilled photo requests abort, and video preview temporarily freeze.

Before changing this property, you must call the [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) method to obtain exclusive access to the capture device. Attempting to change this property without locking the device raises an exception ([`genericException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1412113-genericexception)).

## See Also

- [enum AVCaptureColorSpace](avcapturecolorspace.md)
  An enumeration of color spaces a device can support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/activecolorspace)*