# intrinsics

**Framework**: ARKit  
**Kind**: property

A matrix that converts between the 2D camera plane and 3D world coordinate space.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var intrinsics: simd_float3x3 { get }
```

#### Discussion

The intrinsic matrix (commonly represented in equations as `K`) is based on physical characteristics of the device camera and a pinhole camera model. You can use the matrix to transform 3D coordinates to 2D coordinates on an image plane.

![None](https://docs-assets.developer.apple.com/published/c60173c427c21f36cc89581392cdf0e8/media-2902622%402x.png)

The values `fx` and `fy` are the pixel focal length, and are identical for square pixels. The values `ox` and `oy` are the offsets of the principal point from the top-left corner of the image frame. All values are expressed in pixels.

## See Also

- [var imageResolution: CGSize](arcamera/imageresolution.md)
  The width and height, in pixels, of the captured camera image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/intrinsics)*