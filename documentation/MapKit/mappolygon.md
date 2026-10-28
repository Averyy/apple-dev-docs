# MapPolygon

**Framework**: MapKit  
**Kind**: struct  
**Role**: Structure

A closed polygon overlay.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
struct MapPolygon
```

## Overview

Use this view to create map polygons instances in the closure you provide to the `content` parameter in the [`Map`](./map.md) initializers.

## Topics

### Creating a map polygon
- [init(coordinates: [CLLocationCoordinate2D])](./mappolygon/init%28coordinates%29.md)
  Creates a polygon from a list of coordinates you provide.
- [init(points: [MKMapPoint])](./mappolygon/init%28points%29.md)
  Creates a polygon from a list of map points.
- [init(MKPolygon)](./mappolygon/init%28_%29.md)
  Creates a polygon from the polygon you provide.
### Styling the polygon
- [func foregroundStyle(some ShapeStyle) -> some MapContent](./mapcontent/foregroundstyle%28_%29.md)
  Specifies the shape style used to fill content in drawing map overlays.
- [func stroke(some ShapeStyle, lineWidth: CGFloat) -> some MapContent](./mapcontent/stroke%28_,linewidth%29.md)
  Applies the given shape style to drawn map overlays using the line width you specify.
- [func stroke(some ShapeStyle, style: StrokeStyle) -> some MapContent](./mapcontent/stroke%28_,style%29.md)
  Applies the given shape style to drawn map overlays using the stroke style you specify.
- [func stroke(lineWidth: CGFloat) -> some MapContent](./mapcontent/stroke%28linewidth%29.md)
  Applies the given stoke drawn map overlays using the line width you specify.
- [func strokeStyle(style: StrokeStyle) -> some MapContent](./mapcontent/strokestyle%28style%29.md)
  Applies the given stroke style to drawn map overlays.
- [func tint<S>(S) -> some MapContent](./mapcontent/tint%28_%29.md)
  The tint shape style to apply to map content.
### Setting the overlay level
- [func mapOverlayLevel(level: MKOverlayLevel) -> some MapContent](./mapcontent/mapoverlaylevel%28level%29.md)
  Specifies the position of overlays relative to other map content.
### Type aliases
- [associatedtype Body : MapContent](./mapcontent/body-swift.associatedtype.md)
  The content and behavior of the view.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [MapContent](./mapcontent.md)

## See Also

### Annotations and overlays
- [struct Annotation](./annotation.md)
  A customizable annotation used to indicate a location on a map.
- [struct MapCircle](./mapcircle.md)
  A circular overlay with a configurable radius that you center on a geographic coordinate.
- [struct MapPolyline](./mappolyline.md)
  An open polygon overlay consisting of one or more connected line segments.
- [struct Marker](./marker.md)
  A balloon-shaped annotation that marks a map location.
- [struct UserAnnotation](./userannotation.md)
  Displays the person’s current location on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mappolygon)*