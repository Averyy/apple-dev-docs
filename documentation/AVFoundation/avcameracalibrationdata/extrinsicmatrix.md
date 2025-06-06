# extrinsicMatrix

**Framework**: Avfoundation  
**Kind**: property

A matrix relating a camera’s position and orientation to a world or scene coordinate system.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var extrinsicMatrix: matrix_float4x3 { get }
```

#### Discussion

The extrinsic matrix consists of a unitless 3 x 3 rotation matrix (`R`) on the left and a 3 x 1 column vector translation (`t`) on the right. The translation vector’s units are millimeters.

![None](https://docs-assets.developer.apple.com/published/92babba2b0619b872714b9dcb8889260/media-2902624%402x.png)

The camera’s pose is expressed with respect to a reference camera (camera-to-world view). If the rotation matrix is an identity matrix, then this camera is the reference camera.

> **Note**:  A [`matrix_float4x3`](https://developer.apple.com/documentation/simd/matrix_float4x3) matrix is column major with 3 rows and 4 columns.

## See Also

- [var intrinsicMatrix: matrix_float3x3](avcameracalibrationdata/intrinsicmatrix.md)
  A matrix that relates a camera’s internal properties to an ideal pinhole-camera model.
- [var intrinsicMatrixReferenceDimensions: CGSize](avcameracalibrationdata/intrinsicmatrixreferencedimensions.md)
  The image dimensions to which the camera’s intrinsic matrix values are relative.
- [var pixelSize: Float](avcameracalibrationdata/pixelsize.md)
  The size, in millimeters, of one image pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcameracalibrationdata/extrinsicmatrix)*