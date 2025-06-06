# MKMultiPolygon

**Framework**: MapKit  
**Kind**: class

A collection of multiple closed polygon overlays.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MKMultiPolygon
```

#### Overview

Use a [`MKMultiPolygon`](mkmultipolygon.md) when you have multiple distinct polygon shapes that you intend to render using the same style.

## Topics

### Creating a multipolygon
- [init([MKPolygon])](mkmultipolygon/init(_:).md)
  Creates a multipolygon object using the provided polygons.
### Accessing polygons
- [var polygons: [MKPolygon]](mkmultipolygon/polygons.md)
  An array containing the polygons that make up the multipolygon object.

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

- [class MKPolygon](mkpolygon.md)
  A closed polygon overlay.
- [class MKPolygonRenderer](mkpolygonrenderer.md)
  The visual representation of a single polygon overlay.
- [class MKMultiPolygonRenderer](mkmultipolygonrenderer.md)
  The visual representation of multiple polygon overlays.
- [class MKOverlayPathRenderer](mkoverlaypathrenderer.md)
  The visual representation of a path-based overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmultipolygon)*