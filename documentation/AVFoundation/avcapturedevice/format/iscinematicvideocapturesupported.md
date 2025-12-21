# isCinematicVideoCaptureSupported

**Framework**: AVFoundation  
**Kind**: property

Indicates whether the format supports Cinematic Video capture.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var isCinematicVideoCaptureSupported: Bool { get }
```

#### Discussion

This property returns `true` if the format supports Cinematic Video that produces a controllable, simulated depth of field and adds beautiful focus transitions for a cinema-grade look.

## See Also

- [var defaultSimulatedAperture: Float](avcapturedevice/format/defaultsimulatedaperture.md)
  Default shallow depth of field simulated aperture.
- [var minSimulatedAperture: Float](avcapturedevice/format/minsimulatedaperture.md)
  Minimum supported shallow depth of field simulated aperture.
- [var maxSimulatedAperture: Float](avcapturedevice/format/maxsimulatedaperture.md)
  Maximum supported shallow depth of field simulated aperture.
- [var videoMaxZoomFactorForCinematicVideo: CGFloat](avcapturedevice/format/videomaxzoomfactorforcinematicvideo.md)
  Indicates the maximum zoom factor available for the [`videoZoomFactor`](avcapturedevice/videozoomfactor.md) property when Cinematic Video capture is enabled on the device input.
- [var videoMinZoomFactorForCinematicVideo: CGFloat](avcapturedevice/format/videominzoomfactorforcinematicvideo.md)
  Indicates the minimum zoom factor available for the [`videoZoomFactor`](avcapturedevice/videozoomfactor.md) property when Cinematic Video capture is enabled on the device input.
- [var videoFrameRateRangeForCinematicVideo: AVFrameRateRange?](avcapturedevice/format/videoframeraterangeforcinematicvideo.md)
  Indicates the minimum / maximum frame rates available when Cinematic Video capture is enabled on the device input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/iscinematicvideocapturesupported)*