# MapPolyline

**Framework**: MapKit  
**Kind**: struct

An open polygon overlay consisting of one or more connected line segments.

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
struct MapPolyline
```

#### Overview

Use this view to create map polylines instances in the closure you provide to the `content` parameter in the [`Map`](map.md) initializers.

## Topics

### Creating a polyline
- [init(MKPolyline)](mappolyline/init(_:)-93u7w.md)
  Creates a polyline from polyline you provide.
- [init(MKRoute)](mappolyline/init(_:)-5p2kx.md)
  Creates a polyline that traces the route you provide.
- [init(coordinates: [CLLocationCoordinate2D], contourStyle: MapPolyline.ContourStyle)](mappolyline/init(coordinates:contourstyle:).md)
  Creates a polyline that traces a path between the given coordinates using the specifed contour style.
- [init(points: [MKMapPoint], contourStyle: MapPolyline.ContourStyle)](mappolyline/init(points:contourstyle:).md)
  Creates a new polyline that traces a path between the provided points using the specifed contour style.
### Styling the polyline
- [func stroke(some ShapeStyle, lineWidth: CGFloat) -> some MapContent](mapcontent/stroke(_:linewidth:).md)
  Applies the given shape style to drawn map overlays using the line width you specify.
- [func stroke(some ShapeStyle, style: StrokeStyle) -> some MapContent](mapcontent/stroke(_:style:).md)
  Applies the given shape style to drawn map overlays using the stroke style you specify.
- [func stroke(lineWidth: CGFloat) -> some MapContent](mapcontent/stroke(linewidth:).md)
  Applies the given stoke drawn map overlays using the line width you specify.
- [func strokeStyle(style: StrokeStyle) -> some MapContent](mapcontent/strokestyle(style:).md)
  Applies the given stroke style to drawn map overlays.
- [MapPolyline.ContourStyle](mappolyline/contourstyle.md)
  Values that define how MapKit styles lines to represent the contour of the Earth.
### Setting the overlay level
- [func mapOverlayLevel(level: MKOverlayLevel) -> some MapContent](mapcontent/mapoverlaylevel(level:).md)
  Specifies the position of overlays relative to other map content.
### Type aliases
- [associatedtype Body : MapContent](mapcontent/body-swift.associatedtype.md)
  The content and behavior of the view.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Escapable](../Swift/Escapable.md)
- [MapContent](mapcontent.md)

## See Also

- [struct Annotation](annotation.md)
  A customizable annotation used to indicate a location on a map.
- [struct MapCircle](mapcircle.md)
  A circular overlay with a configurable radius that you center on a geographic coordinate.
- [struct MapPolygon](mappolygon.md)
  A closed polygon overlay.
- [struct Marker](marker.md)
  A balloon-shaped annotation that marks a map location.
- [struct UserAnnotation](userannotation.md)
  Displays the person’s current location on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mappolyline)*