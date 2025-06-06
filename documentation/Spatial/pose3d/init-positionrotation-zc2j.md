# init(position:rotation:)

**Framework**: Spatial  
**Kind**: init

Creates a pose with the specified double-precision position vector and quaternion.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
init(position: simd_double3 = .zero, rotation: simd_quatd)
```

## Parameters

- `position`: A vector that specifies the position of the pose.
- `rotation`: A quaternion structure that specifies the rotation of the pose.

## See Also

- [init()](pose3d/init.md)
  Creates a pose structure.
- [init?(simd_float4x4)](pose3d/init(_:)-8njy6.md)
  Creates a pose from the specified 4 x 4 single-precision matrix.
- [init?(simd_double4x4)](pose3d/init(_:)-9xspz.md)
  Creates a pose from the specified 4 x 4 double-precision matrix.
- [init(forward: Vector3D, up: Vector3D)](pose3d/init(forward:up:).md)
  Creates a pose with the specified forward and up vectors.
- [init(position: simd_float3, rotation: simd_quatf)](pose3d/init(position:rotation:)-1gu7k.md)
  Creates a pose with the specified single-precision position vector and quaternion.
- [init(position: Point3D, rotation: Rotation3D)](pose3d/init(position:rotation:)-5afaf.md)
  Creates a pose with the specified Spatial position and rotation structures.
- [init(position: Point3D, rotation: Rotation3D)](pose3d/init(position:rotation:)-5vswy.md)
  Creates a pose with the specified single-precision position vector and quaternion.
- [init(position: Point3D, target: Point3D, up: Vector3D)](pose3d/init(position:target:up:).md)
  Returns a pose at the specified position with the rotation towards the target.
- [init?(transform: AffineTransform3D)](pose3d/init(transform:)-2sey4.md)
  Returns a pose with a position and rotation defined by an affine transform.
- [init?(transform: ProjectiveTransform3D)](pose3d/init(transform:)-4go9c.md)
  Returns a pose with a position and rotation defined by a projective transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/pose3d/init(position:rotation:)-zc2j)*