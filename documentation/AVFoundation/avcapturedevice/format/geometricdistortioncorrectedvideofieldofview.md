# geometricDistortionCorrectedVideoFieldOfView

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) float geometricDistortionCorrectedVideoFieldOfView;
```

## Discussion

If the capture device doesn’t support geometric distortion correction (GDC), the value of this property is equal to the value of [`videoFieldOfView`](./videofieldofview.md).

## See Also

### Determining field of view
- [var videoFieldOfView: Float](./videofieldofview.md)
  Indicates the format’s horizontal field of view in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/geometricdistortioncorrectedvideofieldofview)*