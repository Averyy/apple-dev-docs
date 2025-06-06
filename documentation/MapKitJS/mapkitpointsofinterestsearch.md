# mapkit.PointsOfInterestSearch

**Framework**: MapKit JS  
**Kind**: class

An object that fetches points of interest within a specified region.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
interface mapkit.PointsOfInterestSearch
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Overview

Use [`mapkit.PointsOfInterestSearch`](mapkit.pointsofinterestsearch/mapkit.pointsofinterestsearch.md) to fetch points of interest. Mapkit JS exposes this functionality through a search object that makes network requests to the search service. To use search, create an instance of a [`mapkit.PointsOfInterestSearch`](mapkit.pointsofinterestsearch/mapkit.pointsofinterestsearch.md) object with the desired options and use the instance to make search requests. You may optionally specify a [`mapkit.PointOfInterestFilter`](mapkit.pointofinterestfilter.md) that lists categories to include or exclude. The default behavior of the fetch returns all points of interest.

To leverage the map’s current region to request points of interest, create a request with a rectangular bounding box using a [`mapkit.CoordinateRegion`](mapkit.coordinateregion.md). The request fetches points of interest within the rectangular region.

To retrieve points of interest nearby or “around the user,” create a request with a circular area defined by a center point of [`mapkit.Coordinate`](mapkit.coordinate.md) and a [`radius`](pointsofinterestsearchoptions/radius.md) in meters.

If you set a language ID, the fetch returns addresses in the selected language, if available; for instance, `fr-CA` or `fr-FR`. If you don’t provide a language ID, the fetch request uses the language ID initialized with the map.

## Topics

### Creating a Points of Interest Search
- [mapkit.PointsOfInterestSearch](mapkit.pointsofinterestsearch/mapkit.pointsofinterestsearch.md)
  Creates a search object for fetching points of interest.
- [PointsOfInterestSearchOptions](pointsofinterestsearchoptions.md)
  Options that you may provide when you create a points of interest search.
- [region](mapkit.pointsofinterestsearch/region.md)
  The region that bounds the area in which to fetch points of interest.
- [center](mapkit.pointsofinterestsearch/center.md)
  The center point of the request represented as latitude and longitude.
- [radius](mapkit.pointsofinterestsearch/radius.md)
  The distance provided in meters, or the longest distance derived from the center point to the region’s bounding box.
- [pointOfInterestFilter](mapkit.pointsofinterestsearch/pointofinterestfilter.md)
  A filter that lists points of interest categories to include or exclude.
- [language](mapkit.pointsofinterestsearch/language.md)
  The language ID to use when fetching points of interest.
- [MaxRadius](mapkit.pointsofinterestsearch/maxradius.md)
  The maximum distance to use from the center of the region for fetching points of interest.
### Fetching points of interest
- [search](mapkit.pointsofinterestsearch/search.md)
  Fetches points of interest.
- [PointsOfInterestSearchDelegate](pointsofinterestsearchdelegate.md)
  An object or callback function that MapKit JS calls when fetching points of interest.
- [PointsOfInterestSearchResponse](pointsofinterestsearchresponse.md)
  The result of a request used to fetch points of interest.
### Canceling a points of interest search
- [cancel](mapkit.pointsofinterestsearch/cancel.md)
  Cancels a search request using its request ID.

## See Also

- [mapkit.filterExcludingAllCategories](mapkit/mapkit.filterexcludingallcategories.md)
  A value that excludes all point-of-interest categories.
- [mapkit.filterIncludingAllCategories](mapkit/mapkit.filterincludingallcategories.md)
  A value that includes all point-of-interest categories.
- [mapkit.PointOfInterestFilter](mapkit.pointofinterestfilter.md)
  A filter for determining the points of interest to include or exclude on a map or in a local search.
- [mapkit.MapFeatureAnnotation](mapkit.mapfeatureannotation.md)
  An object that represents a map feature that the user selects.
- [mapkit.MapFeatureAnnotationGlyphImage](mapkit.mapfeatureannotationglyphimage.md)
  An object that describes map feature annotation images.
- [mapkit.PointOfInterestCategory](mapkit.pointofinterestcategory.md)
  Point-of-interest categories.
- [mapkit.MapFeatureType](mapkit.mapfeaturetype.md)
  Values that describe the feature type of a point of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.pointsofinterestsearch)*