# MapCircle

**Framework**: MapKit  
**Kind**: struct

A circular overlay with a configurable radius that you center on a geographic coordinate.

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
struct MapCircle
```

#### Overview

Use this view to create circular overlays in the closure you provide to the `content` parameter in [`Map`](map.md) initializers.

## Topics

### Creating a map circle
- [init(MKCircle)](mapcircle/init(_:).md)
  Creates a circle overlay from an existing map circle object.
- [init(center: CLLocationCoordinate2D, radius: CLLocationDistance)](mapcircle/init(center:radius:).md)
  Creates a circle with the center coordinate and radius you specify.
- [init(mapRect: MKMapRect)](mapcircle/init(maprect:).md)
  Creates the largest possible circle centered within the given map rectangle.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [MapContent](mapcontent.md)

## See Also

- [struct Annotation](annotation.md)
  A customizable annotation used to indicate a location on a map.
- [struct MapPolygon](mappolygon.md)
  A closed polygon overlay.
- [struct MapPolyline](mappolyline.md)
  An open polygon overlay consisting of one or more connected line segments.
- [struct Marker](marker.md)
  A balloon-shaped annotation that marks a map location.
- [struct UserAnnotation](userannotation.md)
  Displays the person’s current location on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcircle)*