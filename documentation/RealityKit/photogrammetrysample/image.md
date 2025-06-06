# image

**Framework**: RealityKit  
**Kind**: property

The image data for this sample.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
let image: CVPixelBuffer
```

#### Discussion

Provide image data in the [`kCVPixelFormatType_32BGRA`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_32BGRA) or [`kCVPixelFormatType_32ARGB`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_32ARGB) pixel formats.

## See Also

- [var metadata: [String : Any]](photogrammetrysample/metadata.md)
  An image’s EXIF metadata.
- [var depthDataMap: CVPixelBuffer?](photogrammetrysample/depthdatamap.md)
  The image’s depth data.
- [var gravity: CMAcceleration?](photogrammetrysample/gravity.md)
  An image’s gravity vector.
- [var objectMask: CVPixelBuffer?](photogrammetrysample/objectmask.md)
  The image’s object mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysample/image)*