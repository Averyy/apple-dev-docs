# videoMaxScaleAndCropFactor

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The connection’s maximum video scale and crop factor.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var videoMaxScaleAndCropFactor: CGFloat { get }
```

```objc
@property (nonatomic, readonly) CGFloat videoMaxScaleAndCropFactor;
```

#### Discussion

The value defines the largest value you can set the [`videoScaleAndCropFactor`](./videoscaleandcropfactor.md) property to, which only applies to a video connection.

## See Also

### Scaling a video
- [var videoScaleAndCropFactor: CGFloat](./videoscaleandcropfactor.md)
  The current scale and crop factor the video output uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/videomaxscaleandcropfactor)*