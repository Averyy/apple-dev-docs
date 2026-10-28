# videoFieldOfView

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Indicates the format’s horizontal field of view in degrees.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var videoFieldOfView: Float { get }
```

```objc
@property (nonatomic, readonly) float videoFieldOfView;
```

## Discussion

Returns zero if the format’s field of view is unknown.

## See Also

### Determining field of view
- [var geometricDistortionCorrectedVideoFieldOfView: Float](./geometricdistortioncorrectedvideofieldofview.md)
  A horizontal field of view for the format after correction for geometric distortion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videofieldofview)*