# MKOverlay

**Framework**: MapKit  
**Kind**: protocol

An interface for associating content with a specific map region.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
protocol MKOverlay : MKAnnotation
```

#### Overview

 are data objects that define the geographic data to cover. MapKit defines several concrete classes that adopt this protocol and define standard shapes like rectangles, circles, and polygons. You might use overlays to define the geographic boundaries of a national park or trace a bus route along city streets. You add an overlay to your map view by calling its [`addOverlay(_:)`](mkmapview/addoverlay(_:).md) method or any other map view method for adding overlays to the map. When the overlay’s region intersects the visible portion of the map, the map view calls the [`mapView(_:rendererFor:)`](mkmapviewdelegate/mapview(_:rendererfor:).md) method of its delegate to obtain the renderer object responsible for drawing the overlay.

If you add an overlay to a map view as an annotation, instead of adding it as an overlay, the map view treats your overlay as an annotation. Specifically, it displays your overlay only when its [`coordinate`](mkoverlay/coordinate.md) is in the visible map region, rather than displaying the overlay when any portion of its covered area is visible.

## Topics

### Describing the overlay geometry
- [var coordinate: CLLocationCoordinate2D](mkoverlay/coordinate.md)
  The approximate center point of the overlay area.
- [var boundingMapRect: MKMapRect](mkoverlay/boundingmaprect.md)
  The projected rectangle that encompasses the overlay.
### Determining map intersections
- [func intersects(MKMapRect) -> Bool](mkoverlay/intersects(_:).md)
  Returns a Boolean value that indicates whether the specified rectangle intersects the overlay’s shape.
### Optimizing map rendering
- [func canReplaceMapContent() -> Bool](mkoverlay/canreplacemapcontent.md)
  Returns a Boolean value that indicates whether the overlay content replaces the underlying map content.

## Relationships

### Inherits From
- [MKAnnotation](mkannotation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [MKCircle](mkcircle.md)
- [MKGeodesicPolyline](mkgeodesicpolyline.md)
- [MKMultiPolygon](mkmultipolygon.md)
- [MKMultiPolyline](mkmultipolyline.md)
- [MKPolygon](mkpolygon.md)
- [MKPolyline](mkpolyline.md)
- [MKTileOverlay](mktileoverlay.md)

## See Also

- [class MKOverlayRenderer](mkoverlayrenderer.md)
  The shared infrastructure for drawing overlays on the map surface.
- [class MKShape](mkshape.md)
  An abstract class that defines the basic properties for all shape-based overlay objects.
- [class MKMultiPoint](mkmultipoint.md)
  An abstract class that defines the common behavior that open and closed polygon overlays share.
- [class MKPlacemark](mkplacemark.md)
  A user-friendly description of a location on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlay)*