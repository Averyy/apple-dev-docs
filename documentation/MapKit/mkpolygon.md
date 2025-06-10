# MKPolygon

**Framework**: MapKit  
**Kind**: class

A closed polygon overlay.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class MKPolygon
```

#### Overview

The points you add to this overlay connect end-to-end in the order you provide them. The first and last points connect to each other to create a closed shape.

When creating a polygon, you can mask out portions of the polygon by specifying one or more interior polygons. For the polygons you specify, this class uses the even-odd fill rule to determine the final occupied area. When applied to overlapping polygons, this rule can cause the framework to mask specific regions out and thereby remove them from the total occupied area. For more information about how fill rules apply to paths, see [`Paths`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_paths/dq_paths.html#//apple_ref/doc/uid/TP30001066-CH211) in [`Quartz 2D Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066).

## Topics

### Creating a polygon overlay
- [convenience init(points: UnsafePointer<MKMapPoint>, count: Int)](mkpolygon/init(points:count:).md)
  Creates and returns a polygon object from the specified set of map points.
- [convenience init(points: UnsafePointer<MKMapPoint>, count: Int, interiorPolygons: [MKPolygon]?)](mkpolygon/init(points:count:interiorpolygons:).md)
  Creates and returns a polygon object from the specified set of map points and interior polygons.
- [convenience init(coordinates: UnsafePointer<CLLocationCoordinate2D>, count: Int)](mkpolygon/init(coordinates:count:).md)
  Creates and returns a polygon object from the specified set of coordinates.
- [convenience init(coordinates: UnsafePointer<CLLocationCoordinate2D>, count: Int, interiorPolygons: [MKPolygon]?)](mkpolygon/init(coordinates:count:interiorpolygons:).md)
  Creates and returns a polygon object from the specified set of coordinates and interior polygons.
### Accessing the interior polygons
- [var interiorPolygons: [MKPolygon]?](mkpolygon/interiorpolygons.md)
  The array of polygons that nest inside the enclosing polygon.

## Relationships

### Inherits From
- [MKMultiPoint](mkmultipoint.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MKAnnotation](mkannotation.md)
- [MKGeoJSONObject](mkgeojsonobject.md)
- [MKOverlay](mkoverlay.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MKPolygonRenderer](mkpolygonrenderer.md)
  The visual representation of a single polygon overlay.
- [class MKMultiPolygon](mkmultipolygon.md)
  A collection of multiple closed polygon overlays.
- [class MKMultiPolygonRenderer](mkmultipolygonrenderer.md)
  The visual representation of multiple polygon overlays.
- [class MKOverlayPathRenderer](mkoverlaypathrenderer.md)
  The visual representation of a path-based overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpolygon)*