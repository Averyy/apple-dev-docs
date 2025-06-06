# mapkit.PointOfInterestFilter

**Framework**: MapKit JS  
**Kind**: class

A filter for determining the points of interest to include or exclude on a map or in a local search.

**Availability**:
- MapKit JS 5.32.2+

## Declaration

```swift
interface mapkit.PointOfInterestFilter
```

#### Overview

You can apply a point of interest filter when you create a map ([`MapConstructorOptions`](mapconstructoroptions.md)), when you update an existing map ([`mapkit.Map`](mapkit.map/mapkit.map.md)), or when you fetch points of interest ([`SearchConstructorOptions`](searchconstructoroptions.md)).

## Topics

### Creating filters
- [including](mapkit.pointofinterestfilter/including.md)
  Creates a point of interest filter that includes categories from a list that you provide.
- [excluding](mapkit.pointofinterestfilter/excluding.md)
  Creates a point of interest filter that excludes categories from a list that you provide.
### Querying filter behavior
- [includingAllCategories](mapkit.pointofinterestfilter/includingallcategories.md)
  A filter that includes all point-of-interest categories.
- [excludingAllCategories](mapkit.pointofinterestfilter/excludingallcategories.md)
  A filter that excludes all point-of-interest categories.
- [includesCategory](mapkit.pointofinterestfilter/includescategory.md)
  Returns a Boolean value that indicates whether the filter includes the provided point-of-interest category.
- [excludesCategory](mapkit.pointofinterestfilter/excludescategory.md)
  Returns a Boolean value that indicates whether the filter excludes the provided point-of-interest category.

## See Also

- [mapkit.filterExcludingAllCategories](mapkit/mapkit.filterexcludingallcategories.md)
  A value that excludes all point-of-interest categories.
- [mapkit.filterIncludingAllCategories](mapkit/mapkit.filterincludingallcategories.md)
  A value that includes all point-of-interest categories.
- [mapkit.PointsOfInterestSearch](mapkit.pointsofinterestsearch.md)
  An object that fetches points of interest within a specified region.
- [mapkit.MapFeatureAnnotation](mapkit.mapfeatureannotation.md)
  An object that represents a map feature that the user selects.
- [mapkit.MapFeatureAnnotationGlyphImage](mapkit.mapfeatureannotationglyphimage.md)
  An object that describes map feature annotation images.
- [mapkit.PointOfInterestCategory](mapkit.pointofinterestcategory.md)
  Point-of-interest categories.
- [mapkit.MapFeatureType](mapkit.mapfeaturetype.md)
  Values that describe the feature type of a point of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.pointofinterestfilter)*