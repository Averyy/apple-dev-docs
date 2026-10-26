# SPRotation3DSlerpLongest

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns the spherical linear interpolation along the longest arc between two rotations.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```c
static SPRotation3D SPRotation3DSlerpLongest(SPRotation3D from, SPRotation3D to, double t);
```

## See Also

### Transforming a 3D rotation structure
- [var inverse: Rotation3D](./rotation3d/inverse.md)
  The inverse of the rotation.
- [SPRotation3DSlerp](./sprotation3dslerp.md)
  Returns the spherical linear interpolation along the shortest arc between two rotations.
- [static let identity: Rotation3D](./rotation3d/identity.md)
  The identity rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprotation3dslerplongest)*