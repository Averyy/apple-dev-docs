# SPAffineTransform3DFloatRotateByQuaternion

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```c
static SPAffineTransform3DFloat SPAffineTransform3DFloatRotateByQuaternion(SPAffineTransform3DFloat transform, simd_quatf quaternion);
```

#### Return Value

A transform that’s rotated by the specified quaternion.

#### Discussion

Returns an affine transform that’s constructed by concatenating an existing affine transform and a rotation specified by a quaternion.

## Parameters

- `transform`: The source transform.
- `quaternion`: The quaternion that defines the rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spaffinetransform3dfloatrotatebyquaternion)*