# MKMultiPolyline

**Framework**: MapKit  
**Kind**: class

A collection of multipolyline shapes, each consisting of one or more connected line segments.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class MKMultiPolyline
```

#### Overview

Use a [`MKMultiPolyline`](mkmultipolyline.md) object when you have multiple distinct polyline shapes that you intend to render using the same style.

## Topics

### Creating a multipolyline object
- [init([MKPolyline])](mkmultipolyline/init(_:).md)
  Creates a multipolyline object using the provided polylines.
### Accessing polyline objects
- [var polylines: [MKPolyline]](mkmultipolyline/polylines.md)
  An array containing the polyline objects that make up the multipolyline object.

## Relationships

### Inherits From
- [MKShape](mkshape.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MKAnnotation](mkannotation.md)
- [MKGeoJSONObject](mkgeojsonobject.md)
- [MKOverlay](mkoverlay.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MKPolyline](mkpolyline.md)
  An open polygon overlay consisting of one or more connected line segments.
- [class MKGeodesicPolyline](mkgeodesicpolyline.md)
  An open polygon overlay consisting of line segments that follow the contours of the Earth to create the shortest path between the specified points.
- [class MKPolylineRenderer](mkpolylinerenderer.md)
  A visual representation of any polyline overlay object.
- [class MKMultiPolylineRenderer](mkmultipolylinerenderer.md)
  A visual representation of multiple polyline overlay objects.
- [class MKGradientPolylineRenderer](mkgradientpolylinerenderer.md)
  A visual representation of any polyline overlay object with a gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmultipolyline)*