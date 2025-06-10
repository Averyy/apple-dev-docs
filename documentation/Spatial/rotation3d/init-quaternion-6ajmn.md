# init(quaternion:)

**Framework**: Spatial  
**Kind**: init

Creates a rotation axis from the specified single-precision quaternion.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- visionOS ?+
- watchOS 9.0+
- Unknown ?+ - Deprecated
- tvOS 16.0+

## Declaration

```swift
init(quaternion: simd_quatf)
```

## Parameters

- `quaternion`: A single-precision quaternion that specifies the rotation.

## See Also

- [init(Angle2D, Angle2D, Angle2D, order: EulerAngles.Order)](eulerangles/init(_:_:_:order:).md)
  Creates a new Euler angles structure from the specified angle structures and order.
- [init(eye: Point3D, target: Point3D, up: Vector3D)](rotation3d/init(eye:target:up:).md)
  Creates a rotation structure that’s the look-at direction from a position to a target.
- [init(axis: RotationAxis3D, angle: Angle2D)](rotation3d/init(axis:angle:).md)
  Creates a rotation structure with the specified axis and the specified angle from Spatial structures.
- [static let zero: Rotation3D](rotation3d/zero.md)
  The rotation with the zero value.
- [var isZero: Bool](rotation3d/iszero.md)
  A Boolean value that indicates whether the rotation is zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d/init(quaternion:)-6ajmn)*