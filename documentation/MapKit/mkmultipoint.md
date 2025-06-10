# MKMultiPoint

**Framework**: MapKit  
**Kind**: class

An abstract class that defines the common behavior that open and closed polygon overlays share.

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
class MKMultiPoint
```

#### Overview

Don’t create instances of this class directly. Instead, create instances of the [`MKPolygon`](mkpolygon.md) or [`MKPolyline`](mkpolyline.md) classes. However, you can use the methods and property of this class to access information about the specific points associated with the line or polygon.

## Topics

### Accessing the points in the shape
- [func points() -> UnsafeMutablePointer<MKMapPoint>](mkmultipoint/points.md)
  Returns an array of map points associated with the shape.
- [var pointCount: Int](mkmultipoint/pointcount.md)
  The number of points associated with the shape.
- [func location(atPointIndex: Int) -> CGFloat](mkmultipoint/location(atpointindex:).md)
  Translates a point index into a unit distance along the shape.
- [func locations(at: IndexSet) -> [CGFloat]](mkmultipoint/locations(at:).md)
  Translates a point index set into a unit distance along the shape.
### Getting coordinate values
- [func getCoordinates(UnsafeMutablePointer<CLLocationCoordinate2D>, range: NSRange)](mkmultipoint/getcoordinates(_:range:).md)
  Retrieves one or more points associated with the shape and converts them to coordinate values.

## Relationships

### Inherits From
- [MKShape](mkshape.md)
### Inherited By
- [MKPolygon](mkpolygon.md)
- [MKPolyline](mkpolyline.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MKAnnotation](mkannotation.md)
- [MKGeoJSONObject](mkgeojsonobject.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MKOverlay](mkoverlay.md)
  An interface for associating content with a specific map region.
- [class MKOverlayRenderer](mkoverlayrenderer.md)
  The shared infrastructure for drawing overlays on the map surface.
- [class MKShape](mkshape.md)
  An abstract class that defines the basic properties for all shape-based overlay objects.
- [class MKPlacemark](mkplacemark.md)
  A user-friendly description of a location on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmultipoint)*