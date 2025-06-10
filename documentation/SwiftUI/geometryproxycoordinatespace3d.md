# GeometryProxyCoordinateSpace3D

**Framework**: SwiftUI  
**Kind**: struct

A representation of a `GeometryProxy3D` which can be used for `CoordinateSpace3D` based conversions.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct GeometryProxyCoordinateSpace3D
```

## Topics

### Instance Methods
- [func anchored(in: UnitPoint3D) -> some CoordinateSpace3D](geometryproxycoordinatespace3d/anchored(in:).md)
  Returns a modified `CoordinateSpace3D` offset to match the provided `anchorPoint` in the original coordinate space.

## Relationships

### Conforms To
- [CoordinateSpace3D](../Spatial/CoordinateSpace3D.md)

## See Also

- [enum Axis](axis.md)
  The horizontal or vertical dimension in a 2D coordinate system.
- [struct Angle](angle.md)
  A geometric angle whose value you access in either radians or degrees.
- [struct UnitPoint](unitpoint.md)
  A normalized 2D point in a view’s coordinate space.
- [struct UnitPoint3D](unitpoint3d.md)
  A normalized 3D point in a view’s coordinate space.
- [struct Anchor](anchor.md)
  An opaque value derived from an anchor source and a particular view.
- [protocol DepthAlignmentID](depthalignmentid.md)
- [struct Alignment3D](alignment3d.md)
  An alignment in all three axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/geometryproxycoordinatespace3d)*