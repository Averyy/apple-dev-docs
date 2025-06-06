# scaleFactor

**Framework**: AVFoundation  
**Kind**: property

Indicates the factor by which video buffers captured from the screen are to be scaled.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var scaleFactor: CGFloat { get set }
```

#### Discussion

By default, `AVCaptureScreenInput` captures the video buffers from the display at a scale factor of 1.0 (no scaling). Set this property to scale the buffers by a given factor; for example a 320x240 capture area with a scaleFactor of `2.0` produces video buffers at 640x480.

## See Also

- [var minFrameDuration: CMTime](avcapturescreeninput/minframeduration.md)
  The screen input’s minimum frame duration.
- [var cropRect: CGRect](avcapturescreeninput/croprect.md)
  Indicates the bounding rectangle of the screen area to be captured, in pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/scalefactor)*