# isExposureModeSupported(_:)

**Framework**: AVFoundation  
**Kind**: method

Returns a Boolean value that indicates whether a device supports the specified exposure mode.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
func isExposureModeSupported(_ exposureMode: AVCaptureDevice.ExposureMode) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `exposureMode` is supported; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `exposureMode`: An exposure mode to query.

## See Also

- [var exposureMode: AVCaptureDevice.ExposureMode](avcapturedevice/exposuremode-swift.property.md)
  The exposure mode for the device.
- [AVCaptureDevice.ExposureMode](avcapturedevice/exposuremode-swift.enum.md)
  Constants that specify the exposure mode of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isexposuremodesupported(_:))*