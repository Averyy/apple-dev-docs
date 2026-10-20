# objectMask

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The image’s object mask.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var objectMask: CVPixelBuffer? { get set }
```

#### Discussion

When a photograph of an object includes surrounding objects, such as plants, buildings, or people in an outdoor space, you can create an object mask to exclude the portions of the image that don’t contain the object. Masking extraneous image data reduces the number of landmarks RealityKit attempts to match, speeds up the object-creation process, and produces a more accurate 3D model.

Provide the object mask in [`kCVPixelFormatType_OneComponent8`](../../CoreVideo/kcvpixelformattype_onecomponent8.md) format and with the same height and width as [`image`](./image.md). RealityKit ignores any pixel in [`image`](./image.md) when the corresponding pixel in [`objectMask`](./objectmask.md) has a value of `0.0` (black) unless [`isObjectMaskingEnabled`](../photogrammetrysession/configuration-swift.struct/isobjectmaskingenabled.md) is set to `False` in the session’s configuration.

## See Also

### Describing the sample
- [let image: CVPixelBuffer](./image.md)
  The image data for this sample.
- [var metadata: [String : Any]](./metadata.md)
  An image’s EXIF metadata.
- [var depthDataMap: CVPixelBuffer?](./depthdatamap.md)
  The image’s depth data.
- [var gravity: CMAcceleration?](./gravity.md)
  An image’s gravity vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysample/objectmask)*