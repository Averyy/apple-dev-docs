# SPPose3DMakeWithVector

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Creates a pose with the specified position and rotation vectors.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```c
static SPPose3D SPPose3DMakeWithVector(simd_double3 position, simd_quatd rotation);
```

## See Also

### Creating a 3D pose structure
- [SPPose3DMakeLookAt](./sppose3dmakelookat-6y4bb.md)
  Returns a pose at the specified position with the rotation towards the target.
- [SPPose3DMakeLookAt](./sppose3dmakelookat-8brxe.md)
- [SPPose3DMakeLookAt](./sppose3dmakelookat-dgpp.md)
- [SPPose3DMakeWith4x4Matrix](./sppose3dmakewith4x4matrix.md)
  Creates a pose from the specified 4 x 4 double-precision matrix.
- [SPPose3DMakeWithAffineTransform](./sppose3dmakewithaffinetransform.md)
  Returns a pose with a position and rotation that an affine transform defines.
- [SPPose3DMakeWithProjectiveTransform](./sppose3dmakewithprojectivetransform.md)
  Returns a pose with a position and rotation that a projective transform defines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppose3dmakewithvector)*