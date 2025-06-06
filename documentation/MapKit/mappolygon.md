# MapPolygon

**Framework**: MapKit  
**Kind**: struct

A closed polygon overlay.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
struct MapPolygon
```

#### Overview

Use this view to create map polygons instances in the closure you provide to the `content` parameter in the [`Map`](map.md) initializers.

## Topics

### Creating a map polygon
- [init(coordinates: [CLLocationCoordinate2D])](mappolygon/init(coordinates:).md)
  Creates a polygon from a list of coordinates you provide.
- [init(points: [MKMapPoint])](mappolygon/init(points:).md)
  Creates a polygon from a list of map points.
- [init(MKPolygon)](mappolygon/init(_:).md)
  Creates a polygon from the polygon you provide.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [MapContent](mapcontent.md)

## See Also

- [struct Annotation](annotation.md)
  A customizable annotation used to indicate a location on a map.
- [struct MapCircle](mapcircle.md)
  A circular overlay with a configurable radius that you center on a geographic coordinate.
- [struct MapPolyline](mappolyline.md)
  An open polygon overlay consisting of one or more connected line segments.
- [struct Marker](marker.md)
  A balloon-shaped annotation that marks a map location.
- [struct UserAnnotation](userannotation.md)
  Displays the person’s current location on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mappolygon)*