# AVCaptureDevice.LensStabilizationStatus.outOfRange

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

Lens stabilization was enabled for the photo capture, but device motion or capture duration exceeded the stabilization module’s correction limits.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
case outOfRange
```

```c
AVCaptureLensStabilizationStatusOutOfRange
```

## See Also

### Lens stabilization values
- [AVCaptureDevice.LensStabilizationStatus.unsupported](./unsupported.md)
  Lens stabilization isn’t available on the device or device configuration that captured this photo.
- [AVCaptureDevice.LensStabilizationStatus.off](./off.md)
  Lens stabilization isn’t specified for this photo capture.
- [AVCaptureDevice.LensStabilizationStatus.active](./active.md)
  Lens stabilization was active for the full duration of the photo capture.
- [AVCaptureDevice.LensStabilizationStatus.unavailable](./unavailable.md)
  Lens stabilization was temporarily unavailable during the photo capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/lensstabilizationstatus/outofrange)*