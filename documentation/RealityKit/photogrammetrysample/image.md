# image

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

Provide image data in the [`kCVPixelFormatType_32BGRA`](../../CoreVideo/kcvpixelformattype_32bgra.md) or [`kCVPixelFormatType_32ARGB`](../../CoreVideo/kcvpixelformattype_32argb.md) pixel formats.

## See Also

### Describing the sample
- [var metadata: [String : Any]](./metadata.md)
  An image’s EXIF metadata.
- [var depthDataMap: CVPixelBuffer?](./depthdatamap.md)
  The image’s depth data.
- [var gravity: CMAcceleration?](./gravity.md)
  An image’s gravity vector.
- [var objectMask: CVPixelBuffer?](./objectmask.md)
  The image’s object mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysample/image)*