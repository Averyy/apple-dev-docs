# MKMultiPolyline

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface MKMultiPolyline : MKShape
```

## Overview

Use a [`MKMultiPolyline`](./mkmultipolyline.md) object when you have multiple distinct polyline shapes that you intend to render using the same style.

## Topics

### Creating a multipolyline object
- [init([MKPolyline])](./mkmultipolyline/init%28_%29.md)
  Creates a multipolyline object using the provided polylines.
### Accessing polyline objects
- [var polylines: [MKPolyline]](./mkmultipolyline/polylines.md)
  An array containing the polyline objects that make up the multipolyline object.
### Initializers
- [init(polylines: [MKPolyline])](./mkmultipolyline/init%28polylines%29.md)

## Relationships

### Inherits From
- [MKShape](./mkshape.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [MKAnnotation](./mkannotation.md)
- [MKGeoJSONObject](./mkgeojsonobject.md)
- [MKOverlay](./mkoverlay.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Multiple segment lines
- [class MKPolyline](./mkpolyline.md)
  An open polygon overlay consisting of one or more connected line segments.
- [class MKGeodesicPolyline](./mkgeodesicpolyline.md)
  An open polygon overlay consisting of line segments that follow the contours of the Earth to create the shortest path between the specified points.
- [class MKPolylineRenderer](./mkpolylinerenderer.md)
  A visual representation of any polyline overlay object.
- [class MKMultiPolylineRenderer](./mkmultipolylinerenderer.md)
  A visual representation of multiple polyline overlay objects.
- [class MKGradientPolylineRenderer](./mkgradientpolylinerenderer.md)
  A visual representation of any polyline overlay object with a gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmultipolyline)*