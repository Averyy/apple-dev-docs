# videoMaxZoomFactorForCinematicVideo

**Framework**: AVFoundation  
**Kind**: property

Indicates the maximum zoom factor available for the [`videoZoomFactor`](avcapturedevice/videozoomfactor.md) property when Cinematic Video capture is enabled on the device input.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var videoMaxZoomFactorForCinematicVideo: CGFloat { get }
```

#### Discussion

Devices support a limited zoom range when Cinematic Video capture is active. If this device format does not support Cinematic Video capture, this property returns `1.0`.

## See Also

- [var isCinematicVideoCaptureSupported: Bool](avcapturedevice/format/iscinematicvideocapturesupported.md)
  Indicates whether the format supports Cinematic Video capture.
- [var defaultSimulatedAperture: Float](avcapturedevice/format/defaultsimulatedaperture.md)
  Default shallow depth of field simulated aperture.
- [var minSimulatedAperture: Float](avcapturedevice/format/minsimulatedaperture.md)
  Minimum supported shallow depth of field simulated aperture.
- [var maxSimulatedAperture: Float](avcapturedevice/format/maxsimulatedaperture.md)
  Maximum supported shallow depth of field simulated aperture.
- [var videoMinZoomFactorForCinematicVideo: CGFloat](avcapturedevice/format/videominzoomfactorforcinematicvideo.md)
  Indicates the minimum zoom factor available for the [`videoZoomFactor`](avcapturedevice/videozoomfactor.md) property when Cinematic Video capture is enabled on the device input.
- [var videoFrameRateRangeForCinematicVideo: AVFrameRateRange?](avcapturedevice/format/videoframeraterangeforcinematicvideo.md)
  Indicates the minimum / maximum frame rates available when Cinematic Video capture is enabled on the device input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videomaxzoomfactorforcinematicvideo)*