# min

**Framework**: Spatial  
**Kind**: property  
**Role**: Instance Property

A point that represents the corner of the rectangle with the smallest x-, y-, and z-coordinates.

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
var min: Point3D { get }
```

```c
static SPPoint3D SPRect3DGetMinimum(SPRect3D rect);
```

## See Also

### Inspecting a 3D rectangle’s properties
- [var center: Point3D](./center.md)
  The center of the rectangle.
- [var cornerPoints: [Point3D]](./cornerpoints.md)
  The corner points of the rectangle.
- [var max: Point3D](./max.md)
  A point that represents the corner of the rectangle with the largest x-, y-, and z-coordinates.
- [var origin: Point3D](./origin.md)
  The origin of the rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3d/min)*