# PointsOfInterestSearch

**Framework**: MapKit JS  
**Kind**: class

An object that fetches points of interest within a specified region.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
class PointsOfInterestSearch extends Service
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Overview

Use [`PointsOfInterestSearch`](pointsofinterestsearch.md) to fetch points of interest. Mapkit JS exposes this functionality through a search object that makes network requests to the search service. To use search, create an instance of a [`PointsOfInterestSearch`](pointsofinterestsearch.md) object with the desired options and use the instance to make search requests. You may optionally specify a [`PointOfInterestFilter`](pointofinterestfilter.md) that lists categories to include or exclude. The default behavior of the fetch returns all points of interest.

To leverage the map’s current region to request points of interest, create a request with a rectangular bounding box using a [`CoordinateRegion`](coordinateregion.md). The request fetches points of interest within the rectangular region.

To retrieve points of interest nearby or “around the user,” create a request with a circular area defined by a center point of [`Coordinate`](coordinate.md) and a [`radius`](pointsofinterestsearchoptions/radius.md) in meters.

If you set a language ID, the fetch returns addresses in the selected language, if available; for instance, `fr-CA` or `fr-FR`. If you don’t provide a language ID, the fetch request uses the language ID initialized with the map.

## Topics

### Creating a Points of Interest Search
- [new PointsOfInterestSearch(options)](pointsofinterestsearch/pointsofinterestsearchconstructor.md)
  Creates a search object for fetching points of interest.
- [interface PointsOfInterestSearchConstructorOptions](pointsofinterestsearchconstructoroptions.md)
  Options that you provide when creating a points-of-interest search.
- [interface PointsOfInterestSearchOptions](pointsofinterestsearchoptions.md)
  Options that you may provide when you create a points of interest search.
- [region](pointsofinterestsearch/region.md)
  The region that bounds the area in which to fetch points of interest.
- [center](pointsofinterestsearch/center.md)
  The center point of the request represented as latitude and longitude.
- [radius](pointsofinterestsearch/radius.md)
  The distance provided in meters, or the longest distance derived from the center point to the region’s bounding box.
- [pointOfInterestFilter](pointsofinterestsearch/pointofinterestfilter.md)
  A filter that lists points of interest categories to include or exclude.
- [language](serviceconstructoroptions/language.md)
  A language identifier that determines the language for the service results text.
- [MaxRadius](pointsofinterestsearch/maxradius.md)
  The maximum distance to use from the center of the region for fetching points of interest.
### Fetching points of interest
- [search(callback, options)](pointsofinterestsearch/search.md)
  Fetches points of interest.
- [type PointsOfInterestSearchDelegate](pointsofinterestsearchdelegate.md)
  An object or callback function that MapKit JS calls when fetching points of interest.
- [interface PointsOfInterestSearchResponse](pointsofinterestsearchresponse.md)
  The result of a request used to fetch points of interest.
### Canceling a points of interest search
- [cancel(id)](service/cancel.md)
  Cancels a request using the provided request ID.

## Relationships

### Inherits From
- [Service](service.md)

## See Also

- [filterExcludingAllCategories](mapkit/filterexcludingallcategories.md)
  A value that excludes all point-of-interest categories.
- [filterIncludingAllCategories](mapkit/filterincludingallcategories.md)
  A value that includes all point-of-interest categories.
- [class PointOfInterestFilter](pointofinterestfilter.md)
  A filter for determining the points of interest to include or exclude on a map or in a local search.
- [class MapFeatureAnnotation](mapfeatureannotation.md)
  An object that represents a map feature that the user selects.
- [class MapFeatureAnnotationGlyphImage](mapfeatureannotationglyphimage.md)
  An object that describes map feature annotation images.
- [const PointOfInterestCategory](pointofinterestcategory.md)
  Point-of-interest categories.
- [const MapFeatureType](mapfeaturetype.md)
  Values that describe the feature type of a point of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/pointsofinterestsearch)*