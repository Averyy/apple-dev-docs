# SPPose3DGet4x4Matrix

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns the pose’s underlying matrix.

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
static simd_double4x4 SPPose3DGet4x4Matrix(SPPose3D pose);
```

## See Also

### Inspecting a 3D pose’s properties
- [var position: Point3D](./pose3d/position.md)
  The pose’s position.
- [var rotation: Rotation3D](./pose3d/rotation.md)
  The pose’s rotation.
- [SPPose3DGetInverse](./sppose3dgetinverse.md)
  Returns the affine pose’s inverse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppose3dget4x4matrix)*