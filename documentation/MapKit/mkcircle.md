# MKCircle

**Framework**: MapKit  
**Kind**: class

A circular overlay with a configurable radius that you center on a geographic coordinate.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
class MKCircle
```

#### Overview

This class defines the portion of the map that the overlay covers. To draw the region, return an [`MKCircleRenderer`](mkcirclerenderer.md) object from the [`mapView(_:rendererFor:)`](mkmapviewdelegate/mapview(_:rendererfor:).md) method of your map view delegate.

## Topics

### Creating a circle overlay
- [convenience init(center: CLLocationCoordinate2D, radius: CLLocationDistance)](mkcircle/init(center:radius:).md)
  Creates and returns a circle object using the specified coordinate and radius.
- [convenience init(mapRect: MKMapRect)](mkcircle/init(maprect:).md)
  Creates and returns a circle object that derives the circular area from the specified rectangle.
### Accessing the overlay’s attributes
- [var coordinate: CLLocationCoordinate2D](mkcircle/coordinate.md)
  The center point of the circular area, specified as a latitude and longitude.
- [var radius: CLLocationDistance](mkcircle/radius.md)
  The radius of the circular area, in meters.
- [var boundingMapRect: MKMapRect](mkcircle/boundingmaprect.md)
  The bounding rectangle of the circular area.

## Relationships

### Inherits From
- [MKShape](mkshape.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MKAnnotation](mkannotation.md)
- [MKOverlay](mkoverlay.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MKCircleRenderer](mkcirclerenderer.md)
  The visual representation of a circular overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkcircle)*