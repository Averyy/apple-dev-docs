# supportedDynamicAspectRatios

**Framework**: AVFoundation  
**Kind**: property

Indicates the supported aspect ratios for the device format.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var supportedDynamicAspectRatios: [AVCaptureDevice.AspectRatio] { get }
```

#### Discussion

An array that describes the aspect ratios that are supported for this format. If this device format does not support dynamic aspect ratio, this property returns an empty array.

## See Also

- [func videoFieldOfView(for: AVCaptureDevice.AspectRatio, geometricDistortionCorrected: Bool) -> Float](avcapturedevice/format/videofieldofview(for:geometricdistortioncorrected:).md)
  Indicates the horizontal field of view for an aspect ratio, either uncorrected or corrected for geometric distortion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/supporteddynamicaspectratios)*