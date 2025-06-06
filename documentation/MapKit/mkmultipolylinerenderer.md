# MKMultiPolylineRenderer

**Framework**: MapKit  
**Kind**: class

A visual representation of multiple polyline overlay objects.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MKMultiPolylineRenderer
```

#### Overview

Use the multipolyline renderer to provide the styling of multiple polylines that you create using [`MKMultiPolyline`](mkmultipolyline.md).

## Topics

### Creating a multipolyline renderer
- [init(multiPolyline: MKMultiPolyline)](mkmultipolylinerenderer/init(multipolyline:).md)
  Creates an object that renders a visual representation of multiple polyline objects.
### Accessing the multipolyline object
- [var multiPolyline: MKMultiPolyline](mkmultipolylinerenderer/multipolyline.md)
  An object that represents multiple polyline shapes, each consisting of one or more connected line segments.

## Relationships

### Inherits From
- [MKOverlayPathRenderer](mkoverlaypathrenderer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MKPolyline](mkpolyline.md)
  An open polygon overlay consisting of one or more connected line segments.
- [class MKGeodesicPolyline](mkgeodesicpolyline.md)
  An open polygon overlay consisting of line segments that follow the contours of the Earth to create the shortest path between the specified points.
- [class MKMultiPolyline](mkmultipolyline.md)
  A collection of multipolyline shapes, each consisting of one or more connected line segments.
- [class MKPolylineRenderer](mkpolylinerenderer.md)
  A visual representation of any polyline overlay object.
- [class MKGradientPolylineRenderer](mkgradientpolylinerenderer.md)
  A visual representation of any polyline overlay object with a gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmultipolylinerenderer)*