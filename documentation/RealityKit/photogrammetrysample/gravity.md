# gravity

**Framework**: RealityKit  
**Kind**: property

An image’s gravity vector.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var gravity: CMAcceleration? { get set }
```

#### Discussion

Some cameras, including iPhone cameras, capture a gravity vector for each image. This vector indicates the orientation of the camera at the moment you took the picture. RealityKit uses this gravity vector to improve landmark matching with the other images in the session.

## See Also

- [let image: CVPixelBuffer](photogrammetrysample/image.md)
  The image data for this sample.
- [var metadata: [String : Any]](photogrammetrysample/metadata.md)
  An image’s EXIF metadata.
- [var depthDataMap: CVPixelBuffer?](photogrammetrysample/depthdatamap.md)
  The image’s depth data.
- [var objectMask: CVPixelBuffer?](photogrammetrysample/objectmask.md)
  The image’s object mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysample/gravity)*