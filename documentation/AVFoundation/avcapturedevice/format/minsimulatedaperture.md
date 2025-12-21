# minSimulatedAperture

**Framework**: AVFoundation  
**Kind**: property

Minimum supported shallow depth of field simulated aperture.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var minSimulatedAperture: Float { get }
```

#### Discussion

On devices that do not support changing the simulated aperture value, this returns a value of `0`.

## See Also

- [var isCinematicVideoCaptureSupported: Bool](avcapturedevice/format/iscinematicvideocapturesupported.md)
  Indicates whether the format supports Cinematic Video capture.
- [var defaultSimulatedAperture: Float](avcapturedevice/format/defaultsimulatedaperture.md)
  Default shallow depth of field simulated aperture.
- [var maxSimulatedAperture: Float](avcapturedevice/format/maxsimulatedaperture.md)
  Maximum supported shallow depth of field simulated aperture.
- [var videoMaxZoomFactorForCinematicVideo: CGFloat](avcapturedevice/format/videomaxzoomfactorforcinematicvideo.md)
  Indicates the maximum zoom factor available for the [`videoZoomFactor`](avcapturedevice/videozoomfactor.md) property when Cinematic Video capture is enabled on the device input.
- [var videoMinZoomFactorForCinematicVideo: CGFloat](avcapturedevice/format/videominzoomfactorforcinematicvideo.md)
  Indicates the minimum zoom factor available for the [`videoZoomFactor`](avcapturedevice/videozoomfactor.md) property when Cinematic Video capture is enabled on the device input.
- [var videoFrameRateRangeForCinematicVideo: AVFrameRateRange?](avcapturedevice/format/videoframeraterangeforcinematicvideo.md)
  Indicates the minimum / maximum frame rates available when Cinematic Video capture is enabled on the device input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/minsimulatedaperture)*