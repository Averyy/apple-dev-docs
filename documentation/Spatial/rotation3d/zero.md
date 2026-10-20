# zero

**Framework**: Spatial  
**Kind**: property  
**Role**: Type Property

The rotation with the zero value.

**Availability**:
- iOS 16.0+ - Deprecated in 17.0
- iPadOS 16.0+ - Deprecated in 17.0
- Mac Catalyst 16.0+ - Deprecated in 17.0
- macOS 13.0+ - Deprecated in 14.0
- tvOS 16.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.0+ - Deprecated in 10.0

> **Deprecated**: This constant is deprecated.

## Declaration

```swift
static let zero: Rotation3D
```

```c
static const SPRotation3D SPRotation3DZero;
```

## See Also

### Deprecated symbols
- [init(Angle2D, Angle2D, Angle2D, order: EulerAngles.Order)](../eulerangles/init%28_,_,_,order%29.md)
  Creates a new Euler angles structure from the specified angle structures and order.
- [init(eye: Point3D, target: Point3D, up: Vector3D)](./init%28eye,target,up%29.md)
  Creates a rotation structure that’s the look-at direction from a position to a target.
- [init(axis: RotationAxis3D, angle: Angle2D)](./init%28axis,angle%29.md)
  Creates a rotation structure with the specified axis and the specified angle from Spatial structures.
- [init(quaternion: simd_quatf)](./init%28quaternion%29-6ajmn.md)
  Creates a rotation axis from the specified single-precision quaternion.
- [var isZero: Bool](./iszero.md)
  A Boolean value that indicates whether the rotation is zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d/zero)*