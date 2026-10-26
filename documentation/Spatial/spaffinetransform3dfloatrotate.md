# SPAffineTransform3DFloatRotate

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
static SPAffineTransform3DFloat SPAffineTransform3DFloatRotate(SPAffineTransform3DFloat transform, SPRotation3DFloat rotation);
```

#### Return Value

A transform that’s rotated by the specified rotation.

#### Discussion

Returns an affine transform that’s constructed by concatenating an existing affine transform and a rotation.

## Parameters

- `transform`: The source transform.
- `rotation`: The rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spaffinetransform3dfloatrotate)*