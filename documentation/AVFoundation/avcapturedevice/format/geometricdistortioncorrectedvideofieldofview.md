# geometricDistortionCorrectedVideoFieldOfView

**Framework**: AVFoundation  
**Kind**: property

A horizontal field of view for the format after correction for geometric distortion.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var geometricDistortionCorrectedVideoFieldOfView: Float { get }
```

#### Discussion

If the capture device doesn’t support geometric distortion correction (GDC), the value of this property is equal to the value of [`videoFieldOfView`](avcapturedevice/format/videofieldofview.md).

## See Also

- [var videoFieldOfView: Float](avcapturedevice/format/videofieldofview.md)
  Indicates the format’s horizontal field of view in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/geometricdistortioncorrectedvideofieldofview)*