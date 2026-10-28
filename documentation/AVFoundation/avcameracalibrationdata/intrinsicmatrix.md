# intrinsicMatrix

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A matrix that relates a camera’s internal properties to an ideal pinhole-camera model.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var intrinsicMatrix: matrix_float3x3 { get }
```

```objc
@property (nonatomic, readonly) matrix_float3x3 intrinsicMatrix;
```

## Discussion

The intrinsic matrix allows you to transform 3D coordinates to 2D coordinates on an image plane using the pinhole camera model. Equations like the following commonly represent the intrinsic matrix as `K:`

![A mathematical equation for the intrinsic matrix. K equals a three-by-three matrix that corresponds to specific pixel values.](https://developer.apple.com/tutorials/images/com.apple.avfoundation/media-2902623@2x.png)

The equation expresses all values in pixels. The values `fx` and `fy` are the pixel focal length, and are identical for square pixels. The `ox` and `oy` values are the offsets of the principal point, from the top-left corner of the image frame. The principal point is relative to the top-left corner of the top-left pixel. Each pixel value represents a sampled value from the center of that pixel.

## See Also

### Mapping pixels to scene geometry
- [var intrinsicMatrixReferenceDimensions: CGSize](./intrinsicmatrixreferencedimensions.md)
  The image dimensions to which the camera’s intrinsic matrix values are relative.
- [var extrinsicMatrix: matrix_float4x3](./extrinsicmatrix.md)
  A matrix relating a camera’s position and orientation to a world or scene coordinate system.
- [var pixelSize: Float](./pixelsize.md)
  The size, in millimeters, of one image pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcameracalibrationdata/intrinsicmatrix)*