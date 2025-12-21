# PointOfInterestFilter

**Framework**: MapKit JS  
**Kind**: class

A filter for determining the points of interest to include or exclude on a map or in a local search.

**Availability**:
- MapKit JS 5.33.1+

## Declaration

```swift
class PointOfInterestFilter
```

#### Overview

You can apply a point-of-interest filter when you create a map ([`MapConstructorOptions`](mapconstructoroptions.md)), when you update an existing map ([`Map`](map.md)), or when you fetch points of interest ([`SearchConstructorOptions`](searchconstructoroptions.md)).

## Topics

### Creating filters
- [excluding(categories)](pointofinterestfilter/excluding.md)
  Creates a point-of-interest filter that excludes categories from a list that you provide.
- [including(categories)](pointofinterestfilter/including.md)
  Creates a point-of-interest filter that includes categories from a list that you provide.
- [excludingAllCategories](pointofinterestfilter/excludingallcategories.md)
  A filter that excludes all point-of-interest categories.
- [includingAllCategories](pointofinterestfilter/includingallcategories.md)
  A filter that includes all point-of-interest categories.
### Querying filter behavior
- [excludesCategory(category)](pointofinterestfilter/excludescategory.md)
  Returns a Boolean value that indicates whether the filter excludes the provided point-of-interest category.
- [includesCategory(category)](pointofinterestfilter/includescategory.md)
  Returns a Boolean value that indicates whether the filter includes the provided point-of-interest category.

## See Also

- [filterExcludingAllCategories](mapkit/filterexcludingallcategories.md)
  A value that excludes all point-of-interest categories.
- [filterIncludingAllCategories](mapkit/filterincludingallcategories.md)
  A value that includes all point-of-interest categories.
- [class PointsOfInterestSearch](pointsofinterestsearch.md)
  An object that fetches points of interest within a specified region.
- [class MapFeatureAnnotation](mapfeatureannotation.md)
  An object that represents a map feature that the user selects.
- [class MapFeatureAnnotationGlyphImage](mapfeatureannotationglyphimage.md)
  An object that describes map feature annotation images.
- [const PointOfInterestCategory](pointofinterestcategory.md)
  Point-of-interest categories.
- [const MapFeatureType](mapfeaturetype.md)
  Values that describe the feature type of a point of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/pointofinterestfilter)*