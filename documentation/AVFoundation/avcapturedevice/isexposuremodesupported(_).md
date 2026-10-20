# isExposureModeSupported(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) isExposureModeSupported:(AVCaptureExposureMode) exposureMode;
```

#### Return Value

[`true`](../../Swift/true.md) if `exposureMode` is supported; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `exposureMode`: An exposure mode to query.

## See Also

### Managing the exposure mode
- [var exposureMode: AVCaptureDevice.ExposureMode](./exposuremode-swift.property.md)
  The exposure mode for the device.
- [AVCaptureDevice.ExposureMode](./exposuremode-swift.enum.md)
  Constants that specify the exposure mode of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isexposuremodesupported(_:))*