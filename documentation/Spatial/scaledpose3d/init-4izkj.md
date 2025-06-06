# init(_:)

**Framework**: Spatial  
**Kind**: init

Creates a scaled pose from the specified 4 x 4 double-precision matrix.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS ?+
- watchOS 11.0+

## Declaration

```swift
init?(_ matrix: simd_double4x4)
```

## See Also

- [init()](scaledpose3d/init.md)
  Creates a scaled pose structure.
- [init?(simd_float4x4)](scaledpose3d/init(_:)-v6ox.md)
  Creates a scaled pose from the specified 4 x 4 single-precision matrix.
- [init(forward: Vector3D, scale: Double, up: Vector3D)](scaledpose3d/init(forward:scale:up:).md)
  Creates a scaled pose with the specified forward and up vectors.
- [init(position: simd_float3, rotation: simd_quatf, scale: Float)](scaledpose3d/init(position:rotation:scale:)-8ndo4.md)
  Creates a scaled pose with the specified single-precision position vector and quaternion.
- [init(position: simd_double3, rotation: simd_quatd, scale: Double)](scaledpose3d/init(position:rotation:scale:)-6fom1.md)
  Creates a scaled pose with the specified double-precision position vector and quaternion.
- [init(position: Point3D, target: Point3D, scale: Double, up: Vector3D)](scaledpose3d/init(position:target:scale:up:).md)
  Returns a scaled pose at the specified position with the rotation toward the target.
- [init(position: Point3D, rotation: Rotation3D, scale: Double)](scaledpose3d/init(position:rotation:scale:)-7ya6f.md)
  Creates a pose with the specified Spatial position, rotation, and scale structures.
- [init(position: Point3D, rotation: Rotation3D, scale: Double)](scaledpose3d/init(position:rotation:scale:)-8fyu0.md)
  Creates a scaled pose with the specified double-precision position vector and quaternion.
- [init?(transform: AffineTransform3D)](scaledpose3d/init(transform:)-oogv.md)
  Returns a scaled pose with a position, rotation, and scale defined by an affine transform.
- [init?(transform: ProjectiveTransform3D)](scaledpose3d/init(transform:)-9s08k.md)
  Returns a scaled pose with a position, rotation, and scale defined by a projective transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/scaledpose3d/init(_:)-4izkj)*