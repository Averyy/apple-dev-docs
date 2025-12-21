# videoFieldOfView(for:geometricDistortionCorrected:)

**Framework**: AVFoundation  
**Kind**: method

Indicates the horizontal field of view for an aspect ratio, either uncorrected or corrected for geometric distortion.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func videoFieldOfView(for aspectRatio: AVCaptureDevice.AspectRatio, geometricDistortionCorrected: Bool) -> Float
```

#### Discussion

A float indicating the field of view for the corresponding [`AVCaptureDevice.AspectRatio`](avcapturedevice/aspectratio.md). Set `AVCaptureDevice/geometricDistortionCorrected` to `true` to receive the field of view corrected for geometric distortion. If this device format does not support dynamic aspect ratio, this function returns `0`.

## See Also

- [var supportedDynamicAspectRatios: [AVCaptureDevice.AspectRatio]](avcapturedevice/format/supporteddynamicaspectratios.md)
  Indicates the supported aspect ratios for the device format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videofieldofview(for:geometricdistortioncorrected:))*