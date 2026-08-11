# MapPolyline.ContourStyle

**Framework**: MapKit  
**Kind**: struct

Values that define how MapKit styles lines to represent the contour of the Earth.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
struct ContourStyle
```

## Topics

### Styles
- [static var geodesic: MapPolyline.ContourStyle](mappolyline/contourstyle/geodesic.md)
  Line segments that follow the contours of the Earth to represent the shortest path between the specified points.
- [static var straight: MapPolyline.ContourStyle](mappolyline/contourstyle/straight.md)
  Straight-line segments between points.

## See Also

- [func stroke(some ShapeStyle, lineWidth: CGFloat) -> some MapContent](mapcontent/stroke(_:linewidth:).md)
  Applies the given shape style to drawn map overlays using the line width you specify.
- [func stroke(some ShapeStyle, style: StrokeStyle) -> some MapContent](mapcontent/stroke(_:style:).md)
  Applies the given shape style to drawn map overlays using the stroke style you specify.
- [func stroke(lineWidth: CGFloat) -> some MapContent](mapcontent/stroke(linewidth:).md)
  Applies the given stoke drawn map overlays using the line width you specify.
- [func strokeStyle(style: StrokeStyle) -> some MapContent](mapcontent/strokestyle(style:).md)
  Applies the given stroke style to drawn map overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mappolyline/contourstyle)*