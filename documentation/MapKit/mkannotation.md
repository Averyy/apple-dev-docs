# MKAnnotation

**Framework**: MapKit  
**Kind**: protocol

An interface for associating your content with a specific map location.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
protocol MKAnnotation : NSObjectProtocol
```

#### Overview

An object that adopts this protocol manages the data that you want to display on the map surface. It doesn’t provide the visual representation that the map displays. Instead, your map view’s delegate provides the [`MKAnnotationView`](mkannotationview.md) objects necessary to display the content of your annotations. When you want to display content at a specific point on the map, add an annotation object to the map view. When the annotation’s [`coordinate`](mkannotation/coordinate.md) is visible on the map, the map view asks its delegate to provide an appropriate view to display any content associated with the annotation. You implement the [`mapView(_:viewFor:)`](mkmapviewdelegate/mapview(_:viewfor:)-8humz.md) method of the delegate to provide that view.

An object that adopts this protocol needs to implement the [`coordinate`](mkannotation/coordinate.md) property. The other methods of this protocol are optional.

## Topics

### Position attributes
- [var coordinate: CLLocationCoordinate2D](mkannotation/coordinate.md)
  The center point (specified as a map coordinate) of the annotation.
### Title attributes
- [var title: String?](mkannotation/title.md)
  The string containing the annotation’s title.
- [var subtitle: String?](mkannotation/subtitle.md)
  The string containing the annotation’s subtitle.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [MKOverlay](mkoverlay.md)
### Conforming Types
- [MKCircle](mkcircle.md)
- [MKClusterAnnotation](mkclusterannotation.md)
- [MKGeodesicPolyline](mkgeodesicpolyline.md)
- [MKMapFeatureAnnotation](mkmapfeatureannotation.md)
- [MKMapItemAnnotation](mkmapitemannotation.md)
- [MKMultiPoint](mkmultipoint.md)
- [MKMultiPolygon](mkmultipolygon.md)
- [MKMultiPolyline](mkmultipolyline.md)
- [MKPlacemark](mkplacemark.md)
- [MKPointAnnotation](mkpointannotation.md)
- [MKPolygon](mkpolygon.md)
- [MKPolyline](mkpolyline.md)
- [MKShape](mkshape.md)
- [MKTileOverlay](mktileoverlay.md)
- [MKUserLocation](mkuserlocation.md)

## See Also

- [class MKPlacemark](mkplacemark.md)
  A user-friendly description of a location on the map.
- [class MKAnnotationView](mkannotationview.md)
  The visual representation of one of your annotation objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotation)*