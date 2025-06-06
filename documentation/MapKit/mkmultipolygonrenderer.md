# MKMultiPolygonRenderer

**Framework**: MapKit  
**Kind**: class

The visual representation of multiple polygon overlays.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MKMultiPolygonRenderer
```

#### Overview

Use this renderer to provide the style for multiple polygons created using [`MKMultiPolygon`](mkmultipolygon.md).

## Topics

### Creating a multipolygon renderer
- [init(multiPolygon: MKMultiPolygon)](mkmultipolygonrenderer/init(multipolygon:).md)
  Creates and returns a renderer that handles drawing for the specified multipolygon overlay object.
### Accessing the multipolygon object
- [var multiPolygon: MKMultiPolygon](mkmultipolygonrenderer/multipolygon.md)
  The multipolygon object that the renderer uses to draw the overlay’s contents.

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

- [class MKPolygon](mkpolygon.md)
  A closed polygon overlay.
- [class MKPolygonRenderer](mkpolygonrenderer.md)
  The visual representation of a single polygon overlay.
- [class MKMultiPolygon](mkmultipolygon.md)
  A collection of multiple closed polygon overlays.
- [class MKOverlayPathRenderer](mkoverlaypathrenderer.md)
  The visual representation of a path-based overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmultipolygonrenderer)*