# minSimulatedAperture

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) float minSimulatedAperture;
```

## Discussion

On devices that do not support changing the simulated aperture value, this returns a value of `0`.

## See Also

### Determining Cinematic video support
- [var isCinematicVideoCaptureSupported: Bool](./iscinematicvideocapturesupported.md)
  Indicates whether the format supports Cinematic Video capture.
- [var defaultSimulatedAperture: Float](./defaultsimulatedaperture.md)
  Default shallow depth of field simulated aperture.
- [var maxSimulatedAperture: Float](./maxsimulatedaperture.md)
  Maximum supported shallow depth of field simulated aperture.
- [var videoMaxZoomFactorForCinematicVideo: CGFloat](./videomaxzoomfactorforcinematicvideo.md)
  Indicates the maximum zoom factor available for the [`videoZoomFactor`](../videozoomfactor.md) property when Cinematic Video capture is enabled on the device input.
- [var videoMinZoomFactorForCinematicVideo: CGFloat](./videominzoomfactorforcinematicvideo.md)
  Indicates the minimum zoom factor available for the [`videoZoomFactor`](../videozoomfactor.md) property when Cinematic Video capture is enabled on the device input.
- [var videoFrameRateRangeForCinematicVideo: AVFrameRateRange?](./videoframeraterangeforcinematicvideo.md)
  Indicates the minimum / maximum frame rates available when Cinematic Video capture is enabled on the device input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/minsimulatedaperture)*