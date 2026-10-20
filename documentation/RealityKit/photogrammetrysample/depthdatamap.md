# depthDataMap

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The image’s depth data.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var depthDataMap: CVPixelBuffer? { get set }
```

#### Discussion

Some cameras, including iPhone cameras, capture depth data in addition to image data. Providing this data can help [`PhotogrammetrySession`](../photogrammetrysession.md) determine the real-world scale of the photographed object and result in a correctly sized 3D object for placement in an AR scene. This property is read-only.

Depth data can be in either [`kCVPixelFormatType_DisparityFloat32`](../../CoreVideo/kcvpixelformattype_disparityfloat32.md) or [`kCVPixelFormatType_DepthFloat32`](../../CoreVideo/kcvpixelformattype_depthfloat32.md) format.

## See Also

### Describing the sample
- [let image: CVPixelBuffer](./image.md)
  The image data for this sample.
- [var metadata: [String : Any]](./metadata.md)
  An image’s EXIF metadata.
- [var gravity: CMAcceleration?](./gravity.md)
  An image’s gravity vector.
- [var objectMask: CVPixelBuffer?](./objectmask.md)
  The image’s object mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysample/depthdatamap)*