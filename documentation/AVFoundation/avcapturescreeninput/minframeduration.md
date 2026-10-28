# minFrameDuration

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The screen input’s minimum frame duration.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var minFrameDuration: CMTime { get set }
```

```objc
@property (nonatomic) CMTime minFrameDuration;
```

## Discussion

The `minFrameDuration` is the reciprocal of its maximum frame rate.

You use this property to request a maximum frame rate at which the input produces video frames. The requested rate may not be achievable due to overall bandwidth, so actual frame rates may be lower.

## See Also

### Setting video capture options
- [var cropRect: CGRect](./croprect.md)
  Indicates the bounding rectangle of the screen area to be captured, in pixels.
- [var scaleFactor: CGFloat](./scalefactor.md)
  Indicates the factor by which video buffers captured from the screen are to be scaled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/minframeduration)*