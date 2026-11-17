# intrinsics

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A matrix that converts between the 2D camera plane and 3D world coordinate space.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
var intrinsics: simd_float3x3 { get }
```

```objc
@property (nonatomic, readonly) simd_float3x3 intrinsics;
```

## Discussion

The intrinsic matrix (commonly represented in equations as `K`) is based on physical characteristics of the device camera and a pinhole camera model. You can use the matrix to transform 3D coordinates to 2D coordinates on an image plane.

The matrix has the following contents: fx 0   px 0  fy  py 0  0   1 The values `fx` and `fy` are the pixel focal length, and are identical for square pixels. The values `px` and `py` are the coordinates of the principal point—the offsets of the principal point from the top-left corner of the image frame. All values are expressed in pixels. The origin is at the center of the upper-left pixel.

## Discussion

![](https://developer.apple.com/tutorials/images/com.apple.arkit/media-2902622@2x.png)

## See Also

### Examining Imaging Parameters
- [var imageResolution: CGSize](./imageresolution.md)
  The width and height, in pixels, of the captured camera image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/intrinsics)*