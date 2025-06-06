# MKPolylineRenderer

**Framework**: MapKit  
**Kind**: class

A visual representation of any polyline overlay object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
class MKPolylineRenderer
```

#### Overview

This renderer strokes the line only; it doesn’t fill it. You can change the color and other drawing attributes of the polyline by modifying the properties it inherits from the main class. You typically use this class as-is and don’t subclass it.

## Topics

### Creating a polyline renderer
- [init(polyline: MKPolyline)](mkpolylinerenderer/init(polyline:).md)
  Creates a new overlay view using the specified polyline overlay object.
### Accessing the polyline overlay
- [var polyline: MKPolyline](mkpolylinerenderer/polyline.md)
  The polyline overlay object that contains the information for drawing the overlay.
### Accessing the stroke
- [var strokeStart: CGFloat](mkpolylinerenderer/strokestart.md)
  The unit distance along the line where the stroke starts.
- [var strokeEnd: CGFloat](mkpolylinerenderer/strokeend.md)
  The unit distance along the line where the stroke ends.

## Relationships

### Inherits From
- [MKOverlayPathRenderer](mkoverlaypathrenderer.md)
### Inherited By
- [MKGradientPolylineRenderer](mkgradientpolylinerenderer.md)
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
- [class MKMultiPolylineRenderer](mkmultipolylinerenderer.md)
  A visual representation of multiple polyline overlay objects.
- [class MKGradientPolylineRenderer](mkgradientpolylinerenderer.md)
  A visual representation of any polyline overlay object with a gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpolylinerenderer)*