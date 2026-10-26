# SPRect3DGetCornerPoints

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns the corner points of the rectangle.

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
static void SPRect3DGetCornerPoints(SPRect3D rect, SPPoint3D points[]);
```

## See Also

### Inspecting a 3D rectangle’s properties
- [var center: Point3D](./rect3d/center.md)
  The center of the rectangle.
- [var max: Point3D](./rect3d/max.md)
  A point that represents the corner of the rectangle with the largest x-, y-, and z-coordinates.
- [var min: Point3D](./rect3d/min.md)
  A point that represents the corner of the rectangle with the smallest x-, y-, and z-coordinates.
- [var origin: Point3D](./rect3d/origin.md)
  The origin of the rectangle.
- [size](./sprect3d/size.md)
  The size of the rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprect3dgetcornerpoints)*