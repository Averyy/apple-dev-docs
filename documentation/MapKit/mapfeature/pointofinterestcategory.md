# pointOfInterestCategory

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The point of interest category of the map feature.

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
var pointOfInterestCategory: MKPointOfInterestCategory? { get }
```

#### Discussion

If the feature doesn’t have a point of interest category, this value is `nil`.

## See Also

### Accessing the feature’s properties
- [var kind: MapFeature.FeatureKind](./kind.md)
  The kind of feature represented by the map feature.
- [MapFeature.FeatureKind](./featurekind.md)
  The kind of feature represented by a map feature.
- [var coordinate: CLLocationCoordinate2D](./coordinate.md)
  The coordinate of the map feature.
- [var title: String?](./title.md)
  The title of the map feature.
- [var backgroundColor: Color?](./backgroundcolor.md)
  The background color associated with the map feature.
- [var image: Image?](./image.md)
  An image associated with the map feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapfeature/pointofinterestcategory)*