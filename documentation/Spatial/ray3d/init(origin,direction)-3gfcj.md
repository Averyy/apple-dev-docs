# init(origin:direction:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

Creates a ray with the specified origin and the specified direction from single-precision vectors.

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
init(origin: simd_float3 = .zero, direction: simd_float3)
```

## Parameters

- `origin`: A vector that specifies the ray’s origin.
- `direction`: A vector that specifies the ray’s direction.

## See Also

### Creating a 3D ray structure
- [init()](./init%28%29.md)
  Creates a ray structure.
- [init(origin: Point3D, direction: Vector3D)](./init%28origin,direction%29-5sxkl.md)
  Creates a ray with the specified origin and the specified direction from Spatial primitives.
- [init(origin: simd_double3, direction: simd_double3)](./init%28origin,direction%29-47w1c.md)
  Creates a ray with the specified origin and the specified direction from double-precision vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/ray3d/init(origin:direction:)-3gfcj)*