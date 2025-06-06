# MKCircleRenderer

**Framework**: MapKit  
**Kind**: class

The visual representation of a circular overlay.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
class MKCircleRenderer
```

#### Overview

This renderer fills and strokes the circular region that the overlay object represents. You can change the color and other drawing attributes of the circle by modifying the properties it inherits from the main class. You typically use this class as-is and don’t subclass it.

You create an instance of this class in your map view delegate’s [`mapView(_:rendererFor:)`](mkmapviewdelegate/mapview(_:rendererfor:).md) method.

## Topics

### Creating a circle renderer
- [init(circle: MKCircle)](mkcirclerenderer/init(circle:).md)
  Creates a new overlay view using the specified circle overlay object.
### Accessing the overlay object
- [var circle: MKCircle](mkcirclerenderer/circle.md)
  The circle overlay object that contains the information for drawing the overlay.
### Accessing the stroke
- [var strokeStart: CGFloat](mkcirclerenderer/strokestart.md)
  The unit distance along the circle where the stroke starts.
- [var strokeEnd: CGFloat](mkcirclerenderer/strokeend.md)
  The unit distance along the circle where the stroke ends.

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

- [class MKCircle](mkcircle.md)
  A circular overlay with a configurable radius that you center on a geographic coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkcirclerenderer)*