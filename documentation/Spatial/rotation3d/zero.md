# zero

**Framework**: Spatial  
**Kind**: property

The rotation with the zero value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static let zero: Rotation3D
```

## See Also

- [init(Angle2D, Angle2D, Angle2D, order: EulerAngles.Order)](eulerangles/init(_:_:_:order:).md)
  Creates a new Euler angles structure from the specified angle structures and order.
- [init(eye: Point3D, target: Point3D, up: Vector3D)](rotation3d/init(eye:target:up:).md)
  Creates a rotation structure that’s the look-at direction from a position to a target.
- [init(axis: RotationAxis3D, angle: Angle2D)](rotation3d/init(axis:angle:).md)
  Creates a rotation structure with the specified axis and the specified angle from Spatial structures.
- [init(quaternion: simd_quatf)](rotation3d/init(quaternion:)-6ajmn.md)
  Creates a rotation axis from the specified single-precision quaternion.
- [var isZero: Bool](rotation3d/iszero.md)
  A Boolean value that indicates whether the rotation is zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d/zero)*