# SPScaledPose3DGet4x4Matrix

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns a 4 x 4 matrix that represents the scaled pose’s translation, rotation, and scale.

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
static simd_double4x4 SPScaledPose3DGet4x4Matrix(SPScaledPose3D scaledPose);
```

## See Also

### Inspecting a 3D scaled pose’s properties
- [var position: Point3D](./scaledpose3d/position.md)
  The scaled pose’s position.
- [var rotation: Rotation3D](./scaledpose3d/rotation.md)
  The scaled pose’s rotation.
- [var scale: Double](./scaledpose3d/scale.md)
  The scaled pose’s scale.
- [SPScaledPose3DGetInverse](./spscaledpose3dgetinverse.md)
  Returns a new scaled pose with the inverse matrix of the specified scaled pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spscaledpose3dget4x4matrix)*