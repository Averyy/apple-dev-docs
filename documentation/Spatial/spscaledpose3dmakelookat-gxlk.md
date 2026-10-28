# SPScaledPose3DMakeLookAt

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```c
static SPScaledPose3D SPScaledPose3DMakeLookAt(SPVector3D forward, double scale, SPVector3D up);
```

## Return Value

A new scaled pose stucture.

## Discussion

Returns a scaled pose with the specified forward and up vectors.

> **Note**: This function creates a scaled pose where @p +z is forward.

## Parameters

- `forward`: The forward direction.
- `scale`: The uniform scale of the pose.
- `up`: The up direction.

## See Also

### Creating a 3D scaled-pose structure
- [SPScaledPose3DMake](./spscaledpose3dmake-9dbop.md)
  Returns a scaled pose with the specified position, rotation, and scale.
- [SPScaledPose3DMake](./spscaledpose3dmake-793r5.md)
- [SPScaledPose3DMakeLookAt](./spscaledpose3dmakelookat-7bxnk.md)
  Returns a scaled pose at the specified position with the rotation towards the target.
- [SPScaledPose3DMakeLookAt](./spscaledpose3dmakelookat-8yp17.md)
- [SPScaledPose3DMakeWith4x4Matrix](./spscaledpose3dmakewith4x4matrix.md)
  Returns a new scaled pose structure from the specified 4 x 4 matrix.
- [SPScaledPose3DMakeWithAffineTransform](./spscaledpose3dmakewithaffinetransform.md)
  Returns a scaled pose with a position, rotation, and scale that the specified affine transform defines.
- [SPScaledPose3DMakeWithProjectiveTransform](./spscaledpose3dmakewithprojectivetransform.md)
  Returns a scaled pose with a position, rotation, and scale that the specified projective transform defines.
- [SPScaledPose3DMakeWithVector](./spscaledpose3dmakewithvector.md)
  Returns a scaled pose with the specified position, rotation, and scale.
- [SPScaledPose3DIdentity](./spscaledpose3didentity.md)
  A structure that contains a position, rotation, and scale.
- [SPScaledPose3DInvalid](./spscaledpose3dinvalid.md)
  A structure that contains a position, rotation, and scale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spscaledpose3dmakelookat-gxlk)*