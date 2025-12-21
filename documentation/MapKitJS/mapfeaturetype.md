# MapFeatureType

**Framework**: MapKit JS  
**Kind**: enum

Values that describe the feature type of a point of interest.

**Availability**:
- MapKit JS 5.74.1+

## Declaration

```swift
const MapFeatureType: Readonly<{
    readonly PointOfInterest: "PointOfInterest";
    readonly Territory: "Territory";
    readonly PhysicalFeature: "PhysicalFeature";
}>
```

## Topics

### Feature types
- [PhysicalFeature](mapfeaturetype/physicalfeature.md)
  A physical feature on the Earth such as a mountain range, river, or ocean basin.
- [PointOfInterest](mapfeaturetype/pointofinterest.md)
  A feature that describes a point of interest, such as a museum, park, or cafe.
- [Territory](mapfeaturetype/territory.md)
  A feature that describes a territory, such as a region or neighborhood.
### Type Aliases
- [type MapFeatureType](mapfeaturetype/mapfeaturetype.md)
  A type alias that represents the values of the map feature type enumeration.

## See Also

- [filterExcludingAllCategories](mapkit/filterexcludingallcategories.md)
  A value that excludes all point-of-interest categories.
- [filterIncludingAllCategories](mapkit/filterincludingallcategories.md)
  A value that includes all point-of-interest categories.
- [class PointOfInterestFilter](pointofinterestfilter.md)
  A filter for determining the points of interest to include or exclude on a map or in a local search.
- [class PointsOfInterestSearch](pointsofinterestsearch.md)
  An object that fetches points of interest within a specified region.
- [class MapFeatureAnnotation](mapfeatureannotation.md)
  An object that represents a map feature that the user selects.
- [class MapFeatureAnnotationGlyphImage](mapfeatureannotationglyphimage.md)
  An object that describes map feature annotation images.
- [const PointOfInterestCategory](pointofinterestcategory.md)
  Point-of-interest categories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapfeaturetype)*