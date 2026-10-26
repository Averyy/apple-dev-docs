# SPRect3DMakeAtCenterWithVector

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```c
static SPRect3D SPRect3DMakeAtCenterWithVector(SPVector3D center, SPVector3D size);
```

#### Return Value

A new rectangle stucture.

#### Discussion

Returns a rectangle at the specified center using Spatial vectors.

## Parameters

- `center`: A Spatial vector that specifies the center of the rectangle.
- `size`: A Spatial vector that specifies the size of the rectangle.

## See Also

### Creating a 3D rectangle structure
- [init(center: Point3D, size: Size3D)](./rect3d/init%28center,size%29-133fy.md)
  Creates a rectangle with the specified center and the specified size from Spatial structures.
- [init(origin: Point3D, size: Size3D)](./rect3d/init%28origin,size%29-9a089.md)
  Creates a rectangle structure.
- [SPRect3DMakeAtCenterWithVector](./sprect3dmakeatcenterwithvector-9118a.md)
  Creates a rectangle with the specified center and the specified size from double-precision vectors.
- [SPRect3DMakeAtOriginWithVector](./sprect3dmakeatoriginwithvector-36awh.md)
  Creates a rectangle at the specified origin and the specified size from double-precision vectors.
- [SPRect3DMakeAtOriginWithVector](./sprect3dmakeatoriginwithvector-7m66h.md)
- [SPRect3DMakeBoundingFromPoints](./sprect3dmakeboundingfrompoints.md)
  Creates a rectangle that’s the bounding box of the specified points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprect3dmakeatcenterwithvector-9doe4)*