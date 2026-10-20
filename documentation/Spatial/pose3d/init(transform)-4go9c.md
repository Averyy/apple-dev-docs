# init(transform:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

Returns a pose with a position and rotation defined by a projective transform.

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
init?(transform: ProjectiveTransform3D)
```

## Parameters

- `transform`: The source transform. The function only considers the transform’s rotation and translation components.

## See Also

### Creating a 3D pose structure
- [init()](./init%28%29.md)
  Creates a pose structure.
- [init?(simd_float4x4)](./init%28_%29-8njy6.md)
  Creates a pose from the specified 4 x 4 single-precision matrix.
- [init?(simd_double4x4)](./init%28_%29-9xspz.md)
  Creates a pose from the specified 4 x 4 double-precision matrix.
- [init(forward: Vector3D, up: Vector3D)](./init%28forward,up%29.md)
  Creates a pose with the specified forward and up vectors.
- [init(position: simd_float3, rotation: simd_quatf)](./init%28position,rotation%29-1gu7k.md)
  Creates a pose with the specified single-precision position vector and quaternion.
- [init(position: Point3D, rotation: Rotation3D)](./init%28position,rotation%29-5afaf.md)
  Creates a pose with the specified Spatial position and rotation structures.
- [init(position: Point3D, rotation: Rotation3D)](./init%28position,rotation%29-5vswy.md)
  Creates a pose with the specified single-precision position vector and quaternion.
- [init(position: simd_double3, rotation: simd_quatd)](./init%28position,rotation%29-zc2j.md)
  Creates a pose with the specified double-precision position vector and quaternion.
- [init(position: Point3D, target: Point3D, up: Vector3D)](./init%28position,target,up%29.md)
  Returns a pose at the specified position with the rotation towards the target.
- [init?(transform: AffineTransform3D)](./init%28transform%29-2sey4.md)
  Returns a pose with a position and rotation defined by an affine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/pose3d/init(transform:)-4go9c)*