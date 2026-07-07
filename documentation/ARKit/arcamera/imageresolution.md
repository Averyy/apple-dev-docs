# imageResolution

**Framework**: ARKit  
**Kind**: property

The width and height, in pixels, of the captured camera image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
var imageResolution: CGSize { get }
```

#### Discussion

This size describes the image in the [`capturedImage`](arframe/capturedimage.md) buffer, which contains image data in the camera device’s native sensor orientation. To convert image coordinates to match a specific display orientation of that image, use the `ARCamera/viewMatrix(for:)` or `ARCamera/projectPoint(_:orientation:viewportSize:)` method.

## See Also

- [var intrinsics: simd_float3x3](arcamera/intrinsics.md)
  A matrix that converts between the 2D camera plane and 3D world coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/imageresolution)*