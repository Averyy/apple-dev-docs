# init(position:rotation:scale:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

Creates a pose with the specified Spatial position, rotation, and scale structures.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
init(position: Point3D, rotation: Rotation3D, scale: Double)
```

## See Also

### Creating a 3D scaled-pose structure
- [init()](./init%28%29.md)
  Creates a scaled pose structure.
- [init?(simd_float4x4)](./init%28_%29-v6ox.md)
  Creates a scaled pose from the specified 4 x 4 single-precision matrix.
- [init?(simd_double4x4)](./init%28_%29-4izkj.md)
  Creates a scaled pose from the specified 4 x 4 double-precision matrix.
- [init(forward: Vector3D, scale: Double, up: Vector3D)](./init%28forward,scale,up%29.md)
  Creates a scaled pose with the specified forward and up vectors.
- [init(position: simd_float3, rotation: simd_quatf, scale: Float)](./init%28position,rotation,scale%29-8ndo4.md)
  Creates a scaled pose with the specified single-precision position vector and quaternion.
- [init(position: simd_double3, rotation: simd_quatd, scale: Double)](./init%28position,rotation,scale%29-6fom1.md)
  Creates a scaled pose with the specified double-precision position vector and quaternion.
- [init(position: Point3D, target: Point3D, scale: Double, up: Vector3D)](./init%28position,target,scale,up%29.md)
  Returns a scaled pose at the specified position with the rotation toward the target.
- [init(position: Point3D, rotation: Rotation3D, scale: Double)](./init%28position,rotation,scale%29-8fyu0.md)
  Creates a scaled pose with the specified double-precision position vector and quaternion.
- [init?(transform: AffineTransform3D)](./init%28transform%29-oogv.md)
  Returns a scaled pose with a position, rotation, and scale defined by an affine transform.
- [init?(transform: ProjectiveTransform3D)](./init%28transform%29-9s08k.md)
  Returns a scaled pose with a position, rotation, and scale defined by a projective transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/scaledpose3d/init(position:rotation:scale:)-7ya6f)*