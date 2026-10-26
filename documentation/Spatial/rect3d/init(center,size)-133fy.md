# init(center:size:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

Creates a rectangle with the specified center and the specified size from Spatial structures.

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
init(center: Point3D, size: Size3D)
```

```c
static SPRect3D SPRect3DMakeAtCenter(SPPoint3D center, SPSize3D size);
```

## Parameters

- `center`: A point structure that specifies the rectangle’s center.
- `size`: A size structure that specifies the rectangle’s size.

## See Also

### Creating a 3D rectangle structure
- [init()](./init%28%29.md)
  Creates a rectangle structure.
- [init(center: simd_double3, size: simd_double3)](./init%28center,size%29-77l0z.md)
  Creates a rectangle with the specified center and the specified size from double-precision vectors.
- [init(center: Vector3D, size: Vector3D)](./init%28center,size%29-9cfq7.md)
  Creates a rectangle with the specified center and the specified size from Spatial vectors.
- [init(center: simd_float3, size: simd_float3)](./init%28center,size%29-zr2x.md)
  Creates a rectangle with the specified center and the specified size from single-precision vectors.
- [init(origin: simd_double3, size: simd_double3)](./init%28origin,size%29-5xyrs.md)
  Creates a rectangle at the specified origin with the specified size from double-precision vectors.
- [init(origin: simd_float3, size: simd_float3)](./init%28origin,size%29-7fnuf.md)
  Creates a rectangle at the specified origin with the specified size from single-precision vectors.
- [init(origin: Vector3D, size: Vector3D)](./init%28origin,size%29-7o8ad.md)
  Creates a rectangle with the specified origin and the specified size from Spatial vectors.
- [init(origin: Point3D, size: Size3D)](./init%28origin,size%29-7v73.md)
  Creates a rectangle at the specified origin and the specified size from Spatial structures.
- [init(origin: Point3D, size: Size3D)](./init%28origin,size%29-9a089.md)
  Creates a rectangle structure.
- [init(points: [Point3D])](./init%28points%29.md)
  Creates a rectangle that’s the bounding box of the specified points.
- [SPRect3DMakeAtCenterWithVector](../sprect3dmakeatcenterwithvector-9118a.md)
  Creates a rectangle with the specified center and the specified size from double-precision vectors.
- [SPRect3DMakeAtCenterWithVector](../sprect3dmakeatcenterwithvector-9doe4.md)
- [SPRect3DMakeAtOriginWithVector](../sprect3dmakeatoriginwithvector-36awh.md)
  Creates a rectangle at the specified origin and the specified size from double-precision vectors.
- [SPRect3DMakeAtOriginWithVector](../sprect3dmakeatoriginwithvector-7m66h.md)
- [SPRect3DMakeBoundingFromPoints](../sprect3dmakeboundingfrompoints.md)
  Creates a rectangle that’s the bounding box of the specified points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3d/init(center:size:)-133fy)*