# MKShape

**Framework**: MapKit  
**Kind**: class

An abstract class that defines the basic properties for all shape-based overlay objects.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
class MKShape
```

#### Overview

You can’t instantiate this class directly; use a subclass instead. Subclasses are responsible for defining the geometry of the shape and providing an appropriate value for the coordinate property they inherit from the [`MKAnnotation`](mkannotation.md) protocol.

## Topics

### Accessing the shape attributes
- [var title: String?](mkshape/title.md)
  The title of the shape annotation.
- [var subtitle: String?](mkshape/subtitle.md)
  The subtitle of the shape annotation.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MKCircle](mkcircle.md)
- [MKMultiPoint](mkmultipoint.md)
- [MKMultiPolygon](mkmultipolygon.md)
- [MKMultiPolyline](mkmultipolyline.md)
- [MKPointAnnotation](mkpointannotation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MKAnnotation](mkannotation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MKOverlay](mkoverlay.md)
  An interface for associating content with a specific map region.
- [class MKOverlayRenderer](mkoverlayrenderer.md)
  The shared infrastructure for drawing overlays on the map surface.
- [class MKMultiPoint](mkmultipoint.md)
  An abstract class that defines the common behavior that open and closed polygon overlays share.
- [class MKPlacemark](mkplacemark.md)
  A user-friendly description of a location on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkshape)*