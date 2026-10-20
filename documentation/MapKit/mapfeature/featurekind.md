# MapFeature.FeatureKind

**Framework**: MapKit  
**Kind**: struct  
**Role**: Structure

The kind of feature represented by a map feature.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
struct FeatureKind
```

## Topics

### Kinds of features
- [static var physicalFeature: MapFeature.FeatureKind](./featurekind/physicalfeature.md)
  A physical map feature.
- [static var pointOfInterest: MapFeature.FeatureKind](./featurekind/pointofinterest.md)
  A point of interest.
- [static var territory: MapFeature.FeatureKind](./featurekind/territory.md)
  A territory or political boundary.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)

## See Also

### Accessing the feature’s properties
- [var kind: MapFeature.FeatureKind](./kind.md)
  The kind of feature represented by the map feature.
- [var coordinate: CLLocationCoordinate2D](./coordinate.md)
  The coordinate of the map feature.
- [var title: String?](./title.md)
  The title of the map feature.
- [var backgroundColor: Color?](./backgroundcolor.md)
  The background color associated with the map feature.
- [var image: Image?](./image.md)
  An image associated with the map feature.
- [var pointOfInterestCategory: MKPointOfInterestCategory?](./pointofinterestcategory.md)
  The point of interest category of the map feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapfeature/featurekind)*