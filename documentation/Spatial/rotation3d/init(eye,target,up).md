# init(eye:target:up:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

Creates a rotation structure that’s the look-at direction from a position to a target.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
init(eye: Point3D, target: Point3D, up: Vector3D = Vector3D(x: 0, y: 1, z: 0))
```

## Parameters

- `eye`: The eye position.
- `target`: The target position.
- `up`: The up direction.

## See Also

### Deprecated symbols
- [init(Angle2D, Angle2D, Angle2D, order: EulerAngles.Order)](../eulerangles/init%28_,_,_,order%29.md)
  Creates a new Euler angles structure from the specified angle structures and order.
- [init(axis: RotationAxis3D, angle: Angle2D)](./init%28axis,angle%29.md)
  Creates a rotation structure with the specified axis and the specified angle from Spatial structures.
- [init(quaternion: simd_quatf)](./init%28quaternion%29-6ajmn.md)
  Creates a rotation axis from the specified single-precision quaternion.
- [static let zero: Rotation3D](./zero.md)
  The rotation with the zero value.
- [var isZero: Bool](./iszero.md)
  A Boolean value that indicates whether the rotation is zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d/init(eye:target:up:))*