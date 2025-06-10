# init(_:_:_:order:)

**Framework**: Spatial  
**Kind**: init

Creates a new Euler angles structure from the specified angle structures and order.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+
- Unknown ?+ - Deprecated
- Mac Catalyst ?+

## Declaration

```swift
init(_ x: Angle2D, _ y: Angle2D, _ z: Angle2D, order: EulerAngles.Order)
```

## Parameters

- `x`: The first angle.
- `y`: The second angle.
- `z`: The third angle.
- `order`: The Euler angle order.

## See Also

- [init(eye: Point3D, target: Point3D, up: Vector3D)](rotation3d/init(eye:target:up:).md)
  Creates a rotation structure that’s the look-at direction from a position to a target.
- [init(axis: RotationAxis3D, angle: Angle2D)](rotation3d/init(axis:angle:).md)
  Creates a rotation structure with the specified axis and the specified angle from Spatial structures.
- [init(quaternion: simd_quatf)](rotation3d/init(quaternion:)-6ajmn.md)
  Creates a rotation axis from the specified single-precision quaternion.
- [static let zero: Rotation3D](rotation3d/zero.md)
  The rotation with the zero value.
- [var isZero: Bool](rotation3d/iszero.md)
  A Boolean value that indicates whether the rotation is zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/eulerangles/init(_:_:_:order:))*