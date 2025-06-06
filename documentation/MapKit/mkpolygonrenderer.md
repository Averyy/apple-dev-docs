# MKPolygonRenderer

**Framework**: MapKit  
**Kind**: class

The visual representation of a single polygon overlay.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
class MKPolygonRenderer
```

#### Overview

This renderer creates the polygon overlay by first filling the shape and then representing its outline with strokes. You can change the color and other drawing attributes of the polygon by modifying the properties inherited from the parent class.

## Topics

### Creating a polygon renderer
- [init(polygon: MKPolygon)](mkpolygonrenderer/init(polygon:).md)
  Creates a new renderer that handles drawing for the specified polygon overlay object.
### Accessing the polygon overlay object
- [var polygon: MKPolygon](mkpolygonrenderer/polygon.md)
  The polygon object that contains the information used to draw the overlay’s contents.
### Accessing the stroke
- [var strokeStart: CGFloat](mkpolygonrenderer/strokestart.md)
  The unit distance along the polygon where the stroke starts.
- [var strokeEnd: CGFloat](mkpolygonrenderer/strokeend.md)
  The unit distance along the polygon where the stroke ends.

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
- [class MKMultiPolygon](mkmultipolygon.md)
  A collection of multiple closed polygon overlays.
- [class MKMultiPolygonRenderer](mkmultipolygonrenderer.md)
  The visual representation of multiple polygon overlays.
- [class MKOverlayPathRenderer](mkoverlaypathrenderer.md)
  The visual representation of a path-based overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpolygonrenderer)*