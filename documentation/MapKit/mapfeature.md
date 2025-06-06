# MapFeature

**Framework**: MapKit  
**Kind**: struct

A tappable map feature.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
struct MapFeature
```

#### Overview

Tappable map features can include single points of interest, such as hotels and restaurants, a territory, or a physical map feature such as an ocean, basin, river, or mountain range.

## Topics

### Accessing the feature’s properties
- [var kind: MapFeature.FeatureKind](mapfeature/kind.md)
  The kind of feature represented by the map feature.
- [MapFeature.FeatureKind](mapfeature/featurekind.md)
  The kind of feature represented by a map feature.
- [var coordinate: CLLocationCoordinate2D](mapfeature/coordinate.md)
  The coordinate of the map feature.
- [var title: String?](mapfeature/title.md)
  The title of the map feature.
- [var backgroundColor: Color?](mapfeature/backgroundcolor.md)
  The background color associated with the map feature.
- [var image: Image?](mapfeature/image.md)
  An image associated with the map feature.
- [var pointOfInterestCategory: MKPointOfInterestCategory?](mapfeature/pointofinterestcategory.md)
  The point of interest category of the map feature.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [struct MapSelection](mapselection.md)
  A value representing a selected feature on a map.
- [protocol MapSelectable](mapselectable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapfeature)*