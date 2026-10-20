# MKPolyline

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

An open polygon overlay consisting of one or more connected line segments.

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
class MKPolyline
```

```objc
@interface MKPolyline : MKMultiPoint
```

#### Overview

The points connect end-to-end in the order that you provide them. The first and last points don’t automatically connect to each other.

## Topics

### Creating a polyline overlay
- [convenience init(points: UnsafePointer<MKMapPoint>, count: Int)](./mkpolyline/init%28points,count%29.md)
  Creates a polyline object from the specified set of map points.
- [convenience init(coordinates: UnsafePointer<CLLocationCoordinate2D>, count: Int)](./mkpolyline/init%28coordinates,count%29.md)
  Creates a polyline object from the specified set of coordinates.

## Relationships

### Inherits From
- [MKMultiPoint](./mkmultipoint.md)
### Inherited By
- [MKGeodesicPolyline](./mkgeodesicpolyline.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [MKAnnotation](./mkannotation.md)
- [MKGeoJSONObject](./mkgeojsonobject.md)
- [MKOverlay](./mkoverlay.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Multiple segment lines
- [class MKGeodesicPolyline](./mkgeodesicpolyline.md)
  An open polygon overlay consisting of line segments that follow the contours of the Earth to create the shortest path between the specified points.
- [class MKMultiPolyline](./mkmultipolyline.md)
  A collection of multipolyline shapes, each consisting of one or more connected line segments.
- [class MKPolylineRenderer](./mkpolylinerenderer.md)
  A visual representation of any polyline overlay object.
- [class MKMultiPolylineRenderer](./mkmultipolylinerenderer.md)
  A visual representation of multiple polyline overlay objects.
- [class MKGradientPolylineRenderer](./mkgradientpolylinerenderer.md)
  A visual representation of any polyline overlay object with a gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpolyline)*